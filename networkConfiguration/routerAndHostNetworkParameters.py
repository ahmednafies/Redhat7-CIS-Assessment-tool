import os
import source


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

    if output1 in terminal_output1 and output2 in termagic_function_twominal_output2:
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


# ----- 3.2.5 Ensure broadcast ICMP requests are ignored (Scored) ---- #

def check_broadCast_ICMP_request_ignored():
    config = '3.2.5 Ensure broadcast ICMP requests are ignored (Scored)'
    command = 'sysctl net.ipv4.icmp_echo_ignore_broadcasts'
    output = 'net.ipv4.icmp_echo_ignore_broadcasts = 1'
    source.output_isIn_terminal_output(config, command, output)


# --- 3.2.6 Ensure bogus ICMP responses are ignored (Scored) --- #

def check_bogus_icmp_requests_ignored():
    config = '3.2.6 Ensure bogus ICMP responses are ignored (Scored)'
    command = 'sysctl net.ipv4.icmp_ignore_bogus_error_responses'
    output = 'net.ipv4.icmp_ignore_bogus_error_responses = 1'
    source.output_isIn_terminal_output(config, command, output)


# --- 3.2.7 Ensure Reverse Path Filtering is enabled (Scored) ----#

def check_reverse_path_filtering_enabled():
    config = '3.2.7 Ensure Reverse Path Filtering is enabled (Scored)'

    command1 = 'sysctl net.ipv4.conf.all.rp_filter'
    output1 = 'net.ipv4.conf.all.rp_filter = 1'
    command2 = 'sysctl net.ipv4.conf.default.rp_filter'
    output2 = 'net.ipv4.conf.default.rp_filter = 1'

    print('checking "' + config + '" ..... ')

    terminal_variable = os.popen(command1)
    terminal_output1 = terminal_variable.read()

    terminal_variable = os.popen(command2)
    terminal_output2 = terminal_variable.read()

    if output1 in terminal_output1 and output2 in terminal_output2:
        source.return_function(True, config)
    else:
        source.return_function(False, config)


# --- 3.2.8 Ensure TCP SYN Cookies is enabled (Scored) --- #

def check_tcp_SYN_cookies_is_enabled():
    config = '3.2.8 Ensure TCP SYN Cookies is enabled (Scored)'
    command = 'sysctl net.ipv4.tcp_syncookies'
    output = 'net.ipv4.tcp_syncookies = 1'
    source.output_isIn_terminal_output(config, command, output)
