# I created this file based on the old "Send to Mocha" script
# Lurival Jones 2026 

import nuke
import subprocess
import os


def send_to_mocha():
    try:
        node = nuke.selectedNode()
        if node.Class() != "Read":
            nuke.message("Selecione um node Read.")
            return
    except:
        nuke.message("No nodes selected.")
        return

    # 1. Resolves the actual file path (essential for frame sequences)
    # nuke.filename(node, nuke.REPLACE) converts relative paths into absolute ones
    file_path = nuke.filename(node, nuke.REPLACE)
    file_path = os.path.normpath(file_path)  # Converts / to \ in Windows

    # 2. Node and Project Settings
    first = int(node.knob('first').value())
    last = int(node.knob('last').value())
    fps = nuke.root().knob('fps').value()
    aspect = nuke.root().knob('proxy_format').value().pixelAspect() if nuke.root().knob(
        'proxy').value() else nuke.root().knob('format').value().pixelAspect()

    # 3. Adjust your Mocha version according to the specific ".exe" file.
    mocha_path = "D:/BorisFX/Mocha Pro 2026/bin/mochapro.exe"

    if not os.path.exists(mocha_path):
        nuke.message("Mocha Pro not found in:\n" + mocha_path)
        return

    # 4. Metadata
    cmd = [
        mocha_path,
        "--frame-rate", str(fps),
        "--pixel-aspect", str(aspect),
        "--in", str(first),
        "--out", str(last),
        "--footage", file_path
    ]

    # Open Mocha as an independent process.
    subprocess.Popen(cmd)


# Adds to the Nuke toolbar (only if you want).
toolbar = nuke.menu("Nodes")
m = toolbar.addMenu("MochaTools", icon="mocha_icon.png")
m.addCommand("Send to Mocha", "send_to_mocha()", "shift+m")
