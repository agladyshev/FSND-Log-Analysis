# Logs analysis reporter

A study project from Udacity Fullstack Nanodegree.
The goal of the project is to use SQL to provide insights from the real data and wrap it in plain text with Python language. The database for research is a PostgreSQL datatbase for a fictional news website. The database contains three tables: table with all the articles and content, table with authors and their bio, table with logs from all web requests to the site.
The python script can answer the following questions based on the data:
- What are the most popular articles of all time
- What are the most popular authors of all time
- List the days when bad request constitute more than 1% of all requests


To launch the project:
- Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads) and [Vagrant](https://www.vagrantup.com/downloads.html)
- Clone the repositor
- Download [data archive](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
- Extract it to the root directory of this project repository
- Start the virtual machine by command `vagrant up` in project directory
- Connect to VM by command `vagrant ssh`
- Change directory to `/vagrant/this_project_name`
- Run command `./init.sh` to initialise database
- Run command `python UI.py` to start the program
- Follow the instructions in the interactive shell