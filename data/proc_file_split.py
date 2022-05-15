import sys
import random

with open(sys.argv[1], 'r') as file_origin:
    shardings = int(sys.argv[2])

    names = []
    for i in xrange(shardings):
        name = f'{sys.argv[1]}_{str(i + 1)}'
        names.append(name)

    file_io_handle = [open(names[i], 'w') for i in xrange(shardings)]
    rand_stand = 1.0 / shardings

    for line in file_origin:
        v = random.random()
        part = int(v / rand_stand)
        assert part < shardings

        file_io_handle[part].write(line.strip())
        file_io_handle[part].write('\n')

    for file in file_io_handle:
        file.close()
