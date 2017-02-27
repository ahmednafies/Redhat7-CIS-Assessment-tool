import os
import re

import source


# function runs yum check-update commands and returns what the command line shows


# ----- 1.2.1 Ensure package manager repositories are configured (Not Scored) -----#

# ------------- 1.2.2 Ensure gpgcheck is globally activated (Scored) --------------#


def gpg_globally_activated_yum_conf(command):
    terminal_variable = os.popen(command)
    grep_output = terminal_variable.read()

    regexp = re.compile(r'gpgcheck=1')

    if regexp.search(grep_output):
        return True
    else:

        return False


def gpg_globally_activated_yum_repos(command):
    terminal_variable = os.popen(command)
    grep_output = terminal_variable.read()

    string_array = grep_output.split('\n')

    regexp = re.compile(r'gpgcheck=1')

    for string in string_array:

        if regexp.search(string) == False:
            return False
        else:
            return True


def gpg_globally_activated():
    config = '1.2.2 Ensure gpgcheck is globally activated (Scored)'
    conf_command = 'grep ^gpgcheck /etc/yum.conf'
    repos_command = 'grep ^gpgcheck /etc/yum.repos.d/*'

    print('checking "' + config + '" ..... ')

    yum_conf = gpg_globally_activated_yum_conf(conf_command)
    yum_repos = gpg_globally_activated_yum_repos(repos_command)

    if (yum_conf != True or yum_repos != True):

        source.return_function(False, config)
    else:
        source.return_function(True, config)


# -------------1.2.5 Disable the rhnsd Daemon (Not Scored)-------#

def check_rhnsd_daemon_disabled():
    config = '1.2.5 Disable the rhnsd Daemon (Not Scored)'
    command = 'chkconfig --list rhnsd'

    print('checking "' + config + '" ..... ')

    word = re.compile(r'on')
    error = re.compile(r'error')

    terminal_variable = os.popen(command)
    grep_output = terminal_variable.read()

    if (word.search(grep_output) == True or error.search(grep_output) == True):
        source.return_function(False, config)
    else:
        source.return_function(True, config)
        # --------------------------------------------------------------------#
