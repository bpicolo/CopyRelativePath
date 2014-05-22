import sublime, sublime_plugin

class CopyRelativePathCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if len(self.view.file_name()) > 0:
            sublime.set_clipboard( sublime.active_window().active_view().file_name().replace( sublime.active_window().folders()[0] + '/', '' ))
            sublime.status_message("Copied relative path")

    def is_enabled(self):
        return self.view.file_name() and len(self.view.file_name()) > 0
