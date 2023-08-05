"""Entry point to the cli commands."""
import argparse
import logging
from logging.config import dictConfig

from pyprote.cli_argument_defaults import (
    example_call,
    format_dict_defaults,
    out_dir_default,
)
from pyprote.logging_config.logger_config import get_logger_config
from pyprote.pyprote import fill_templates

dictConfig(get_logger_config())


def main():
    """Entry point to the cli commands."""
    parser = argparse.ArgumentParser(description="Pyprote - Python Package Template Generator")

    # add example_call to help page of the cli
    parser.add_argument("-e", "--example", action="store_true", help=f"Example call: {example_call}")

    # add cli arguments
    fill_arg_parser(parser)

    # add out_dir argument to the parser
    parser.add_argument("--out_dir", default=out_dir_default, help="Output directory")

    args = parser.parse_args()
    if args.example:
        logging.info(example_call)
        return 0

    format_dict_input = {
        "package_name": args.package_name,
        "package_version": args.package_version,
        "package_description": args.package_description,
        "package_author_name": args.package_author_name,
        "package_author_email": args.package_author_email,
        "package_link": args.package_link,
    }
    logging.info(format_dict_input)
    logging.info("Running pyprote on the command line: ")
    fill_templates(format_dict_input, args.out_dir)


def fill_arg_parser(parser):
    """Fill the argparse with the cli arguments."""
    for argument_name, default_val in format_dict_defaults.items():
        cli_command = f"--{argument_name}"
        cli_command_help = f"{argument_name} value"
        parser.add_argument(cli_command, default=default_val, help=cli_command_help)


if __name__ == "__main__":
    main()
