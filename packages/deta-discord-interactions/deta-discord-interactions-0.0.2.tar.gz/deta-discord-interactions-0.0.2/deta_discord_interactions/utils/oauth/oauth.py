"Deals with OAuth2, creating and saving Webhooks"
import json
import os
from typing import Callable, NoReturn
from urllib.parse import quote, unquote

import requests
from deta_discord_interactions.models.component import ActionRow, Button, ButtonStyles

from deta_discord_interactions.models.message import Message

from deta_discord_interactions.discord import DiscordInteractions
from deta_discord_interactions.context import Context

from deta_discord_interactions.utils.database import Database
from deta_discord_interactions.utils.oauth.model import OAuthToken, PendingOAuth


DISCORD_BASE_URL = 'https://discord.com/api/v10'
DEFAULT_MICRO_PATH = "https://{MICRO}.deta.dev"

pending_oauths = Database(name="_discord_interactions_pending_oauths")


def enable_oauth(app: DiscordInteractions, /, *, path: str = "/oauth") -> None:
    "Allows for the app to receive and process OAuth and create Webhooks"
    app.route(path)(_handle_oauth)


def request_oauth(
    ctx: Context,
    /,
    internal_id: str,
    *,
    domain: str = DEFAULT_MICRO_PATH,
    path: str = "/oauth",
    scope: str,
    callback: Callable,
    args: tuple = [],
    kwargs: dict = {},
    message_content: str = "Use the button to register with OAuth",
    button_label: str = "Grant OAuth",
) -> Message:
    """Utility function to make OAuth creation and usage easier
    
    Returns a Message with a link the user must visit to grant an OAuth Token,
    and save a PendingOAuth in the internal database.

    See https://discord.com/developers/docs/topics/oauth2 for the list of available scopes and more information

    Parameters
    ----------
    ctx : Context
        The Context this function is being called from
    internal_id : str
        ID to be used internally. Will be shown in the link.. Will be shown in the link.
    domain : str, default https://{MICRO}.deta.dev
        Base URL for the Micro running the bot
        {MICRO} is filled automatically from the environment variables
    path : str, default '/oauth'
        Path that the user will be sent back to. 
        Must match what has been passed to `enable_webhooks` and be set on the Developer Portal
    scope : str
        OAuth scopes to request, separated by spaces.
    callback : Callable
        Must be a normal function, not a lambda, partial nor a class method.
    args : tuple|list
    kwargs : dict
        Arguments and Keyword arguments to be passed onto callback
        The created newly created OAuthToken and Context passed to request_oauth are always passed first.
    message_content : str
        Message content, besides the button with the URL
    button_label : str
        The URL Button's label


    If the user never finishes the authorization process, the callback will not be called
    If they create one , it will be called with ctx, webhook, `args` and `kwargs`
    The link will only work for one authorization
    """
    promise = PendingOAuth(
        ctx,
        callback.__module__,
        callback.__name__,
        args,
        kwargs,
    )
    redirect_uri = (
        quote(
            domain.format(MICRO = os.getenv("DETA_PATH")) + path,
            safe=''
        )
    )

    with pending_oauths[internal_id] as record:
        record["pending_oauth"] = promise
        record["redirect_uri"] = redirect_uri

    link = (
        f"{DISCORD_BASE_URL}/oauth2/authorize?"
        "response_type=code&"
        f"scope={quote(scope)}&"
        f"guild_id={ctx.guild_id}&"
        f"client_id={os.getenv('DISCORD_CLIENT_ID')}&"
        f"state={internal_id}&"
        f"redirect_uri={redirect_uri}"
    )

    return Message(
        message_content,
        components=[ActionRow([
            Button(
                style=ButtonStyles.LINK,
                url=link,
                label=button_label,
            )
        ])],
        ephemeral=True,
    )


# Mostly for convenience and more... idk, semantic
def create_webhook(
    ctx: Context,
    /,
    internal_id: str,
    domain: str = DEFAULT_MICRO_PATH,
    path: str = "/oauth",
    *,
    callback: Callable,
    args: tuple = (),
    kwargs: dict = {},
    message_content: str = "Use the button to register the Webhook",
    button_label: str = "Create Webhook",
) -> Message:
    """Utility function to make Webhook creation and usage easier
    
    Returns a Message with a link the user must visit to create a webhook,
    and save a PendingWebhook in the internal database.

    Parameters
    ----------
    ctx : Context
        The Context this function is being called from
    internal_id : str
        ID to be used internally. Will be shown in the link.
    domain : str, default https://{MICRO}.deta.dev
-        Base URL for the Micro running the bot
        {MICRO} is filled automatically from the environment variables
    path : str, default '/oauth'
        Path that the user will be sent back to. 
        Must match what has been passed to `enable_webhooks` and be set on the Developer Portal
    callback : Callable
        Must be a normal function, not a lambda, partial nor a class method.
    args : tuple|list
    kwargs : dict
        Arguments and Keyword arguments to be passed onto callback.
        The created newly created OAuthToken and Context passed to create_webhook are always passed first.
    message_content : str
        Message content, besides the button with the URL
    button_label : str
        The Label of the button


    If the user never finishes creating a webhook, the callback will not be called
    If they create one , it will be called with ctx, webhook, `args` and `kwargs`
    The link will only work for one webhook
    """
    return request_oauth(
        ctx,
        internal_id,
        domain=domain,
        path=path,
        scope='webhook.incoming',
        callback=callback,
        args=args,
        kwargs=kwargs,
        message_content=message_content,
        button_label=button_label,
    )



def _handle_oauth(
    request: dict,
    start_response: Callable[[str, list], None],
    abort: Callable[[int, str], NoReturn],
) -> list[str]:
    try:
        code = request["query_dict"]["code"]
        state = request["query_dict"]["state"]
        # guild_id = request["query_dict"]["guild_id"]
    except KeyError:
        abort(400, 'Invalid URL')

    url = DISCORD_BASE_URL + "/oauth2/token"

    try:

        with pending_oauths[state] as record:
            redirect_uri: str = record["redirect_uri"]
            pending_oauth: PendingOAuth = record["pending_oauth"]

        del pending_oauths[state]

        data = {
            'client_id': os.getenv("DISCORD_CLIENT_ID"),
            'client_secret': os.getenv("DISCORD_CLIENT_SECRET"),
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': unquote(redirect_uri),
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(url, data=data, headers=headers)
        response.raise_for_status()
        result = response.json()

        oauth_token = OAuthToken.from_dict(result)

        callback_response = pending_oauth.execute_callback(oauth_token)

        if isinstance(callback_response, (dict, list, int, str)):
            callback_response = json.dumps(callback_response)
        if isinstance(callback_response, str):
            callback_response = callback_response.encode("UTF-8")
        if not isinstance(callback_response, bytes):
            raise Exception("The Callback response should be a dictionary, a string or bytes")


        start_response("200 OK", [('Content-Type', 'application/json')])
        return [callback_response]

    except Exception:
        import traceback
        traceback.print_exc()
        try:
            print('response content', response.content, flush=True)
        except Exception:
            pass
        abort(500, "Something went wrong")
