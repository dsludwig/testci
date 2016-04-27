#!/bin/bash

echo hello world. This is a conda build.
exec_prefix=$(conda info --json | python -c 'import json,sys;print(json.load(sys.stdin)["root_prefix"])')
$exec_prefix/bin/python -c '
import time
import sys
from conda.progressbar import ProgressBar
progress = ProgressBar()
for x in progress(range(10000)):
  sys.stdout.flush()
  time.sleep(0.01)
'
echo 'COMPLETE!'
