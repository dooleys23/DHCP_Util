# Possible code investigations
# x = subprocess.check_output(['ipconfig'])
# x = subprocess.check_output(['DhcpServerv4ScopeStatistics -ComputerName 10.38.97.28 -ScopeId 10.35.170.0'])
import os, subprocess, code


class main():
    def __init__(self):
        self._choice = int(raw_input('Please input a number from the following menu:\n0. Exit\n1. Get a specific scopes details?\n2. Find a device, and its information?\n3. Generate a new .csv with statistics on all scopes?\n'))
        self._argument = 'Powershell.exe DhcpServerv4ScopeStatistics -ComputerName "INSERT_LDAP_SERVER"' #
    def choice(self):
        if self._choice == 0:
            print 'Exiting now'
        elif self._choice == 1:
            self.get_scope_details()
    def get_scope_details(self):
        scope_subnet = str(raw_input('Please enter the subnet you would like to find information on:\nPlease ensure it is in the proper format\nEX:255.255.255.192\n>>>'))
        get_scope_argument = self._argument + ' -ScopeId ' + scope_subnet
        print 'Fetching information now....'
        os.system(get_scope_argument)




x = main()
x.choice()

code.interact(local=locals())
