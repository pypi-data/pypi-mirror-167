"""This module contains the cli arguments with their default values."""
format_dict_defaults = {
    "package_name": "PY_PRO_TE_FILL_ME_IN",
    "package_version": "0.1.0",
    "package_description": "PY_PRO_TE_FILL_ME_IN",
    "package_author_name": "PY_PRO_TE_FILL_ME_IN",
    "package_author_email": "PY_PRO_TE_FILL_ME_IN",
    "package_link": "PY_PRO_TE_FILL_ME_IN",
}

out_dir_default = "pyprote_output_dir"

example_call = "pyprote "
for argument_name, default_val in format_dict_defaults.items():
    example_call = f"{example_call} --{argument_name} '{default_val}'"
example_call = f"{example_call} --out_dir '{out_dir_default}'"
