
import os
import datetime
import shutil
from shutil import copytree, ignore_patterns

files = os.listdir('/media/optimus/')

destination = '/home/optimus/Backup/back_%s'%datetime.datetime.now()
try :
    for f in files:
        source = '/media/optimus/%s' % f
        copytree(source, destination, ignore=ignore_patterns('*.pyc', 'tmp*'))    
except Exception as e:
    print e
