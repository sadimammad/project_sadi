import os

print("Operating system:", os.name)

print("Current directory:", os.getcwd())

print("Information:", os.uname())

print("Files and directories:")
for i in os.listdir():
    print(i)






