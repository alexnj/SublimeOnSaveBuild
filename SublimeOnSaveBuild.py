import sublime, sublime_plugin, re

class SublimeOnSaveBuild( sublime_plugin.EventListener ):
    def on_post_save( self, view ):
        settings = sublime.load_settings( "SublimeOnSaveBuild.sublime-settings" )
        if re.search( settings.get( "filename_filter" ), view.file_name() ):
            view.window().run_command( "build" )
