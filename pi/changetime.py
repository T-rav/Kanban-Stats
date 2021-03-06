"""
Copyright 2014

   Scott Lemmer <scottlemmer1@gmail.com>

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import datetime
import os
from issue import jsonconfig2str

def makeTime():
    filedir=jsonconfig2str()['picDirectory']
    timestamp=datetime.datetime.now().strftime('%y%m%d%H%M')
    print 'new timestamp: '+timestamp
    myfile=open(filedir+"timelog.txt", "a")
    myfile.write("\n"+timestamp)
    myfile.close()

    try:
        os.mkdir(filedir+timestamp)
    except OSError:
        print "Error: The file already exists"
