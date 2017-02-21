import re
import source
import os

# ---------- 1.3.1 Ensure AIDE is installed (Scored) -------------#

def check_aide_installed():

    config = ' 1.3.1 Ensure AIDE is installed (Scored)'
    command = 'rpm -q aide'

    terminal_variable = os.popen(command)
    terminal_output = terminal_variable.read()

    word = re.compile(r'not installed')

    if (word.search(terminal_output)):
        source.return_function(False,config)
    else:
        source.return_function(True,config)


