#################################################################################################################
### Multiple Forks and Execs
#################################################################################################################
### What program does:                 
###     - Creates two child processes using fork.
###     - The first child process should use execl to run the ls command.
###     - The second child process should use execl to run the date command.
###     - The parent process should print "Parent process done" after creating both child processes.
#################################################################################################################
### Expected Output:
###     The output of the ls command followed by the output of the date command, and finally the parent's message.
#################################################################################################################


import os
import time

def main():
    pid1 = os.fork()
    st = 0
    if not pid1:
       st = os.execl("/bin/ls", "ls")
    else:
        pid2 = os.fork()
        if not pid2:
            st = os.execl("/bin/date", "date" "main")
        else:
            #Solution 1
            #os.wait()
            #os.wait()
            
            #Solution 2
            os.waitpid(pid1, 0)
            os.waitpid(pid2, 0)
            print("Parent process done")
    if st:
        return 1
    return 0
    


if __name__ == "__main__":
    main()
