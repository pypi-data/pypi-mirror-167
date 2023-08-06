#!/usr/bin/env python3
import csv
import os
import pathlib
import re
import sys
from argparse import ArgumentParser
from shlex import split
from typing import Optional, Iterable


class UserSettings:
    """
    Easily enable users to personalize your program to their liking.
    Arguments:
        program[str]:
            The name of your program. This is used to define where user
            config files will be stored, e.g. $XDG_CONIG_HOME/program/.

        cmd_line_args(Optional[ArgumentParser]):
            Takes an ArgumentParser object and stores those values under
            user.cmd_args. If you use argparse it makes it easy to store
            that object within this one. One less thing to juggle.

        user_files(Optional[dict]):
            This should be a dict of the user files you want created (if
            needed). So if the user_files dict looks like this:
                {"conf_file": "my_program.conf"}
            Then my_program.conf will be created in the defined config dir
            for your program (see defined variables). You will also be able
            to access this value latter:
                >>> user = UserSettings(my_program, user_files=user_files)
                >>> user.conf_file
                '/home/user/.config/program/my_program.conf'

        create_files(Optional[bool]):
            If you don't want UserSettings to create the files in user_files
            then set this to false. The default value is True.

        default_settings(Option[dict]):
            This should be a dict with settings that a user may define or that
            you may find useful along with their default settings if a user
            were not to define them.
                >>> settings = {"favorite_color": "blue"}
                >>> user = UserSettings("my_program", default_settings=settings)
                >>> user.favorite_color
                'blue'

        read_files(Op[list]):
            If user_files was given then read_files can be a list of the keys
            whose file values you want parsed for user settings. So if my
            user_files looks like this: {"conf_file": "my_program.conf"}
            then I can pass read_files with this value: ["conf_file"]
            UserSettings will then parse that file. Speaking of parsing, let's
            talk about that.

    Parsing files:
        UserSettings can parse any user_file to update the UserSettings objects
        user_settings values. This is done by a simple csv parser. As users
        usually work with conf files and not csv files (in the context of user
        configurable cli programs) the default deliminator is the equal sign,
        "=". This is because it is clean and commonly found in conf files. It is
        probably simplest if I give an example. Take this file for instance:

            # my_program.conf
            # setting \= value
            fav_color = blue
            fav_bool = true
            fav_int = 5
            fav_sentence = my sentence without an equal sign
            other_sentence = my sentence with an escapped \= sign

        If a value in the first column was defined as a key in default_settings
        the value will be updated after parsing the desired file. Additionally
        UserSettings will make an attempt to detect any int or bool values. In
        the above example both fav_int and fav_bool will actually be an int and
        bool value respectively. Any value that does not evaluate to an int or
        bool will be treated as a string. UserSettings allows for escaped
        delimiters. If two unescapped delimiters are found in a line an error
        will be raised with the value of the line where the error was
        encountered. The white space/newlines are stripped from both columns.
        If a setting is not listed in default_settings then UserSettings ignores
        the setting and it's value.
    """

    def __init__(
        self,
        program: str,
        delimiter: Optional[str] = "=",
        cmd_line_args: Optional[ArgumentParser] = None,
        user_files: Optional[dict] = {},
        create_files: Optional[bool] = True,
        default_settings: Optional[dict] = {},
        read_files: Optional[list] = [],
    ):
        self.cmd_args = cmd_line_args
        self._user_files = user_files
        self._define_files(program=program, user_files=user_files)
        self._assert_files(create_files=create_files)
        self._set_default_settings(default_settings=default_settings)
        self._read_user_settings(
            user_settings=default_settings.keys(),
            read_files=read_files,
            delimiter=delimiter,
        )

    def _assert_files(self, create_files):
        """
        Test if config files exist and create them if needed
        """
        dir = pathlib.Path(self._conf_dir)
        if not dir.is_dir():
            dir.mkdir(parents=True, exist_ok=True)
        if not create_files:
            return
        for file in self._files:
            f = pathlib.Path(file)
            if not f.is_file():
                f.touch()

    def _define_files(self, program, user_files):
        """
        Set user config directory location and where user files should be
        located
        """
        path = os.getenv("XDG_CONFIG_HOME", os.path.expanduser("~/.config"))
        self._conf_dir = os.path.join(path, program)
        self._files = []
        for key, value in user_files.items():
            file = os.path.join(self._conf_dir, value)
            self._files.append(file)
            self._user_files[key] = file
            setattr(self, key, file)

    def _read_user_settings(
        self,
        user_settings,
        read_files=None,
        delimiter="=",
    ):
        """
        Read the desired files and set setting values from parsed file.
        """
        # read_files should be a list of the key value(s) from the user_files
        # dict to read
        files = []
        for key, file in self._user_files.items():
            if key in read_files:
                files.append(file)
        # Regex object for
        r = re.compile(rf"\\{delimiter}")
        # Read the desired files
        for file in files:
            test_file = pathlib.Path(file)
            if not test_file.is_file():
                continue
            with open(file) as f:
                reader = csv.reader(
                    f,
                    delimiter=delimiter,
                    escapechar="\\",
                    quoting=csv.QUOTE_NONE,
                )
                for row in reader:
                    if len(row) > 2:
                        raise csv.Error(f"Too many fields on row: {row}")
                    elif len(row) < 2:
                        continue
                    setting_name = row[0].strip()
                    setting_name = r.sub("=", setting_name)
                    setting_value = row[1].strip()
                    setting_value = r.sub("=", setting_value)
                    try:
                        setting_value = eval(setting_value.capitalize())
                    except (NameError, SyntaxError):
                        pass
                    if not setting_name in user_settings:
                        continue
                    setattr(self, setting_name, setting_value)

    def _set_default_settings(self, default_settings):
        """
        Set default values for settings that user might not provide
        """
        for key, value in default_settings.items():
            setattr(self, key, value)


if __name__ == "__main__":
    __program__ = "znp"
    user_files = {
        "conf_file": f"{__program__}.conf",
        "log": f"{__program__}.log",
    }
    user_settings = ["prompt_cmd", "args"]
    read_files = ["conf_file"]
    default_settings = {
        "prompt_cmd": "fzf",
        "args": "",
    }
    user = UserSettings(
        program=__program__,
        user_files=user_files,
        default_settings=default_settings,
        read_files=read_files,
    )
