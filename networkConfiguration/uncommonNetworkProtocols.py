import os, source


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


# ---- 3.5.2 Ensure SCTP is disabled (Not Scored) -----#

def check_SCTP_is_disabled():
    config = '3.5.2 Ensure SCTP is disabled (Not Scored)'

    command1 = 'modprobe -n -v sctp'
    output1 = 'install /bin/true'
    command2 = 'lsmod | grep sctp'
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


# ---- 3.5.3 Ensure rds is disabled (Not Scored) -----#

def check_rds_is_disabled():
    config = '3.5.3 Ensure rds is disabled (Not Scored)'

    command1 = 'modprobe -n -v rds'
    output1 = 'install /bin/true'
    command2 = 'lsmod | grep rds'
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

# ---- 3.5.4 Ensure tipc is disabled (Not Scored) -----#

def check_tipc_is_disabled():
    config = '3.5.4 Ensure rds is disabled (Not Scored)'

    command1 = 'modprobe -n -v tipc'
    output1 = 'install /bin/true'
    command2 = 'lsmod | grep tipc'
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

# -------------------------------------------- #