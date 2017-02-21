import re
import source
import os

# ---------- 1.4.3 Ensure authentication required for single user mode (Not Scored) -------------#

def check_singleUserMode_authentication():

    config = '1.4.3 Ensure authentication required for single user mode (Not Scored)'
    command1 = 'grep /sbin/sulogin /usr/lib/systemd/system/rescue.service'
    command2 = 'grep /sbin/sulogin /usr/lib/systemd/system/emergency.service'

    terminal_variable = os.popen(command1)
    terminal_output1 = terminal_variable.read()

    terminal_variable = os.popen(command2)
    terminal_output2 = terminal_variable.read()

    expected_output = re.compile(r'ExecStart=-/bin/sh -c "/usr/sbin/sulogin; /usr/bin/systemctl --fail --no-block default')

    if (expected_output.search(terminal_output1) and expected_output.search(terminal_output2)):
        source.return_function(True,config)
    else:
        source.return_function(False,config)

