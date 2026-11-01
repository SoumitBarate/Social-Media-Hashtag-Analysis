#!/usr/bin/env python3

import sys

current_hashtag = None
current_count = 0

for line in sys.stdin:
    hashtag, count = line.strip().split('\t')

    count = int(count)

    if current_hashtag == hashtag:
        current_count += count
    else:
        if current_hashtag is not None:
            print(f"{current_hashtag}\t{current_count}")

        current_hashtag = hashtag
        current_count = count

if current_hashtag is not None:
    print(f"{current_hashtag}\t{current_count}")
