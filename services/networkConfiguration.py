import os
import source

# ----- NETWORK PARAMETERS -------#
#---- 3.1.1 Ensure IP forwarding is disabled (Scored) --- #
def check_ip_forwarding_is_disabled():
    config = '3.1.1 Ensure IP forwarding is disabled (Scored)'
    command = 'sysctl net.ipv4.ip_forward'
    output = 'net.ipv4.ip_forward = 0'
    source.output_isIn_terminal_output(config,command,output)

# --- 3.1.2 Ensure packet redirect sending is disabled (Scored) --- #

def check_packet_redirect_sending_is_disabled():
    config = '3.1.2 Ensure packet redirect sending is disabled (Scored)'

    command1 = 'sysctl net.ipv4.conf.all.send_redirects'
    output1 = 'net.ipv4.conf.all.send_redirects = 0'
    command2 = 'sysctl net.ipv4.conf.default.send_redirects'
    output2 = 'net.ipv4.conf.default.send_redirects = 0'

    print('checking "' + config + '" ..... ')

    terminal_variable = os.popen(command1)
    terminal_output1 = terminal_variable.read()

    terminal_variable = os.popen(command2)
    terminal_output2 = terminal_variable.read()

    if output1 in terminal_output1 and output2 in terminal_output2:
        source.return_function(True, config)
    else:
        source.return_function(False, config)
# ---- 3.2.1 Ensure source routed packets are not accepted (Scored) ---- #

def check_source_routed_packets_not_accepted():

    config = '3.2.1 Ensure source routed packets are not accepted (Scored)'

    command1 = 'sysctl net.ipv4.conf.all.accept_source_route'
    output1 = 'net.ipv4.conf.all.accept_source_route = 0'
    command2 = 'sysctl net.ipv4.conf.default.accept_source_route'
    output2 = 'net.ipv4.conf.default.accept_source_route = 0'

    print('checking "' + config + '" ..... ')

    terminal_variable = os.popen(command1)
    terminal_output1 = terminal_variable.read()

    terminal_variable = os.popen(command2)
    terminal_output2 = terminal_variable.read()

    if output1 in terminal_output1 and output2 in terminal_output2:
        source.return_function(True, config)
    else:
        source.return_function(False, config)

# ---- 3.2.2 Ensure ICMP redirects are not accepted (Scored) --- #


def check_ICMP_redirects_are_not_accepted():

    config = '3.2.2 Ensure ICMP redirects are not accepted (Scored)'

    command1 = 'sysctl net.ipv4.conf.all.accept_redirects'
    output1 = 'net.ipv4.conf.all.accept_redirects = 0'
    command2 = 'sysctl net.ipv4.conf.default.accept_redirects'
    output2 = 'net.ipv4.conf.default.accept_redirects = 0'

    print('checking "' + config + '" ..... ')

    terminal_variable = os.popen(command1)
    terminal_output1 = terminal_variable.read()

    terminal_variable = os.popen(command2)
    terminal_output2 = terminal_variable.read()

    if output1 in terminal_output1 and output2 in terminal_output2:
        source.return_function(True, config)
    else:
        source.return_function(False, config)

# ---- 3.2.3 Ensure secure ICMP redirects are not accepted (Scored) ---#

def check_secure_ICMP_redirect_are_not_accepted():
    config = '3.2.3 Ensure secure ICMP redirects are not accepted (Scored)'

    command1 = 'sysctl net.ipv4.conf.all.secure_redirects'
    output1 = 'net.ipv4.conf.all.secure_redirects = 0'
    command2 = 'sysctl net.ipv4.conf.default.secure_redirects'
    output2 = 'net.ipv4.conf.default.secure_redirects = 0'

    print('checking "' + config + '" ..... ')

    terminal_variable = os.popen(command1)
    terminal_output1 = terminal_variable.read()

    terminal_variable = os.popen(command2)
    terminal_output2 = terminal_variable.read()

    if output1 in terminal_output1 and output2 in terminal_output2:
        source.return_function(True, config)
    else:
        source.return_function(False, config)

# ---- 3.2.4 Ensure suspicious packets are logged (Scored) ---#

def check_suspicious_packets_are_logged():
    config = '3.2.4 Ensure suspicious packets are logged (Scored)'

    command1 = 'sysctl net.ipv4.conf.all.log_martians'
    output1 = 'net.ipv4.conf.all.log_martians = 1'
    command2 = 'sysctl net.ipv4.conf.default.log_martians'
    output2 = 'net.ipv4.conf.default.log_martians = 1'

    print('checking "' + config + '" ..... ')

    terminal_variable = os.popen(command1)
    terminal_output1 = terminal_variable.read()

    terminal_variable = os.popen(command2)
    terminal_output2 = terminal_variable.read()

    if output1 in terminal_output1 and output2 in terminal_output2:
        source.return_function(True, config)
    else:
        source.return_function(False, config)
