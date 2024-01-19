import os

import hvac
from yaml import safe_load


def get_config(config_path: str, config_name: str) -> dict:
    """
    Retrieves configuration data from a YAML file using PyYAML.

    Args:
        config_path (str): The path to the directory containing the YAML file.
        config_name (str): The name of the YAML file (excluding extension).

    Returns:
        dict: A dictionary containing the configuration data loaded from the YAML file.

    Raises:
        FileNotFoundError: If the specified YAML file is not found at the given path.
        yaml.YAMLError: If there is an error in parsing the YAML file.

    Example:
        >>> config_data = get_config("/path/to/configs", "example_config")
    """
    config: dict = {}
    sep: str = "/"
    ext: str = ".yaml"
    path: str = config_path + sep + config_name + ext
    with open(path, "r") as file:
        config: dict = safe_load(file)
    return config


def connect_vault() -> hvac.Client:
    """
    Connects to HashiCorp Vault using the userpass authentication method.
    Environment variables: VAULT_USER and VAULT_PASSWD, must be set beforehand.

    Returns:
        hvac.Client: A HashiCorp Vault client authenticated with the provided credentials.

    Raises:
        KeyError: If the required environment variables (VAULT_USER, VAULT_PASSWD) are not set.
        hvac.exceptions.InvalidRequest: If there is an issue with the Vault connection or authentication.

    Example:
        >>> vault_client = connect_vault()
    """
    client = hvac.Client(url="https://deploy.innovafeed.com:8200")
    client.auth.userpass.login(
        username=os.environ["VAULT_USER"], password=os.environ["VAULT_PASSWD"]
    )
    return client


def get_secret(client: hvac.Client, secret: str) -> dict:
    """
    Retrieves a secret from HashiCorp Vault.

    Args:
        client (hvac.Client): A HashiCorp Vault client authenticated with the required credentials.
        secret (str): The path to the secret within the Vault.

    Returns:
        Union[dict, ConnectionError]: A dictionary containing the secret data, or a ConnectionError if not authenticated.

    Raises:
        hvac.exceptions.Forbidden: If not enough permission to read the secret from Vault.

    Example:
        >>> secret_data = get_secret(vault_client, "path/to/secret")
    """
    read_response = client.secrets.kv.v1.read_secret(path=secret, mount_point="kv")
    data = read_response["data"]
    return data
