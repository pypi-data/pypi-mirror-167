#!/usr/bin/env python3
import re
import shlex
import subprocess
from typing import Optional, Iterable


class PromptXError(Exception):
    """
    Raised if OS error when trying to execute constructed prompt command
    or if prompt command returns non-zero value and stderr is not empty.
    """

    def __init__(self, cmd, err):
        self.cmd = cmd
        self.err = err
        self.message = (
            f"Failed to execute constructed command: {self.cmd}\nError: {self.err}"
        )
        super().__init__(self.message)


class PromptXCmdError(Exception):
    """
    Raised if PromptX is given a prompt command that is not fzf, dmenu, or rofi.
    """

    def __init__(self, prompt):
        self.prompt = prompt
        self.message = (
            f"PromptX does not yet handle the given prompt command: {self.prompt}"
        )
        super().__init__(self.message)


class PromptXSelectError(Exception):
    """
    Raised if select value is not "first", "last", or "all"
    """

    def __init__(self, select):
        self.select = select
        self.message = f"Invalid select option given: {self.select}"
        self.message = "\n".join(
            [self.message, 'Valid options are "first", "last", and "all"']
        )
        super().__init__(self.message)


class PromptX:
    """
    Prompt object that makes using dmenu, fzf, or rofi as easy as using
    it from the command line. To initialize the object give the desired
    prompt command you want to use along with any default args to pass.
    No need to pass a '--prompt=' or '-p' flag as this will be added if
    you give a prompt value when using the ask() method. Any other arg
    must be given explicitly in the form of a string. It will be properly
    split for you. Some example usage:

        >>> p = PromptX(prompt_cmd="dmenu", default_args="-l 20 -i")
        >>> choices = [ "1", "2", "3" ]
        >>> response = p.ask(choices)
        >>> print(response)
        '1'
        >>> response = p.ask(choices, prompt="Pick a number:", select="all")
        >>> print(response)
        ['1', '3']

    One nice thing about PromptX is you can configure it once and use it as
    many times as needed. If you need any additional arguments for a specific
    prompt the ask() method happily accepts them while not altering the PromptX
    object.

    Arguments for PromptX():
        prompt_cmd(str):
            The prompt command to use. PromptX can handle dmenu, fzf, and
            rofi. A note on rofi, it requires the '-dmenu' flag to read from
            stdin. PromptX will add this for you.

        default_args(Optional[str]): Default = ""
            This is a string of args like you would pass at the command line.
            PromptX will parse these for you using shlex. If you want to use
            an Iterable to add arguments use the add_args() method which takes
            an Iterable object.

    Arguments for ask() method:
        options(Iterable):
            A list of options to present the user with.

        prompt(Optional[str]):
            The prompt to use when querying the user.  The necassary flag
            will be added automatically to based on the prompt_cmd given on
            initilization.

        additional_args(Optional[str]):
            Add additional arguments to the prompt command.  Any additional
            arguments will be added before the prompt flag. These arguments
            must be a string. They will be appropriately split, just provide
            them as you would from the command line.

        select(Optional[str]):
            User's may select multiple answers in any of the three supported
            prompt_cmds. So you don't have to guess the return type of ask()
            you can indicate which user selection you want ask() to return:
            "first": Default
                Use "first" if you want the first option the user selected.
                Returns a string.
            "last":
                Use "last" if you want the last option the user selected.
                Returns a string.
            "all":
                Use "all" if you want all options the user selected.
                Returns a list of all selected options.

        deliminator(Optional[str]):
            Default is "\n". This is the deliminator to use when joining your
            list of options.

    Arguments for add_args() method:
        additional_args(Iterable):
            This method will add these args to the base_cmd of the PromptX
            object.
    """

    def __init__(
        self,
        prompt_cmd: str,
        default_args: Optional[str] = "",
    ):
        # Check that we can handle the given command
        valid_prompt_cmds = ["dmenu", "fzf", "rofi"]
        if not prompt_cmd in valid_prompt_cmds:
            raise PromptXCmdError(prompt=prompt_cmd)
        # As PromptX works through stdin rofi needs the -dmenu flag to work
        if prompt_cmd == "rofi":
            default_args = " ".join((default_args, "-dmenu"))
        self.prompt_cmd = prompt_cmd
        self.default_args = default_args
        # Create a basic list of command args
        self.base_cmd = shlex.split(" ".join((prompt_cmd, default_args)))

    def ask(
        self,
        options: Iterable,
        prompt: Optional[str] = None,
        additional_args: Optional[str] = None,
        select: Optional[str] = "first",
        deliminator: Optional[str] = "\n",
    ):
        """
        Ask the user to make a selection from the given options

        Arguments:
            options(Iterable):
                A list of options to present the user with.

            prompt(Optional[str]):
                The prompt to use when querying the user.  The necassary flag
                will be added automatically to based on the prompt_cmd given on
                initilization.

            additional_args(Optional[str]):
                Add additional arguments to the prompt command.  Any additional
                arguments will be added before the prompt flag. These arguments
                must be a string. They will be appropriately split, just provide
                them as you would from the command line.

            select(Optional[str]):
                User's may select multiple answers in any of the three supported
                prompt_cmds. So you don't have to guess the return type of ask()
                you can indicate which user selection you want ask() to return:
                "first": Default
                    Use "first" if you want the first option the user selected.
                    Returns a string.
                "last":
                    Use "last" if you want the last option the user selected.
                    Returns a string.
                "all":
                    Use "all" if you want all options the user selected.
                    Returns a list of all selected options.

            deliminator(Optional[str]):
                Default is "\n". This is the deliminator to use when joining your
                list of options.
        """
        # If check that select is properly set
        if select not in ["first", "last", "all"]:
            raise PromptXSelectError(select)
        # Initialize the cmd value
        cmd = self.base_cmd
        # fzf uses stderr to show prompt so we need to check for that
        stderr_file = None if self.prompt_cmd == "fzf" else subprocess.PIPE
        if additional_args is not None:
            cmd.extend(shlex.split(additional_args))
        if self.prompt_cmd == "fzf" and prompt is not None:
            cmd.append(f"--prompt={prompt}")
        elif prompt is not None:
            cmd.extend(["-p", prompt])

        # Start prompt_cmd with given args
        try:
            prompt = subprocess.Popen(
                cmd,
                universal_newlines=True,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=stderr_file,
            )
        # Failed to execute constructed command
        except OSError as err:
            raise PromptXError(cmd=cmd, err=err)

        # Create one long string similar to choice=$(printf '%s\n' "$@" | dmenu) in bash
        opts_str = deliminator.join(map(str, options))
        # Open stdin and populate choices
        with prompt.stdin:
            prompt.stdin.write(opts_str)

        # Wait for selection
        if prompt.wait() == 0:
            # Process user selection
            selection = prompt.stdout.read().rstrip().splitlines()
            # Return the requested selection
            if select == "first":
                return selection[0]
            elif select == "last":
                return selection[-1]
            else:
                return selection

        # fzf has no error to read, return None
        if stderr_file == None:
            return None
        # dmenu does print to stderr so we read it and return None
        # unless an actual error was encountered
        stderr = prompt.stderr.read()
        # If no err return None as user hit escape
        if stderr == "":
            return None
        # Otherwise some error occured
        raise PromptXError(cmd, stderr)

    def add_args(self, additional_args: Iterable):
        """
        Add additional args to the base_cmd value of the PromptX object. Does
        not overwrite what was given when when PromptX was initialized.
        """
        for arg in additional_args:
            self.base_cmd.extend(shlex.split(arg))
