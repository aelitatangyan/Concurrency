#################################################################################################################
### Fork and Exec with Arguments 
#################################################################################################################
### What program does:                 
###     - Uses fork to create a child process.
###     - The child process should use execl to run the echo command with an argument (e.g., "Hello from the child process").
###     - The parent process should print "Parent process done" after the child process is created.
#################################################################################################################
### Expected Output:
###     The message from the echo command followed by the parent's message.
#################################################################################################################


import os
import time

def main():
    pid = os.fork()
    st = 0
    if not pid:
       st = os.execl("/bin/echo", "echo", "Hello from the child process")
    else:
        os.wait()
        print("Parent process done")
    if st:
        return 1
    return 0
    


if __name__ == "__main__":
    main()
