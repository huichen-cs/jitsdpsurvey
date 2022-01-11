import sys

with open('jitsdp_cited.txt', 'rt', encoding='utf-8') as f:
    lineno = 0
    line = ''
    while True:
        try:
            line = f.readline()
            if line == '':
                break
            lineno = lineno + 1
            for i,c in enumerate(line):
                if not c.isspace() and not c.isprintable():
                    print('char at {} of line {} is non-printable'.format(i, lineno));
            try:
                print(line, file=sys.stderr)
            except UnicodeEncodeError as err:
                # print(lineno, line.encode(), file=sys.stderr)
                # print(err, file=sys.stderr)
                print('line at {} cause error'.format(lineno))
        except UnicodeDecodeError as err:
            # print(lineno, line.encode(), file=sys.stderr)
            # print(err, file=sys.stderr)
            print('line at {} cause error'.format(lineno))
