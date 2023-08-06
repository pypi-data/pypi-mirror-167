# znp
znp stands for Zathura Next Or Previous. You can also use znp to add a given
file to an instance of [zathura](https://pwmt.org/projects/zathura/).

## Next or Previous
The main goal of znp is to provide an easy way to go to the next or previous file from
within zathura. As of [yet](https://git.pwmt.org/pwmt/zathura/-/issues/93) this
functionality has not been added to zathura. However, after installing `znp` you can
add the following to your `zathurarc` to set `N` and `P` to go to the next or previous
file:

``` vim-snippet
map N exec znp -n $FILE
map P exec znp -p $FILE
```
<!-- Okay so scrap ewmh and instead get a list of zathura pids -->
<!-- Then run exec echo $FILE from dbus -->
<!-- check the out put and compare that with the given file  -->
<!-- this would only work for next_or_prev -->

## Some notes
2. zathura does not have a `$PID` variable like the `$FILE` expansion. Because of this
you will need to give `znp` the `$PID` value when adding a file to an instance of zathura.
See [TODO](#TODO) for ideas on getting around this.
