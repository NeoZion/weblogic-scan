# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#@version:python3.7
#@auther:neozion
#projectname:weblogic-scan

import time

from termcolor import colored

class shell(object):
    def __init__(self,string):
        self._time = '['+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+']  ' 
        self._string = string

    def info(self):
        print(colored(self._time + self._string,'green'))
    
    def warning(self):
        print(colored(self._time + self._string,'red'))
