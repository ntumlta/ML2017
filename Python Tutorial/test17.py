import sys

if len(sys.argv) < 2:
    sys.stderr.write('Error: missing input argument\n')
    exit()
with open(sys.argv[1], 'w') as of:
    of.write('check check 1 2\n')

