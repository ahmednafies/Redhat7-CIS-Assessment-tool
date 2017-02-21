import os

import source


#---------------------2.1 IN ETD SERVICES--------------------------------#
# ---------- 2.1.1 Ensure charge services are not enabled (Scored) ---- #

def check_charge_services_not_enabled():

    config = '2.1.1 Ensure chargen services are not enabled (Scored)'
    command = 'chkconfig --list'
    output1 = 'chargen-dgram:off'
    output2 = 'chargen-stream:off'

    print('checking "'+ config +'" ..... ')
    terminal_variable = os.popen(command)
    terminal_output = terminal_variable.read().replace(' ','')

    if output1 in terminal_output:
        if output2 in terminal_output:
           source.return_function(True, config)
        else:
            source.return_function(False, config)
    else:
        source.return_function(False, config)

#--------2.1.2 Ensure daytime services are not enabled (Scored) ---------#

def check_daytime_services_not_enabled():

    config = '2.1.1 Ensure daytime services are not enabled (Scored)'
    command = 'chkconfig --list'
    output1 = 'daytime-dgram:off'
    output2 = 'daytime-stream:off'

    print('checking "'+ config +'" ..... ')
    terminal_variable = os.popen(command)
    terminal_output = terminal_variable.read().replace(' ','')

    if output1 in terminal_output:
        if output2 in terminal_output:
           source.return_function(True, config)
        else:
            source.return_function(False, config)
    else:
        source.return_function(False, config)

#--------2.1.3 Ensure discard services are not enabled (Scored) ------#

def check_discard_services_not_enabled():

    config = '2.1.1 Ensure daytime services are not enabled (Scored)'
    command = 'chkconfig --list'
    output1 = 'daytime-dgram:off'
    output2 = 'daytime-stream:off'

    print('checking "'+ config +'" ..... ')
    terminal_variable = os.popen(command)
    terminal_output = terminal_variable.read().replace(' ','')

    if output1 in terminal_output:
        if output2 in terminal_output:
           source.return_function(True, config)
        else:
            source.return_function(False, config)
    else:
        source.return_function(False, config)
