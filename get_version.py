#!/usr/bin/env python

from __future__ import print_function

import subprocess

try:
    v = subprocess.check_output(['git', 'describe', '--tags'], universal_newlines=True)
except Exception:
    print('unknown')
else:
    print(v.strip().replace('-', '.'))
