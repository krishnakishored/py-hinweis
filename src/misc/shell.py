"""
the shell can be an interface between the operating system and the services of the kernel of this operating system.
Understanding this, it's obvious that a shell can be either a command-line interface (CLI) or  (GUI)
"""

import os, platform

if platform.system() == "Windows":
    import msvcrt


def getch():
    if platform.system() == "Linux":
        os.system('bash -c "read -n 1"')
    else:
        msvcrt.getch()


print("Type a key!")
key = getch()
# You can't use the getch() function, because os.system() doesn't return the result of the called shell commands.
print("Okay " + str(key))  # None
