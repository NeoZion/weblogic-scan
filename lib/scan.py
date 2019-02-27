# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#@version:python3.7
#@auther:neozion
#projectname:weblogic-scan

'''
    Weblogic version scanning model.
'''

import requests
import sys

from lib.shell import shell

def scanning(url,version=False):
    if version == False:
        shell("Testing Weblogic version").info()
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        }
        try:
            r = requests.get(url,headers=headers,timeout=10)
        except:
            shell("TIMEOUT! Please check Network or URL setting.").warning()
            sys.exit(1)

        try:
            # according to x-powered-by detection weblogic version
            version = r.headers['X-Powered-By'] if r.headers['X-Powered-By'] else False
            shell("This WebLogic version is" + version)
        except:
            pass
        else:
            pass

        if version == False:
            pass
            if version == False:
                shell("Failed to detect weblogic version").warning()
                sys.exit(1)

    # print exploit list and select

    


    
    