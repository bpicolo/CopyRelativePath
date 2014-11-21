# Copy Relative Path
Adds a "Copy Relative Path" command to the Sublime right-click context menu,
which copies the file path of the currently opened file relative
to the folder you have open with the greatest path match.

## Adding a Hotkey
     {"keys": ["super+i"], "command": "copy_relative_path"},

## Relative to "Project Root" Option
Setting the option `copy_relpath_with_common_prefix_root` will instead copy
the path relative to the common prefix of opened folders.

This could be useful if you use a project that includes various folders under
a single project root eg "app", "tests", "scripts" etc, and want copied paths
to be relative to the project root eg `app/foo/bar.txt` (instead of `foo/bar.txt`).
