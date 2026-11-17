import os
from datetime import datetime

os.chdir('d:/srinivas/python/')

print(os.getcwd())

print(os.listdir())

os.makedirs('os_mod')

os.removedirs('os_mod/')

os.rename('test.txt', 'demo.txt')

print(os.stat('demo.txt').st_size)

mod_time = os.stat('demo.txt').st_mtime

print(datetime.fromtimestamp(mod_time))


for dirpath, dirnames, filenames in os.walk('d:/srinivas/python/'):
    print('Current Path:', dirpath)
    print('dir:', dirnames)
    print('files:', filenames)
    print()


print(os.environ.get('NVM_HOME'))

file_path = os.path.join(os.environ.get("NVM_HOME"), 'test.txt')

print(os.path.exists('/tmp/test.png'))

print(os.path.isdir('/tmp/test'))

print(os.path.isfile('/tmp/test'))

print(os.path.splitext('/tmp/test'))
