# Command line for the win
The [CMD challenge](https://cmdchallenge.com/) is a cool game designed to sharpen and improve `Bash` skills. The tasks were done on a command line and increased in complexity as the levels progressed. 
The requirement was to do the firts 27 levels while taking screenshots at 9 levels intervals.
The screenshots were then to be uploaded to the sandbox environemnt using the [SFTP File Transfer Protocol](https://www.sftp.net/specification).
Here are the steps followed to move screenshots to the sandbox enviornment.
1. Using a CLI, navigate to the local directory where the screenshots are saved
2. Connect to the `ALX` sandbox using the `sftp` command i.e. `sftp username@hostname`. The username and hostname should be replaced with the hostname of the ALX `sftp` server found in the sandbox section
3. Enter an `sftp` password available on the ALX sandbox
4. Navigate to the `root` directory where the screenshots will be uploaded
5. To upload the files, use the put <name_of_screenshot>
6. When done, exit `sftp` using the `quit` command
