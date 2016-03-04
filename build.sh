#!/bin/bash

echo hello world. This is a conda build.
source activate root
python -c '
import time
from conda.progressbar import ProgressBar
progress = ProgressBar()
for x in progress(range(1000)):
  time.sleep(0.01)
'
echo 'COMPLETE!'
