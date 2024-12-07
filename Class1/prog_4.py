#############################################################################################################
### Simple Fork and Exec
#############################################################################################################
### *Propgram uses test.txt file from same directory
### What program does:                 
###    - Uses fork to create a child process.
###    - The child process should use execl to run the grep command to search for a specific word (e.g., "main") in a text file (e.g., test.txt).
###    - The parent process should print "Parent process completed".
#############################################################################################################
### Expected Output:
###    The lines in the file test.txt that contain the word "main" followed by "Parent process completed".
#############################################################################################################

import os
import time

def main():
    pid = os.fork()
    st = 0
    if not pid:
       st = os.execl("/usr/bin/grep", "grep", "main", "test.txt")
    else:
        os.wait()
        print("Parent process completed")
    if st:
        return 1
    return 0
    


if __name__ == "__main__":
    main()
