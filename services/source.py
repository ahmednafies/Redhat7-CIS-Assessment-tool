import subprocess
import os
#######---- example functions -----#######

def example_complicated():
    cmdping = "ping -c4 www.google.biz"
    p = subprocess.Popen(cmdping, shell=True, stderr=subprocess.PIPE)
    while True:
        out = p.stderr.read(1)
        if out == '' and p.poll() != None:
            break
        if out != '':
            sys.stdout.write(out)
            sys.stdout.flush()

def example_simple():
    p = subprocess.Popen(["ping", "-c", "10", "www.cyberciti.biz"], stdout=subprocess.PIPE)
    output, err = p.communicate()
    print(output)

# the following example is not recommended

def example_not_recommended():
    f = os.popen('date')
    now = f.read()
    print "Today is ", now


def return_function(result,config):

    if (result == True):
        print (config)
        print('test was successful ... ')
        print('-----------------------------------------------------')
        return True
    else:
        print("Your system has NOT been configured correctly")
        print('WARNING: please check the benchmark "'+config+'" ')
        print('-----------------------------------------------------')
        return False


# ------- main source function ------- #

def magic_function_one(config,command):
    print('checking "'+ config +'" ..... ')
    terminal_variable = os.popen(command)
    grep_output = terminal_variable.read()

    if (grep_output == ''):
        print("Your system has NOT been configured correctly")
        print('WARNING: please check the benchmark "'+config+'" ')
    else:
        print('test was successful ... ')
        print(grep_output)


    print('-----------------------------------------------------')


#----- main source function 2 ----#
def magic_function_two(config,cmd_1,cmd_2):
    print('checking "'+ config +'" ..... ')
    terminal_variable = os.popen(cmd_1)
    grep_output = terminal_variable.read()
    terminal_variable = os.popen(cmd_2)
    mount_output = terminal_variable.read()
    if (grep_output == '' or mount_output == ''):
        print("Your system has NOT been configured correctly")
        print('WARNING: please check the benchmark "'+config+'" ')
    else:
        print('test was successful ... ')
        print(grep_output)
        print(mount_output)

    print('-----------------------------------------------------')

def check_separate_partition_exits(config,command,output):
    print('checking "'+ config +'" ..... ')
    terminal_variable = os.popen(command)
    terminal_output = terminal_variable.read()

    if (int(terminal_output) == int(output)):
        print('test was successful ... ')
        print(terminal_output)
    else:
        print("Your system has NOT been configured correctly")
        print('WARNING: please check the benchmark "'+config+'" ')



    print('-----------------------------------------------------')

def check_options_function(config,cmd,option):
    print('checking "' + config + '" ..... ')
    terminal_variable = os.popen(cmd)
    terminal_output = terminal_variable.read()

    directory_options = terminal_output.split(',')

    if option in directory_options:
        print ('success')
    else:
        print ('WARNING: please check the benchmark "'+config+'" ')


    print('-----------------------------------------------------')


def output_isEqualTo_terminal_output(config,command,output):
    print('checking "'+ config +'" ..... ')
    terminal_variable = os.popen(command)
    terminal_output = terminal_variable.read()

    if (terminal_output == output):
        print('test was successful ... ')
    else:
        print("Your system has NOT been configured correctly")
        print('WARNING: please check the benchmark "'+config+'" ')


    print('-----------------------------------------------------')

def output_isIn_terminal_output(config,command,output):
    print('checking "'+ config +'" ..... ')
    terminal_variable = os.popen(command)
    terminal_output = terminal_variable.read()

    if output in terminal_output:
        print('test was successful ... ')
        print('-----------------------------------------------------')

        return True
    else:
        print("Your system has NOT been configured correctly")
        print('WARNING: please check the benchmark "'+config+'" ')
        print('-----------------------------------------------------')
        return False


def output_isIn_terminal_output_inverse(config,command,output):
    print('checking "'+ config +'" ..... ')
    terminal_variable = os.popen(command)
    terminal_output = terminal_variable.read()

    if output in terminal_output:
        print("Your system has NOT been configured correctly")
        print('WARNING: please check the benchmark "'+config+'" ')
        print('-----------------------------------------------------')
        return True
    else:
        print('test was successful ... ')
        print('-----------------------------------------------------')
        return False