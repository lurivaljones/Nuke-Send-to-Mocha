# Nuke Send to Mocha 

![Gif](screenshots/send_to_mocha.gif)

A Python script for Foundry Nuke (including Nuke Indie) that allows digital compositors to send a Read node directly to Boris FX Mocha Pro Standalone.
This tool is especially useful for Nuke Indie users who might face limitations with the integrated OFX plugin and prefer a seamless way to open footage in Mocha Pro with project settings (range, FPS, aspect ratio) pre-configured.
* Inspired by the old version of the "Send to Mocha" script by Imagineer Systems (Boris FX now).

Features:

One-Click Export: Launch Mocha Pro with the selected footage.
Auto-Sync: Automatically sets Frame Range, FPS, and Pixel Aspect Ratio.
Indie Friendly: Works within Nuke Indie's Python restrictions.
Cross-Platform: Designed to work on Windows, but you can try it on macOS, and Linux.


Installation:

1. Download send_to_mocha.py and place it in your .nuke directory.
2. You can save the mocha_icon.png in the same directory.
3. Add the following lines to your menu.py:

import send_to_mocha
send_to_mocha.install_mocha_menu()

4. Or copy and paste the entire code inside the send_to_mocha.py into your menu.py file.


How to use:

1. Select a Read node in your Nuke node graph.
2. Click on the Send to Mocha menu or use the shortcut shift + M.
3. Mocha will open the "New Project" dialog pre-filled with your Nuke footage settings.

Configuration:

By default, the script looks for common installation paths for Mocha. If you use a different version, you can set an environment variable named MOCHA_PATH or edit the paths list in the script.


Contributing:

Feel free to submit Pull Requests or report issues. 
