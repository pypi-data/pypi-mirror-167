"""
This module defines some extensions for :mod:`nio`, as it is currently missing some methods that :mod:`lokiunimore` desperately needs.
"""

import aiohttp
import nio
import nio.crypto
import logging
import hashlib
import hmac
import typing as t

T = t.TypeVar("T")
Something = t.TypeVar("Something")
log = logging.getLogger(__name__)

from lokiunimore.utils.device_names import generate_device_name


class RequestError(Exception):
    """
    A request to the Matrix homeserver failed.
    """

    def __init__(self, response: nio.responses.ErrorResponse):
        super().__init__()
        self.response: nio.responses.ErrorResponse = response


# noinspection PyProtectedMember
class ExtendedAsyncClient(nio.AsyncClient):
    """
    An :class:`~nio.AsyncClient` with some extra features to be upstreamed some day.
    """

    def __repr__(self):
        return f"<{self.__class__.__qualname__} for {self.user} at {self.homeserver}>"

    def _send(
            self,
            response_class: t.Type[T],
            method: str,
            path: str,
            data: t.Union[None, str, nio.crypto.AsyncDataT] = None,
            response_data: t.Optional[t.Tuple[t.Any, ...]] = None,
            content_type: t.Optional[str] = None,
            trace_context: t.Optional[t.Any] = None,
            data_provider: t.Optional[nio.DataProvider] = None,
            timeout: t.Optional[float] = None,
            content_length: t.Optional[int] = None,
    ) -> T:
        """
        Override :meth:`nio.client.AsyncClient._send` with something that actually raises errors instead of returning them.

        .. danger::

            SUPER UNTESTED. PLEASE WORK. PLEASE DO. PLEASE DO NOT EXPLODE IN PRODUCTION.
        """
        result = super()._send(
            response_class=response_class,
            method=method,
            path=path,
            data=data,
            response_data=response_data,
            content_type=content_type,
            trace_context=trace_context,
            data_provider=data_provider,
            timeout=timeout,
            content_length=content_length,
        )

        if isinstance(result, nio.responses.ErrorResponse):
            log.warning(f"{method} {path} errored: {result!r}")
            raise RequestError(result)

        return result

    async def register_with_shared_secret(self, shared_secret: str, username: str, displayname: str, password: str):
        """
        Given the homeserver's shared secret, perform a `shared-secret registration <https://matrix-org.github.io/synapse/latest/admin_api/register_api.html#shared-secret-registration>`_.

        :param shared_secret: The shared secret to register with.
        :param username: The username of the user to register.
        :param displayname: The displayname of the user to register.
        :param password: The password of the user to register.
        :raises aiohttp.ClientResponseError: If a request is not successful.

        .. note:: ``shared_secret`` is not the same shared secret of :meth:`.login_with_shared_secret`.
        """

        log.debug(f"Registering via shared-secret registration: {username}")

        path = nio.Api._build_path(
            ["v1", "register"],
            base_path="/_synapse/admin"
        )

        nonce: aiohttp.ClientResponse = await self.send("GET", path)
        nonce.raise_for_status()
        nonce: dict[str, ...] = await nonce.json()
        nonce: str = nonce["nonce"]

        mac = hmac.new(shared_secret.encode("utf8"), digestmod=hashlib.sha1)
        mac.update(nonce.encode("utf8"))
        mac.update(b"\0")
        mac.update(username.encode("utf8"))
        mac.update(b"\0")
        mac.update(password.encode("utf8"))
        mac.update(b"\0")
        mac.update(b"notadmin")

        registration: aiohttp.ClientResponse = await self.send("POST", path, nio.Api.to_json({
            "nonce": nonce,
            "username": username,
            "displayname": displayname,
            "password": password,
            "admin": False,
            "mac": mac.hexdigest()
        }))
        registration.raise_for_status()

        log.info(f"Registered via shared-secret registration: {username}")

    async def login_with_shared_secret(self, shared_secret: str) -> None:
        """
        Given a shared secret, perform a login via `com.devture.shared_secret_auth <https://github.com/devture/matrix-synapse-shared-secret-auth>`_.

        :param shared_secret: The shared secret to login with.

        .. note:: ``shared_secret`` is not the same shared secret of :meth:`.register_with_shared_secret`.
        """

        log.debug(f"Logging in as {self.user} with a shared secret...")

        token = hmac.new(key=shared_secret.encode("utf8"), msg=self.user.encode("utf8"), digestmod=hashlib.sha512).hexdigest()

        await self.login_raw({
            "type": "com.devture.shared_secret_auth",
            "identifier": {
                "type": "m.id.user",
                "user": self.user,
            },
            "token": token,
            "initial_device_display_name": generate_device_name(__name__),
        })

        log.debug(f"Login successful!")

    async def room_hierarchy(self, room_id: str, max_depth: int, suggested_only: bool) -> list[dict]:
        """
        Given a space, get the room hierarchy.

        :param room_id: The id of the space to get the hierarchy of.
        :param max_depth: The max depth of subspaces to recurse into.
        :param suggested_only: Whether only suggested rooms should be returned.
        :return: 
        """

        log.debug(f"Getting room hierarchy for: {room_id!r}")

        current = None
        rooms = []

        while True:
            path = ["rooms", room_id, "hierarchy"]
            query = {
                "max_depth": str(max_depth),
                "suggested_only": str(suggested_only).lower(),
            }
            if current:
                query["from"] = current

            result: aiohttp.ClientResponse = await self.send(
                "GET",
                nio.Api._build_path(path, query, base_path="/_matrix/client/v1"),
                headers={
                    "Authorization": f"Bearer {self.access_token}"
                }
            )
            result: dict = await result.json()

            rooms = [*rooms, *result["rooms"]]

            current = result.get("next_batch")
            if not current:
                break

        log.debug(f"Successfully retrieved a hierarchy of {len(rooms)} rooms!")

        return rooms

    async def find_or_create_pm_room(self, user_id: str) -> str:
        """
        Find the first available private message room with the given user, or create one if none exist.

        :param user_id: The user to message.
        :returns: The room id of the created room.
        """

        log.debug(f"Sliding into {user_id}'s PMs...")

        for room in self.rooms.values():
            is_dm = "m.direct" in room.tags
            is_group = room.is_group
            has_two_users = len(room.users) + len(room.invited_users) == 2
            contains_user_id = user_id in room.users.keys() or user_id in room.invited_users.keys()

            if (is_dm or is_group) and has_two_users and contains_user_id:
                log.debug(f"Found PM room for: {user_id}")
                return room.room_id
        else:
            log.debug(f"Creating new PM room for: {user_id}")
            response = await self.room_create(invite=[user_id], is_direct=True)
            if isinstance(response, nio.RoomCreateResponse):
                log.info(f"Created new PM room for: {user_id}")
                return response.room_id
            else:
                raise Exception("Failed to slide into an user's PMs.")

    async def room_send_message_html(self, room_id: str, text: str, html: str) -> Something:
        """
        Send an HTML message with a text fallback.

        :param room_id: The ID of the room to send the message in.
        :param text: The plain text fallback of the message.
        :param html: The HTML message.
        :return: I have no idea, whatever :meth:`~nio.client.AsyncClient.room_send` does.
        """

        return await self.room_send(room_id, "m.room.message", {
            "msgtype": "m.notice",
            "format": "org.matrix.custom.html",
            "formatted_body": html,
            "body": text,
        })

    async def mention_html(self, user_id: str) -> str:
        """
        Create a rich HTML mention.

        To provide a text fallback for the HTML mention, use the ``user_id``.

        :param user_id: The user to mention.
        :return: The HTML string.
        """

        display_name = await self.get_displayname(user_id)

        # language=html
        return f"""<a href="https://matrix.to/#/{user_id}">{display_name}</a>"""
