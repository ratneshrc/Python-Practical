import os

# Current directory
print("Current Directory:")
print(os.getcwd())

# Create directory
if not os.path.exists("TestFolder"):
    os.mkdir("TestFolder")
    print("TestFolder created")
else:
    print("TestFolder already exists")

# List directory
print("\nFiles and folders:")
print(os.listdir())


# Rename directory
if os.path.exists("TestFolder"):
    os.rename("TestFolder", "NewFolder")
    print("TestFolder renamed to NewFolder")

# Delete directory
if os.path.exists("NewFolder"):
    os.rmdir("NewFolder")
    print("NewFolder deleted")