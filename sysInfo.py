# Importing Needed Modules
import os
import platform
import socket
from termcolor import colored 

# Config >>
python_version_tuple = platform.python_version_tuple()
python_version = python_version_tuple[0]+'.'+python_version_tuple[1]+'.'+python_version_tuple[2]
uname = platform.uname()
current_user = uname[1]
system = uname[0]+' '+uname[2]
cpu = uname[5]
machine = uname[4]
IP = socket.gethostbyname(socket.gethostname())
# installing termcolor :(
os.system('pip install termcolor')

# Colored variables
systemColored = colored(system, 'cyan')
Ipcolored = colored(IP, 'cyan')
CuColored = colored(current_user, 'cyan')
CpuColored= colored(cpu, 'cyan')
machineColored = colored(machine, 'cyan')
python_colored = colored(python_version, 'cyan')


# Colored Variables to Print 
systemColoredT = colored('System >> ', 'green')
IpcoloredT = colored('IP >> ', 'green')
CuColoredT = colored('Current User >> ', 'green')
CpuColoredT= colored('CPU >> ', 'green')
machineColoredT = colored('Machine >> ', 'green')
python_coloredT = colored('python Version >> ', 'green')
print('\n',systemColoredT, systemColored,'\n', IpcoloredT, Ipcolored,'\n', CuColoredT, CuColored,'\n', 
CpuColoredT, CpuColored,'\n', machineColoredT, machineColored,'\n', python_coloredT, python_colored,'\n')
