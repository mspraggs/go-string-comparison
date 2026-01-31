from collections import defaultdict
import re
import sys

import matplotlib.pyplot as plt
import numpy as np


STAT_REGEX = re.compile(r'BenchmarkCompare/matching=(\d+)-\d\s*\d+\s*(\d+\.\d+) ns/op')


if __name__ == '__main__':
    try:
        data_path = sys.argv[1]
    except IndexError:
        print(f'Usage: python {sys.argv[0]} <data path>')
        sys.exit()

    data = defaultdict(list)
    with open(data_path) as f:
        for line in f.readlines():
            m = STAT_REGEX.match(line)
            if not m:
                continue

            data[int(m.group(1))].append(float(m.group(2)))

    averages = np.zeros(len(data))
    errors = np.zeros(len(data))

    for length, data in data.items():
        averages[length] = np.average(data)
        errors[length] = np.std(data)

    plt.figure(figsize=(8, 6))
    plt.errorbar(np.arange(averages.size), averages, errors, fmt='o', capsize=0)
    plt.xlabel('Matching bytes')
    plt.ylabel('Comparison time / ns')
    plt.tight_layout()
    plt.show()
