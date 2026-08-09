import asyncio
from datetime import datetime, timezone

from fastapi import WebSocket, WebSocketDisconnect, status

from schemas.user_activity import UpdateUserActivitySchema
from security.interfaces import JWTAuthManagerInterface
from exceptions import TokenExpiredError, InvalidTokenError
from user_activity.interfaces import (
    UserActivityServiceInterface,
    UserActivityWebSocketManagerInterface,
    UserActivityRepoInterface
)


class UserActivityService(UserActivityServiceInterface):
    """Coordinates authentication and lifecycle handling for user activity WebSocket connections."""

    def __init__(
            self,
            manager: UserActivityWebSocketManagerInterface,
            activity_repo: UserActivityRepoInterface,
            jwt_auth_manager: JWTAuthManagerInterface
    ) -> None:
        """
        Initialize the service with its collaborating components.

        Args:
            manager (UserActivityWebSocketManagerInterface): Manager responsible for tracking
                active WebSocket connections and broadcasting events.
            activity_repo (UserActivityRepoInterface): Repository used to persist user activity state.
            jwt_auth_manager (JWTAuthManagerInterface): Manager used to decode and validate access tokens.
        """
        self.activity_ws_manager = manager
        self.activity_repo = activity_repo
        self.jwt_auth_manager = jwt_auth_manager

    async def process(self, websocket: WebSocket) -> None:
        """
        Handle the full lifecycle of a single user activity WebSocket connection.

        Accepts the connection, authenticates the user via a token sent as the
        first message, registers the connection, broadcasts online status,
        and cleans up (marking the user offline) once the connection closes.

        Args:
            websocket (WebSocket): The incoming WebSocket connection.

        Returns:
            None
        """
        # Write your code here
