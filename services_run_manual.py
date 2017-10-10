#!/usr/bin/python3
#!/usr/bin/python
#
#
#Created by JongoFett (2017)
#
#I wanted to create a module that would check services and run them if they
#aren't running already. This one gives you feedback.
#
#Just a simple excerise to get me used to python really
#

import os, sys, subprocess

#This is the subprocess which finds if the service is active
def run_command(command):
    p = subprocess.Popen(command,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
    return iter (p.stdout.read, b'')
#If the service is not active then this command is run
def start_service(run_serv):
    r = subprocess.Popen(run_serv,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)

if __name__ == '__main__':
#Service list, more can be added/removed/amended
    services = ('service0', 'service1')
    for serv in services[0:]:
#the line here creates the command to be run using the 'services' list
        command = 'systemctl is-active {}'.format(serv).split()
for line in run_command(command):
#I found that the result needed decoding as it was coming back as bytes and
#a comparison was not possible until this was done.
    line = line.decode("utf-8").rstrip()

#This will check to see if the serices are active, if not then it will activate
#only the required services. I don't believe this will even attempt to activate
#a service which is already running. Though I haven't checked so could be wrong.
active_service = 'active'
services = ('service0', 'service1')
if line == active_service:
    for serv in services[0::]:
#as with the 'command' portion above this uses the list to start a
#service that shows to not be running. I am sure I could have handeled
#the list portion better and I may look to improve the code later.
#Make sure all lists are changed and match, otherwise it is possible
#this won't work correctly.
        print('{} is '.format(serv) + line)
else:
    for serv in services[0::]:
        print('{} was not active, activating it now'.format(serv))
        run_serv = 'sudo systemctl start {}'.format(serv).split()
        start_service(run_serv)
