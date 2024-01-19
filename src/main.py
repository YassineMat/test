from common_utils import get_config


def function_to_test() -> int:
    """A function to be tested with pytest.
    Note: All your functions must be tested with pytest
    """
    return 1


def main() -> None:
    """Example usage of 'config' variable declared by Hydra
    Hello world, I document my code well, I use static typing and I configure my python project with Hydra!
    """
    config = get_config("config", "main")
    n: int = config["vars"]["iteration"]
    for i in range(n):
        print(config["vars"]["greeting_message"])


if __name__ == "__main__":
    main()
