import os,source

# -- 3.5.1 Ensure DCCP is disabled (Not Scored) --- #

def check_DCCP_is_disabled():

    config = '3.5.1 Ensure DCCP is disabled (Not Scored)'

    command1 = 'modprobe -n -v dccp'
    output1 = 'install /bin/true'
    command2 = 'lsmod | grep dccp'
    output2 = ''

    print('checking "' + config + '" ..... ')

    terminal_variable = os.popen(command1)
    terminal_output1 = terminal_variable.read()

    terminal_variable = os.popen(command2)
    terminal_output2 = terminal_variable.read()

    if output1 in terminal_output1 and output2 == terminal_output2:
        source.return_function(True, config)
    else:
        source.return_function(False, config)