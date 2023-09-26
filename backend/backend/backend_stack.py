from aws_cdk import (
    Stack,
    aws_dynamodb as dynamodb,
    aws_cognito as cognito,
)
from constructs import Construct

class CrushEmoryBackendStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Import existing Cognito User Pool
        user_pool = cognito.UserPool.from_user_pool_id(
            self,
            "ExistingUserPool",
            "us-east-1_9MHY29BIx"  # Replace with your actual User Pool ID
        )

        # DynamoDB table for all Users
        users_table = dynamodb.Table(
            self, "UsersTable",
            partition_key=dynamodb.Attribute(
                name="userId",
                type=dynamodb.AttributeType.STRING
            )
        )

        # DynamoDB table for Likes
        likes_table = dynamodb.Table(
            self, "LikesTable",
            partition_key=dynamodb.Attribute(
                name="userId",
                type=dynamodb.AttributeType.STRING
            ),
            sort_key=dynamodb.Attribute(
                name="likedUserId",
                type=dynamodb.AttributeType.STRING
            )
        )

        # DynamoDB table for Friends
        friends_table = dynamodb.Table(
            self, "FriendsTable",
            partition_key=dynamodb.Attribute(
                name="userId",
                type=dynamodb.AttributeType.STRING
            )
        )

        # DynamoDB table for Matches
        matches_table = dynamodb.Table(
            self, "MatchesTable",
            partition_key=dynamodb.Attribute(
                name="userId",
                type=dynamodb.AttributeType.STRING
            )
        )
