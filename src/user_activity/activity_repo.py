from typing import List

from pymongo.asynchronous.database import AsyncDatabase

from schemas.user_activity import UserBaseDTO, UpdateUserActivitySchema, UserActivitySchema
from user_activity.interfaces import UserActivityRepoInterface


class UserActivityRepository(UserActivityRepoInterface):
    """MongoDB-backend implementation of the user activity repository."""

    def __init__(self, db: AsyncDatabase) -> None:
        """
        Initialize the repository with a MongoDB database instance.

        Args:
            db (AsyncDatabase): The Motor async MongoDB database instance.
        """
        self.db = db

    async def create_user_activity(self, user_data: UserBaseDTO) -> None:
        """
        Create or reset a user's activity record with an initial "offline" status.

        Args:
            user_data (UserBaseDTO): Basic user data (id and email) to seed the activity record.

        Returns:
            None
        """
        # Write your code here

    async def update_user_activity(
            self,
            user_data: UpdateUserActivitySchema
    ) -> UserActivitySchema:
        """
        Update (or create) a user's activity record and return the resulting document.

        Args:
            user_data (UpdateUserActivitySchema): Fields to update on the user's activity record.

        Returns:
            UserActivitySchema: The updated activity record.
        """
        # Write your code here

    async def get_all_active_users(self) -> List[UserActivitySchema]:
        """
        Retrieve all users that currently have an "online" status.

        Returns:
            List[UserActivitySchema]: A list of activity records for all online users.
        """
        # Write your code here
