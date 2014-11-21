import sublime, sublime_plugin
from os.path import commonprefix, relpath

class CopyRelativePathCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filename = self.view.file_name()
        if len(filename) > 0:
            if self.view.settings().get('copy_relpath_with_common_prefix_root', False):
                # Copy the relpath to the common-prefix of open folders
                sublime.set_clipboard(
                    relpath(filename, commonprefix(self.view.window().folders()))
                )
            else:
                # Copy shortest relpath for file compared to open folders
                sublime.set_clipboard(
                    min(
                        (
                            relpath(filename, folder)
                            for folder in sublime.active_window().folders()
                        ),
                        key=len,
                    )
                )

            sublime.status_message("Copied relative path")

    def is_enabled(self):
        return bool(self.view.file_name() and len(self.view.file_name()) > 0)
