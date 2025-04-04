## Problem statement:

### Firewall Configuration with Conditionals
Objective
Create an Ansible role named firewall_setup that manages the configuration of the Uncomplicated Firewall (UFW) on Ubuntu servers. This role should dynamically allow or deny services based on a specified variable.

Detailed Description
This role aims to provide a flexible firewall management system using UFW. It leverages Ansible's capability to use conditionals, ensuring that firewall rules adapt based on the configuration specified in the playbook or external variables.

Key Features
Conditional Firewall Rules: Based on the boolean value of service_allowed, the role will configure UFW to either allow or deny specific services such as HTTP and SSH.
Dynamic Rule Application: The role will use Ansible's ufw module to apply firewall rules dynamically, allowing for real-time security adjustments based on environment or security requirements.

### Commands to run the setup:

* ansible-playbook fw_setup.yaml -e "service_allowed=true" --ask-become-pass
* ansible-playbook fw_setup.yaml -e "service_allowed=false" --ask-become-pass
