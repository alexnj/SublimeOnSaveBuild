SublimeOnSaveBuild Sublime Plugin
=================================

This is a simple plugin for [Sublime Text 2](http://www.sublimetext.com/2) to trigger a build on each save.

Not all projects might need this plugin, especially if the build operation is lengthy. However, if you have a build that does things like pre-processing CSS via tools like [LessCSS](http://lesscss.org) and stitching all JS files together, this might be very handy.

Installation
------------
**With the Package Control plugin:** The easiest way to install SublimeOnSaveBuild is through Package Control, which can be found at this site: http://wbond.net/sublime_packages/package_control

Once you install Package Control, restart ST2 and bring up the Command Palette (`Command+Shift+P` on OS X, `Control+Shift+P` on Linux/Windows). Select "Package Control: Install Package", wait while Package Control fetches the latest package list, then select SublimeOnSaveBuild when the list appears. The advantage of using this method is that Package Control will automatically keep SublimeOnSaveBuild up to date with the latest version.

**Without Git:** Download the latest source from [GitHub](http://github.com/alexnj/SublimeOnSaveBuild) and copy the SublimeOnSaveBuild folder to your Sublime Text 2 "Packages" directory.

**With Git:** Clone the repository in your Sublime Text 2 "Packages" directory:

    git clone git://github.com/alexnj/SublimeOnSaveBuild.git


The "Packages" directory is located at:

* OS X:

        ~/Library/Application Support/Sublime Text 2/Packages/

* Linux:

        ~/.config/sublime-text-2/Packages/

* Windows:

        %APPDATA%/Sublime Text 2/Packages/

Configuring
-----------
There are a number of configuration options available to customize the behavior of SublimeOnSaveBuild. For the latest information on what options are available, select the menu item `Preferences->Package Settings->SublimeOnSaveBuild->Settings - Default`.

Do NOT edit the default SublimeOnSaveBuild settings. Your changes will be lost when SublimeOnSaveBuild is updated. ALWAYS edit the user SublimeOnSaveBuild settings by selecting `Preferences->Package Settings->SublimeOnSaveBuild->Settings - User`. 

* **build_on_save**
Set to `1` to trigger a build on save. By default, this is set to `1`. I.e., SublimeOnSaveBuild attempts to build all projects. You can change this behavior and build only specific projects by configuring the user specific setting of `build_on_save` to `0` and project specific setting to `1`.

* **filename_filter**
SublimeOnSaveBuild matches the name of the file being saved against this regular expression to determine if a build should be triggered. By default, the setting has a value of `"\\.(css|js|sass|less|scss)$"`.

Usage
-----
1. Make sure you have a build operation set up in your Sublime Text 2 project and you are able to build using `Control+B` (Linux/Windows) or `Command+B` (OS X).
2. Hit your favorite shortcut to Saveit should trigger a build.

*Good luck!*