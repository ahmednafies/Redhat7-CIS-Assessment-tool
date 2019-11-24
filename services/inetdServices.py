import os

import source


# ---------------------2.1 IN ETD SERVICES--------------------------------#
# ---------- 2.1.1 Ensure charge services are not enabled (Scored) ---- #

def check_charge_services_not_enabled():
    config = '2.1.1 Ensure chargen services are not enabled (Scored)'
    command = 'chkconfig --list'
    output1 = 'chargen-dgram:off'
    output2 = 'chargen-stream:off'

    print('checking "' + config + '" ..... ')
    terminal_variable = os.popen(command)
    terminal_output = terminal_variable.read().replace(' ', '')

    if output1 in terminal_output:
        if output2 in terminal_output:
            source.return_function(True, config)
        else:
            source.return_function(False, config)
    else:
        source.return_function(False, config)


# --------2.1.2 Ensure daytime services are not enabled (Scored) ---------#

def check_daytime_services_not_enabled():
    config = '2.1.1 Ensure daytime services are not enabled (Scored)'
    command = 'chkconfig --list'
    output1 = 'daytime-dgram:off'
    output2 = 'daytime-stream:off'

    print('checking "' + config + '" ..... ')
    terminal_variable = os.popen(command)
    terminal_output = terminal_variable.read().replace(' ', '')

    if output1 in terminal_output:
        if output2 in terminal_output:
            source.return_function(True, config)
        else:
            source.return_function(False, config)
    else:
        source.return_function(False, config)


# --------2.1.3 Ensure discard services are not enabled (Scored) ------#

def check_discard_services_not_enabled():
    config = '2.1.1 Ensure daytime services are not enabled (Scored)'
    command = 'chkconfig --list'
    output1 = 'daytime-dgram:off'
    output2 = 'daytime-stream:off'

    print('checking "' + config + '" ..... ')
    terminal_variable = os.popen(command)
    terminal_output = terminal_variable.read().replace(' ', '')

    if output1 in terminal_output:
        if output2 in terminal_output:
            source.return_function(True, config)
        else:
            source.return_function(False, config)
    else:
        source.return_function(False, config)


# ----------2.1.4 Ensure echo services are not enabled (Scored)---------#

def check_echo_services_not_enabled():
    config = '2.1.4 Ensure echo services are not enabled (Scored)'
    command = 'chkconfig --list'
    output1 = 'echo-dgram:off'
    output2 = 'echo-stream:off'

    print('checking "' + config + '" ..... ')
    terminal_variable = os.popen(command)
    terminal_output = terminal_variable.read().replace(' ', '')

    if output1 in terminal_output:
        if output2 in terminal_output:
            source.return_function(True, config)
        else:
            source.return_function(False, config)
    else:
        source.return_function(False, config)


# --------2.1.4 Ensure time services are not enabled (Scored)-----#


def check_time_services_not_enabled():
    config = '2.1.4 Ensure time services are not enabled (Scored)'
    command = 'chkconfig --list'
    output1 = 'time-dgram:off'
    output2 = 'time-stream:off'

    print('checking "' + config + '" ..... ')
    terminal_variable = os.popen(command)
    terminal_output = terminal_variable.read().replace(' ', '')

    if output1 in terminal_output:
        if output2 in terminal_output:
            source.return_function(True, config)
        else:
            source.return_function(False, config)
    else:
        source.return_function(False, config)


# ----- 2.1.6 Ensure tftp server is not enabled (Scored) ----#

def check_tftp_server_not_enabled():
    config = '2.1.4 Ensure tftp server are not enabled (Scored)'
    command = 'chkconfig --list'
    output1 = 'tftp::off'

    print('checking "' + config + '" ..... ')
    terminal_variable = os.popen(command)
    terminal_output = terminal_variable.read().replace(' ', '')

    if output1 in terminal_output:
        source.return_function(True, config)
    else:
        source.return_function(False, config)


# ----- 2.1.7 Ensure xinetd is not enabled (Scored) ------#

def check_xinetd_not_enabled():
    config = '2.1.7 Ensure xinetd is not enabled (Scored)'
    command = 'systemctl is-enabled xinetd'
    output = 'disabled'
    source.output_isIn_terminal_output(config, command, output)

    # ---------------------------------------------------------#
