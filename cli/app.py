"""
CLI interface for the social network application.
"""

import sys
from service.social_network import SocialNetworkService
from cli.utils import detect_command_type, CommandType

def run_cli():
    """
    Starts the interactive command-line interface for the social network.
    Validates input before sending to the service layer.
    """
    sn = SocialNetworkService()
    print("Welcome to the Social Networking App. Type your command:")
    while True:
        try:
            command = input("> ").strip()
            command_type = detect_command_type(command)

            if command_type == CommandType.EXIT:
                print("Goodbye!")
                break
            elif command_type == CommandType.UNKNOWN:
                print("Invalid command format.")
                continue

            output = sn.handle_command(command_type, command)
            if output:
                print(output)

        except (KeyboardInterrupt, EOFError):
            print("\nExiting...")
            sys.exit(0)

if __name__ == "__main__":
    run_cli()