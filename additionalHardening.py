import source
import os
import re


#-------- 1.5.1 Ensure core dumps are restricted (Scored) ---------#

def check_core_dumps_restricted():

    config = '1.5.1 Ensure core dumps are restricted (Scored)'
    command1 = 'grep "hard core" /etc/security/limits.conf /etc/security/limits.d/*'
    command2 = 'sysctl fs.suid_dumpable'

    terminal_variable = os.popen(command1)
    terminal_output1 = terminal_variable.read()

    terminal_variable = os.popen(command2)
    terminal_output2 = terminal_variable.read()

    expected_output1 = re.compile(r'hard core 0')
    expected_output2 = re.compile(r'fs.suid_dumpable = 0')


    if (expected_output1.search(terminal_output1) and expected_output2.search(terminal_output2)):
        source.return_function(True,config)
    else:
        source.return_function(False,config)

#---------1.5.2 Ensure XD/NX support is enabled (Not Scored) --------#

def check_NX_XD_support_enabled():

    config = '1.5.2 Ensure XD/NX support is enabled (Not Scored)'
    command = 'dmesg | grep NX'
    output = 'NX (Execute Disable) protection: active'
    source.output_isIn_terminal_output(config,command,output)

# ---- 1.5.3 Ensure address space layout randomization (ASLR) is enabled ----#

def check_ASLR():
    config = '1.5.3 Ensure address space layout randomization (ASLR) is enabled '
    command = 'sysctl kernel.randomize_va_space'
    output = 'kernel.randomize_va_space = 2'
    source.output_isIn_terminal_output(config,command,output)

#----- 1.5.4 Ensure prelink is disabled (Scored) ---- #

def check_prelink_disabled():
    config = '1.5.4 Ensure prelink is disabled (Scored)'
    command = 'rpm -q prelink'
    output = 'package prelink is not installed'
    source.output_isIn_terminal_output(config,command,output)

#---#----------------------------------------------------------#