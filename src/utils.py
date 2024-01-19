from common_utils import connect_vault
from common_utils import get_config
from common_utils import get_secret


def get_db_config(db_name: str) -> dict:
    """
    Retrieves database configuration from a configuration file, with optional secret retrieval from HashiCorp Vault.

    Args:
        db_name (str): The name of the database configuration to retrieve.

    Returns:
        dict: A dictionary containing the database configuration.

    Raises:
        KeyError: If the specified database name is not found in the configuration file.

    Example:
        >>> database_config = get_db_config("my_database")
    """
    config = get_config("config", "databases")
    db_config = config[db_name]

    if "secret" in db_config:
        client = connect_vault()
        secrets = get_secret(client, db_config["secret"])

        for key, value in db_config["protected"].items():
            db_config[key] = secrets[value]

    return db_config
