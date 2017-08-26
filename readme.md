# Logs analysis reporter

A study project from Udacity Fullstack Nanodegree.
The goal of the project is to use SQL to provide insights from the real data and wrap it in plain text with Python language.
To launch the project:
- Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads) and [Vagrant](https://www.vagrantup.com/downloads.html)
- Clone the VM [repository](https://github.com/udacity/fullstack-nanodegree-vm)
- In Terminal open created VM directory
- Change directory to `/vagrant`
- Clone this project repository to this directory
- Download [data archive](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
- Extract it to the root directory of this project repository
- Start the virtual machine by command `vagrant up`
- Connect to VM by command `vagrant ssh`
- Change directory to `/vagrant/this_project_name`
- Run command `./init.sh` to initialise database
- Run command `python UI.py` to start the program
- Follow the instructions in the interactive shell