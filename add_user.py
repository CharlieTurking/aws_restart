import subprocess 
username = input("Enter the name of the user that you want to add to a group: ") 
output = subprocess.Popen('groups', stdout=subprocess.PIPE).communicate()[0] 
print(output)