# znp
znp stands for Zathura Next Or Previous. You can also use znp to add a given
file to an instance of [zathura](https://pwmt.org/projects/zathura/).

# Usage

## Next or Previous
The main goal of znp is to provide an easy way to go to the next or previous file from
within zathura. As of [yet](https://git.pwmt.org/pwmt/zathura/-/issues/93) this
functionality has not been added to zathura. However, after installing `znp` you can
add the following to your `zathurarc` to set `N` and `P` to go to the next or previous
file:

``` vim-snippet
map N exec "znp -n $FILE"
map P exec "znp -p $FILE"
```

*Note* that if your system does not use extended window manager hints
([ewmh](https://specifications.freedesktop.org/wm-spec/wm-spec-1.3.html)), or
you do not have the ewmh python package installed; then, this command may fail
if you  have two instances of zathura open in the same directory.  This is not
something that I have a reasonable fix for and there is no way to reliably
determine the instance issuing the next or previous command. The only way I can
think of fixing this would require patching zathura to include expansion of a
`$PID` variable from the exec function and include that in the zathurarc
command.  However, I am a not a programmer so reviewing the code base and
getting this functionality added may take me some time.

## Adding files
znp can act as a zathura wrapper and add a given file to an existing instance:

``` shell
znp file.pdf
znp /path/to/file.pdf
```

You can give znp a relative or absolute path to file. znp will insert the path
it was called from to the start of the file if needed. No variable expansion
will be done by znp as it expects `$HOME` and such to be expanded by the shell
calling it.

The above works best when only one instance of zathura exists. However, if
multiple exist then zathura will use the user defined `prompt_cmd` set in
`$XDG_CONFIG_HOME/znp/znp.conf` to present a list of zathura instances to open
the file in. You can use `fzf` is the default but you may use `dmenu` or `rofi`.
Here is how this looks in practice:

![fzf.png](media/fzf.png "fzf.png")

![dmenu.png](media/dmenu.png "dmenu.png")

To aviod any prompting you can pass the desired pid to use with the `-P` flag:

``` shell
znp -P 123456 file.pdf
znp -P 123456 /path/to/file.pdf
```

This would require a bit more work on your part but it may be useful in
scripting.

## Query
Speaking of scripting, I added the `-q, --query` flag for my personal scripting
purposes.

The `--query` flag will take the `FILE` argument given to znp and search all
zathura pids for the _first_ (see the note in the [next or previous](#Next or
Previous) section) one that has that file open and return it's pid. I make use
of this to track my last read pdf, epub, cbz/r, zip, etc. using the returned pid
to kill the assumed instance issuing the command. Basically a session tracker so
to speak. Maybe there are other purposes for this or maybe the `zathura.py`
module would be useful as a standalone module for interacting with zathura via
dbus. No clue, let me know.

# Installation
znp is available via [pypi](https://pypi.org/project/znp/) and can be installed via
pip the usual way:

``` shell
pip install znp
```

Use the following if you are installing on a system running X and using
[ewmh](https://specifications.freedesktop.org/wm-spec/wm-spec-1.3.html):

``` shell
pip install znp[x11]
```

Ensure `~/.local/bin` is in your `$PATH` otherwise znp will not be callable from
zathura unless the full path is given.

## Dependencies
1. `python-magic` is used to detect the file type of the next file to prevent
zathura from opening an unreadable file, e.g. log files, markdown files, etc.
2. `psutil` is used to get zathura pids.

## Optional Dependency
1. `ewmh` is used to get the pid of window calling znp. This is a bit hacky but
does allow for the core functionality (opening the next or previous file) to
work without issue. Provided under the `[x11]` branch.
