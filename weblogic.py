# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#@version:python3.7
#@auther:neozion
#projectname:weblogic-scan

'''  
    This is a weblogic version scanning and exploit tool.
'''

import os
import sys

try:
    from termcolor import colored
    from lib.shell import shell
    from lib.scan import scanning
except Exception as e:
    print(e)
    sys.exit(1)

def main():
    version = False
    if sys.version_info[0] == 2:
        shell("[*] Please use python3").info()
        sys.exit(1)
    
    try:
        version = sys.argv[2]
    except:
        pass

    scanning(sys.argv[1],version)
    

if __name__ == '__main__':
    main()

