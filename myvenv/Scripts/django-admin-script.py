#!C:\Users\TsoguevaM\dj\myvenv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Django==2.1.5','console_scripts','django-admin'
__requires__ = 'Django==2.1.5'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Django==2.1.5', 'console_scripts', 'django-admin')()
    )
