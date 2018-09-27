import os, subprocess, code
from threading import Thread
from Queue import Queue


class Main:
    def __init__(self):
        self._argument = 'Powershell.exe DhcpServerv4ScopeStatistics -ComputerName "#DHCP HOST"' #97.28 is the LDAP server used in RDP
        self._task_queue = Queue()

    def choice(self):
        self._choice = int(raw_input(
            'Please input a number from the following menu:'
            '\n0. Exit\n1. Get a specific scopes details?'
            '\n2. Find a device, and its information?'
            '\n3. Generate a new .csv with statistics on all scopes?\n4. Blank\n5. Execute Batch Job\n>>>'))
        if self._choice == 0:
            print 'Exiting now'
        elif self._choice == 1:
            self.get_scope_details()
            x.choice()
        elif self._choice == 5:
            self.execute_batch_jobs()

    def get_scope_details(self):
        scope_subnet = str(raw_input('Please enter the subnet you would like to find information on:'
                                     '\nPlease ensure it is in the proper format\nEX:255.255.255.192\n>>>'))
        get_scope_argument = self._argument + ' -ScopeId ' + scope_subnet
        self._task_queue.put(get_scope_argument)
        print 'Job added to batch list. Returning to main menu:\n'
        x.choice()
        # os.system(get_scope_argument)


#5, done
    def execute_batch_jobs(self):
        thread_count = self._task_queue.qsize() # get int value for total count of batch jobs

        for i in range(thread_count):
            process = Thread(target=self.threaded_jobs())
            process.setDaemon(True)
            process.start()
        quit()

    def threaded_jobs(self):
        while not self._task_queue.empty():
            print self._task_queue.get()
            self._task_queue.task_done()
# x = os.system('powershell.exe DhcpServerv4ScopeStatistics -ComputerName #DHCP HOST# -ScopeId')

x = Main()
x.choice()

code.interact(local=locals())
