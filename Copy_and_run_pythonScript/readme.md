# Problem Statement
The playbook will manage several tasks:

Directory Creation: Ensures a specific directory exists where the Python script will be stored.
File Deployment: Copies the Python script to the specified directory.
Script Execution: Executes the Python script using an environment variable to pass data.
Output Management: Captures and displays the output from the Python script.
Directory Structure
Your project should have a structured directory to organize the Ansible playbook, roles, and the Python script. Here’s the suggested structure:

/home/user
|-- roles/
|   |-- greet/
|       |-- tasks/
|           |-- main.yml
|-- greet.py
|-- greet.yml
Sample greet.py
# File: greet.py
import os

def main():
    # Retrieve the USER_NAME from an environment variable, defaulting to "World"
    user_name = os.getenv("USER_NAME", "World")
    # Print a customized greeting message
    print(f"Hello, {user_name}!")

if __name__ == "__main__":
    main()
Creating the Role (roles/greet/tasks/main.yml)
The role contains all the tasks necessary to deploy and run your script:

Steps to Create roles/greet/tasks/main.yml
1. Create a Directory
This task ensures that a specific directory exists on the localhost where the Python script will be stored. If the directory does not exist, Ansible will create it.

Path: /usr/local/app — The directory where the script will be placed.
Permissions: Set to 0755 to allow the script owner to read, write, and execute within the directory, while others can only read and execute.
- name: Ensure the application directory exists
  file:
    path: "/usr/local/app"
    state: directory
    mode: '0755'
2. Copy the Script
This task copies the greet.py script from the Ansible control machine to the localhost. In this scenerio, we are using localhost only. It ensures that the script is placed in the previously created directory.

Source: The location of greet.py is the /home/user.
Destination: You need to copy greet.py inside /usr/local/app directory.
Permissions: Set to 0755, allowing the script to be executed by the owner and read/executed by others, ensuring that the script can be run securely.
3. Execute the Script
This task executes the greet.py script on the localhost. It uses an environment variable to pass a username to the script, which the script uses to customize its output.

Command: The command to run the Python script.
Environment Variable: USER_NAME is set dynamically through the playbook and is used by the script to customize the greeting.
Output Registration: Captures the output of the script for further use or debugging. The name of the register is greet_output.
4. Handle the Output
After the script is executed, this task displays the output captured from the script. This is useful for debugging and verifying that the script ran as expected.

Debug Module: Used to print the output of the script to the Ansible console/log.
Task-2: Create the greet.yml playbook in /home/user.
In this YAML, ensure to mention:

Hosts: localhost
Permissions: Use become: yes
Variables: Define user_name as alice.
Roles: Include greet
Execution
Run the playbook using the following command from your Ansible control machine:

ansible-playbook greet.yml -K
