import sublime, sublime_plugin

class SublimeOnSaveBuild( sublime_plugin.EventListener ):
    def onPostSave( self, view ):
        if view.window().canRunCommand( "build" ):
            view.window().run_command( "build" )
