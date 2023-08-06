# About

`andrewtools` is an assortment of handy Python tools made by someone named Andrew.

# Quick Start

## Supported Python Versions

Python 3.8+

## Mac / Linux
```
pip install andrewtools
```

## Windows
```
py -m pip install andrewtools
```

## Examples

## Progress Bar

If you are working on a program that uses a loop that takes a significant amount of time to execute, it can be nice to follow the progress of your program while it runs. Use `print_progress_bar` to visualize the progress via the command line.

```
import time
from andrewtools import print_progress_bar

iterations = 10
for i in range(iterations):
    print_progress_bar(i, iterations, width=10, prefix="Progress")
    time.sleep(0.5)

# Printed to command line:
Progress | ***------- | 30%  <- % and progress bar update in-place while loop runs
```

- Warning: this function will not play well if the loop includes other print statements. The progress bar may get printed on a separate line for each iteration, which may not be desirable.