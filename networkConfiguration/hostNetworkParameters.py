import os
import source


# ----- NETWORK PARAMETERS -------#
# ---- 3.1.1 Ensure IP forwarding is disabled (Scored) --- #
def check_ip_forwarding_is_disabled():
    config = '3.1.1 Ensure IP forwarding is disabled (Scored)'
    command = 'sysctl net.ipv4.ip_forward'
    output = 'net.ipv4.ip_forward = 0'
    source.output_isIn_terminal_output(config, command, output)


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

