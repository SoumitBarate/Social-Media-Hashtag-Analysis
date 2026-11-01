#!/usr/bin/env python3

import sys
import re

for line in sys.stdin:
    hashtags = re.findall(r'#\w+', line.lower())

    for hashtag in hashtags:
        print(f"{hashtag}\t1")
