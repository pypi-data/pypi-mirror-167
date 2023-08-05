"""pyprote.py file."""

import logging
import os
from pathlib import Path
from typing import Optional

from pyprote.cli_argument_defaults import format_dict_defaults, out_dir_default


def fill_templates(
    format_dict: Optional[dict] = None,
    out_dir: Optional[str] = None,
) -> None:
    """Fill templates with package information.

    Args:
        format_dict (Optional[dict]): Dictionary with format strings.
        out_dir (Path): Output directory.
    """
    if format_dict is None:
        format_dict = format_dict_defaults
    if out_dir is None:
        out_dir = out_dir_default

    os.makedirs(out_dir, exist_ok=True)
    for template in (Path(__file__).parent / "templates").rglob("*_template"):
        output_path = get_output_path(template, format_dict["package_name"], out_dir)
        if template.is_dir():
            os.makedirs(output_path, exist_ok=True)
        else:
            if output_path.exists():
                logging.info(f"{output_path} already exists. Skipping.")
            else:
                file_content = format_file(template, output_path, format_dict)
                output_path.write_text(file_content)
                logging.info(f"{output_path} created.")


def get_output_path(template: Path, package_name: str, out_dir: str) -> Path:
    """Get output path for a template.

    Args:
        template (Path): Template path.
        package_name (str): Package name.
        out_dir (str): Output directory.

    Returns:
        Path: Output path.
    """
    templates_dir = Path(__file__).parent / "templates"

    template_path_formatted = str(template).replace("_template", "").replace("package_name", package_name)
    return Path(out_dir) / Path(template_path_formatted).relative_to(templates_dir)


def format_file(template: Path, output_path: Path, format_dict: dict) -> str:
    """Format file with black.

    Args:
        template (Path): Template file.
        output_path (Path): Output file path.
        format_dict (dict): Dictionary with format strings.

    Returns:
        str: Formatted file.
    """
    file_content = template.read_text()
    # json files have so many { and } that the template would become unreadable by replacing them
    # with LEFT_CURLY_BRACKET and RIGHT_CURLY_BRACKET
    if output_path.suffix == ".json":
        return file_content
    file_content = file_content.format(**format_dict)
    return file_content.replace("LEFT_CURLY_BRACKET", "{").replace("RIGHT_CURLY_BRACKET", "}")
