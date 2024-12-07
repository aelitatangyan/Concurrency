#############################################################################################################
### Simple Fork and Exec
#############################################################################################################
### What program does:                 
###    - Uses fork to create a child process.
###    - In the child process, use execl to run the ls command to list the contents of the current directory.
###    - The parent process should print "Parent process done" after the child process is created.
#############################################################################################################
### Expected Output:
###     The directory listing should be printed, followed by the parent's message.
#############################################################################################################

import os
import time

def main():
    pid = os.fork()
    st = 0
    if not pid:
        st = os.execl("/bin/ls", "ls")
    else:
        os.wait()
        print("Parent process done")
    if st:
        return 1
    return 0
    


if __name__ == "__main__":
    main()
