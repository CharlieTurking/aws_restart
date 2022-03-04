"""
Your module description
"""
import os
import subprocess
print("os.system doing the work \n")
os.system("ls")
print("subprocess doing the work \n")
subprocess.run(["ls", "-all"])
subprocess.run(["ls","-l","README.md"])

##
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
##
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
##

def runThis(iCommand, iCommandArgument):
    print(f'This command will be run: {command} {commandArgument}')
    subprocess.run([iCommand,iCommandArgument])
command="touch"
commandArgument="./mygit/CTmyfile.txt"
#print(f'Creating a new file: {command} {commandArgument}')
runThis(command, commandArgument)
#subprocess.run([command,commandArgument])
command="echo"
commandArgument="'Charlie was here' > /home/ec2-user/environment/mygit/CTmyfile.txt"
runThis(command, commandArgument)