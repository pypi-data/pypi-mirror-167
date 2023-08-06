from bodo_platform_utils.config import CATALOG_PREFIX, SNOWFLAKE_PC_CATALOG_NAME, DEFAULT_SECRET_GROUP
from bodo_platform_utils.secrets import get


# Users have to use the below helper functions to get the secrets from SSM.
def get_data(name=None, _parallel=True):
    """
    :param name: Name of the Catalog
    :param _parallel: Defaults to True
   :return: JSON object containing the Catalog data
   """
    if name is None:
        name = SNOWFLAKE_PC_CATALOG_NAME

    catalog_name = f"{CATALOG_PREFIX}-{name}"

    # Currently all the catalogs will be stored under default secret group.
    # Default secret group will be created at the time of workspace creation.
    return get(catalog_name, DEFAULT_SECRET_GROUP, _parallel)

