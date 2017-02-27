import os,source


# --- 3.3.1 Ensure IPv6 router advertisements are not accepted (Scored) --- #

def check_IPv6_router_ads_not_accepted():
    config = '3.3.1 Ensure IPv6 router advertisements are not accepted (Scored)'

    command1 = 'sysctl net.ipv6.conf.all.accept_ra'
    output1 = 'net.ipv6.conf.all.accept_ra = 0'
    command2 = 'sysctl net.ipv6.conf.default.accept_ra'
    output2 = 'net.ipv6.conf.default.accept_ra = 0'

    print('checking "' + config + '" ..... ')

    terminal_variable = os.popen(command1)
    terminal_output1 = terminal_variable.read()

    terminal_variable = os.popen(command2)
    terminal_output2 = terminal_variable.read()

    if output1 in terminal_output1 and output2 in terminal_output2:
        source.return_function(True, config)
    else:
        source.return_function(False, config)


# ---- 3.3.2 Ensure IPv6 redirects are not accepted (Scored) ---#

def check_IPv6_redirect_not_accepted():
    config = '3.3.2 Ensure IPv6 redirects are not accepted (Scored)'

    command1 = 'sysctl net.ipv6.conf.all.accept_redirects'
    output1 = 'net.ipv6.conf.all.accept_redirect = 0'
    command2 = 'sysctl net.ipv6.conf.default.accept_redirects'
    output2 = 'net.ipv6.conf.default.accept_redirect = 0'

    print('checking "' + config + '" ..... ')

    terminal_variable = os.popen(command1)
    terminal_output1 = terminal_variable.read()

    terminal_variable = os.popen(command2)
    terminal_output2 = terminal_variable.read()

    if output1 in terminal_output1 and output2 in terminal_output2:
        source.return_function(True, config)
    else:
        source.return_function(False, config)


# ---- 3.3.3 Ensure IPv6 is disabled (Not Scored) --- #

def check_IPv6_is_disabled():
    config = '3.3.3 Ensure IPv6 is disabled (Not Scored)'
    command = 'modprobe -c | grep ipv6'
    output = 'options ipv6 disable=1'
    source.output_isIn_terminal_output(config, command, output)

