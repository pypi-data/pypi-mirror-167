import os
from bodo_platform_utils.utils_types import CloudProvider

WORKSPACE_UUID = os.environ.get("BODO_PLATFORM_WORKSPACE_UUID")
REGION = os.environ.get("BODO_PLATFORM_WORKSPACE_REGION")
# Default to AWS for now.
CLOUD_PROVIDER = CloudProvider(
    os.environ.get("BODO_PLATFORM_WORKSPACE_CLOUD_PROVIDER", "AWS")
)

# This is related to Snowflake Partner Connect, we use the same constant in the backend
# to store the data coming from Partner Connect.
SNOWFLAKE_PC_CATALOG_NAME = 'snowflake_pc'

CATALOG_PREFIX = "catalog-secret"
DEFAULT_SECRET_GROUP = "default"
