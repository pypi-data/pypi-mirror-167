#!/usr/bin/env python3
"""Configuration management for Constellate."""

from os import PathLike
from typing import Union
import toml

class ConstellateConfig:
    """Configuration for Constellate."""
    def __init__(self, theme="default", local_panel_url="http://localhost:5006", prod_panel_url="http://localhost:5006"):
        """Creates a new configuration.

        Parameters
        ----------
        theme :string
            The theme to use. "default" and "rho" are included by default.
        local_panel_url : string
            The URL for the Panel server used when running development.
        prod_panel_url : string
            The URL for the Panel server used in Vercel deployment.
        """
        self.theme = theme
        self.local_panel_url = local_panel_url
        self.prod_panel_url = prod_panel_url

    @classmethod
    def from_toml(cls, filename: Union[str, PathLike]):
        """Initializes configuration from a TOML file."""
        with open(filename, 'r') as infile:
            data = toml.load(infile)

        return cls(**data)

    def to_env_files(self, local_fn: Union[str, PathLike], prod_fn: Union[str, PathLike]):
        """Converts to two env files of the form accepted by NextJS and writes to output."""
        with open(local_fn, 'w') as out:
            out.write(f"""CONSTELLATE_THEME={self.theme}
PANEL_URL={self.local_panel_url}
""")

        with open(prod_fn, 'w') as out:
            out.write(f"""CONSTELLATE_THEME={self.theme}
PANEL_URL={self.prod_panel_url}
""")
