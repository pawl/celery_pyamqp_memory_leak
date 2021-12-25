import linecache
import os
import tracemalloc
from time import sleep

from tasks import app

def print_stats():
    insp = app.control.inspect()
    active_lst = insp.active()
    cluster_stats = insp.stats()
    active_queues = insp.active_queues()
    all_stats = {
        "active": active_lst,
        "stats": cluster_stats,
        "queues": active_queues
    }
    print(all_stats)


def display_top(snapshot, key_type='lineno', limit=10):
    snapshot = snapshot.filter_traces((
        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
        tracemalloc.Filter(False, "<unknown>"),
    ))
    top_stats = snapshot.statistics(key_type)

    print("Top %s lines" % limit)
    for index, stat in enumerate(top_stats[:limit], 1):
        frame = stat.traceback[0]
        print("#%s: %s:%s: %.1f KiB"
              % (index, frame.filename, frame.lineno, stat.size / 1024))
        line = linecache.getline(frame.filename, frame.lineno).strip()
        if line:
            print('    %s' % line)

    other = top_stats[limit:]
    if other:
        size = sum(stat.size for stat in other)
        print("%s other: %.1f KiB" % (len(other), size / 1024))
    total = sum(stat.size for stat in top_stats)
    print("Total allocated size: %.1f KiB" % (total / 1024))

tracemalloc.start()


def main():
    while True:
        print_stats()
        snapshot = tracemalloc.take_snapshot()
        display_top(snapshot)
        sleep(1)


if __name__ == '__main__':
    main()
