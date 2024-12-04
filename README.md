## Task Tracker CLI 
Task tracker is a project used to track and manage your tasks. 
In this task, you will build a simple command line interface (CLI) to track what you need to do, what you have done, and what you are currently working on. 
This project will help you practice your programming skills, including working with the filesystem, handling user inputs, and building a simple CLI application.

### How to solve this task
1. Write a python script that contains the functions of the above mentioned operations.
2. (optional) run the python scrips if the logic is correct and if it is working properly.
3. Install and run nuitka, which is used to convert python script to executable script
   use `pip install nuitka`
4. Run the command `nuitka --standalone --onefile --output-dir=dist task-cli.py` which is the command used to convert python script to executable script.
   Code breakdown:
   --standalone: Packages all the dependencies into a single folder.
   --onefile: Creates a single executable .exe file.
   --output-dir-dist: Specifies that the output has to be in a directory called "dist".
5. After execution of this commad, a directory called as dist is created. It has 2 sub folders task-cli.build, and task-cli.dist.
6. Navigate into task-cli.dist and find the executable file (task-cli.exe).
7. To run this executable file, run command in the format `.\task-cli "function" "argument"`. eg. `.\task-cli add "Buy groceries."`
8. After execution of the command, for verification if it has executed properly, check tasks.json in the dist directory if the operation has been accurate