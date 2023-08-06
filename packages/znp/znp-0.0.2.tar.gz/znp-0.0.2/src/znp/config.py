#!/usr/bin/env python3
from .appdirs import user_config_dir as appdirs
import os
import sys
import pathlib
from shlex import split
import csv


class UserSettings:
    """Class for managing user config files"""

    # User files containing their location on the system
    conf_dir = None
    conf_file = None

    # Command line args passed by user
    # This is an argparse object
    cmd_args = None

    # User's settings as set in their conf and filters files
    prompt_cmd = None

    def __init__(self, program, cmd_line_args=None):
        self.add_cmd_args(cmd_line_args=cmd_line_args)
        self.set_files(program=program)
        self.validate_config()
        self.read_config()

    @classmethod
    def add_cmd_args(cls, cmd_line_args=None):
        cls.cmd_args = cmd_line_args

    @classmethod
    def set_files(cls, program=None):
        """Return user config directory and config_files dict"""

        cls.conf_dir = appdirs(program)
        config_files = {
            "conf_file": f"{program}.conf",
        }

        for key, value in config_files.items():
            value = os.path.join(cls.conf_dir, value)
            setattr(cls, key, value)

    @classmethod
    def read_config(cls):
        """Read user config files and update user_args"""

        with open(cls.conf_file) as conf:
            reader = csv.reader(
                conf, delimiter="=", escapechar="\\", quoting=csv.QUOTE_NONE
            )

            config_settings = ["prompt_cmd"]

            for row in reader:
                if len(row) > 2:
                    raise csv.Error(f"Too many fields on row: {row}")

                setting_name = row[0].strip().lower()
                setting_value = row[1].strip()

                if not setting_name in config_settings:
                    continue

                setattr(cls, setting_name, setting_value)

    @classmethod
    def validate_config(cls):
        """Test if config files exist and create them if needed"""

        dir = pathlib.Path(cls.conf_dir)
        if not dir.is_dir():
            dir.mkdir(parents=True, exist_ok=True)

        files = [cls.conf_file]

        for file in files:
            f = pathlib.Path(file)

            if not f.is_file():
                f.touch()
