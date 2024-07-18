def get_env_dir():
    get_env_dir = input("Please enter which enviroment directory you want to run file compare on\nThe options are\n1.Development\n2.Staging\n3.Production.")
    match get_env_dir.lower():
        case "devevelopment":
            print(f"You entered {get_env_dir}.\nInitiating file parsing and comparisons.\nPlease standby for results.\n")
            return "dev"
        case "dev":
            print(f"You entered {get_env_dir}.\nInitiating file parsing and comparisons.\nPlease standby for results.\n")
            return "dev"
        case "staging":
            print(f"You entered {get_env_dir}.\nInitiating file parsing and comparisons.\nPlease standby for results.\n")
            return "staging"
        case "production":
            print(f"You entered {get_env_dir}.\nInitiating file parsing and comparisons.\nPlease standby for results.\n")
            return "prod"
        case "prod":
            print(f"You entered {get_env_dir}.\nInitiating file parsing and comparisons.\nPlease standby for results.\n")
            return "prod"
        case _:
            raise ValueError(f"Invalid input entere(Entered: {get_env_dir}). Please re-run and enter a valid command.")
