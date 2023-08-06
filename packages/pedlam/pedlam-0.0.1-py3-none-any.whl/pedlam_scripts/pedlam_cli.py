import argparse
import colorlog
import logging

from pedlam.Driver import Driver
from pedlam.helpers.PackageHelper import PackageHelper

def require_arguments():
    """Get the arguments from CLI input.

    Returns:
        :class:`argparse.Namespace`: A namespace with all the parsed CLI arguments.

    """

    parser = argparse.ArgumentParser(
        prog=PackageHelper.get_alias(),
        formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=150, width=150)
    )

    optional = parser._action_groups.pop()
    required = parser.add_argument_group("required arguments")

    required.add_argument("-s", "--size", help="The size of the memory to allocate.", required=True, type=int, default=8)

    parser._action_groups.append(optional)
    return parser.parse_args()

def setup_logger():
    """Setup ColorLog to enable colored logging output."""

    # Colored logging
    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        "%(log_color)s[%(levelname)s] %(message)s",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "white",
            "SUCCESS": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "red,bg_white"
        }
    ))

    logger = colorlog.getLogger()
    logger.addHandler(handler)

    # Also show INFO logs
    logger.setLevel(logging.INFO)

    # Add SUCCESS logging
    logging.SUCCESS = 25
    logging.addLevelName(
        logging.SUCCESS,
        "SUCCESS"
    )

    setattr(
        logger,
        "success",
        lambda message, *args: logger._log(logging.SUCCESS, message, args)
    )

def print_banner():
    """Print a useless ASCII art banner to make things look a bit nicer."""

    print("""
██████╗ ███████╗██████╗ ██╗      █████╗ ███╗   ███╗
██╔══██╗██╔════╝██╔══██╗██║     ██╔══██╗████╗ ████║
██████╔╝█████╗  ██║  ██║██║     ███████║██╔████╔██║
██╔═══╝ ██╔══╝  ██║  ██║██║     ██╔══██║██║╚██╔╝██║
██║     ███████╗██████╔╝███████╗██║  ██║██║ ╚═╝ ██║
╚═╝     ╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
Version """ + PackageHelper.get_version() + """ - Copyright 2022 Pedlam Nur
    """)

def main():
    """Start Pedlam."""

    print_banner()
    setup_logger()

    driver = Driver(require_arguments())
    driver.start()

if __name__ == "__main__":
    main()
