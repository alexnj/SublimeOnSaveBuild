import sublime
import sublime_plugin
import re


class SublimeOnSaveBuild(sublime_plugin.EventListener):
    def on_post_save(self, view):
        global_settings = sublime.load_settings(__name__ + '.sublime-settings')

        # See if we should build. A project level build_on_save setting
        # takes precedence. To be backward compatible, we assume the global
        # build_on_save to be true if not defined.
        should_build = view.settings().get('build_on_save', global_settings.get('build_on_save', True))

        # Load filename filter. Again, a project level setting takes precedence.
        filename_filter = view.settings().get('filename_filter', global_settings.get('filename_filter', '*'))

        if not should_build:
            return

        if not re.search(filename_filter, view.file_name()):
            return

        view.window().run_command('build')
