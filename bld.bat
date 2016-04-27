setlocal EnableDelayedExpansion
set program=^

import time^
import sys^
from conda.progressbar import ProgressBar^
progress = ProgressBar()^
for x in progress(range(10000)):^
  sys.stdout.flush()^
  time.sleep(0.01)^

echo "build on windows"
\Scripts\Miniconda2\python.exe "%program%"
