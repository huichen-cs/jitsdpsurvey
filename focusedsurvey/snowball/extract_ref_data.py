import re
import sys

from enum import Enum




class ParserState(Enum):
    BEGIN = 0
    EXPECT_PAPER = 1,
    EXPECT_REF_HEAD = 2,
    EXPECT_MORE_REF_LINES = 3,
    END_REF_ENTRY = 4,
    END_PAPER = 5,
    END = 6

state = ParserState.BEGIN
paper = None
lineno = 0
spattern = None
ref_line_list = []
paper_refs = 0
paper_count = 0
total_refs = 0




def is_comment(line):
    return len(line.strip()) > 0 and line.strip()[0] == '#'

def is_blank(line):
    return len(line.strip()) == 0

def is_paper_header(line):
    return line.startswith('>>')

def is_valid_paper_header(line):
    return not re.match('^>><.+>.+', line) is None
    
def get_ref_start_pattern(header):
    m = re.match('^>><(.+)>.+', header)
    if len(m.groups()) != 1:
        raise RuntimeError('Not a valid header line [[{}]]'.format(line))
    fmt = m.groups()[0]
    if fmt == 'A(Y)':
        pattern = '^\s*\D+\(\d{4}[a-z]*\)'
    elif fmt == 'AY':
        pattern = '^\s*\D+\d{4}'
    elif fmt == '[N]':
        pattern = '^\s*\[\d+\]'
    elif fmt == 'N':
        pattern = '^\s*\d+\s+'
    elif fmt == 'N.':
        pattern = '^\s*\d+\.\s+'
    else:
        raise RuntimeError('Not a valid header line [[{}]]'.format(line))
    return pattern


def is_ref_head_line(spattern, line):
    return not re.match(spattern, line) is None

def log_state(logfd, state, lineno, line, *argv):
    if argv:
        print('state = {}, lineno = {}, line = {}, argv = {}'.format(state, lineno, line, argv), file=logfd)
    else:
        print('state = {}, lineno = {}, line = {}'.format(state, lineno, line), file=logfd)



def parse(stack, outfd, logfd):
    global state, ref_line_list, spattern, paper, total_refs, paper_refs, paper_count
    while stack:
        if state == ParserState.EXPECT_PAPER:
            line = stack.pop()
            log_state(logfd, state, lineno, line)
            if is_paper_header(line) and is_valid_paper_header(line):
                state = ParserState.EXPECT_REF_HEAD
                paper = line
                spattern = get_ref_start_pattern(line)
            else:
                raise RuntimeError('Not a valid header line [[{}]] at line {}'.format(line, lineno))
            paper_refs = 0
        elif state == ParserState.EXPECT_REF_HEAD:
            line = stack.pop()
            log_state(logfd, state, lineno, line)
            if is_ref_head_line(spattern, line):
                ref_line_list.append(line)
                state = ParserState.EXPECT_MORE_REF_LINES
            elif is_paper_header(line):
                stack.append(line)
                state = ParserState.END_PAPER
            else:
                log_state(logfd, state, lineno, None)
                raise RuntimeError('Unexpected state {} at line {}'.format(state, lineno))
        elif state == ParserState.EXPECT_MORE_REF_LINES:
            line = stack.pop()
            log_state(logfd, state, lineno, line)
            if is_ref_head_line(spattern, line):
                stack.append(line)
                state = ParserState.END_REF_ENTRY
            elif is_paper_header(line):
                stack.append(line)
                state = ParserState.END_REF_ENTRY
            else:
                ref_line_list.append(line)
                state = ParserState.EXPECT_MORE_REF_LINES
        elif state == ParserState.END_REF_ENTRY:
            refentry = ' '.join(ref_line_list)
            print(refentry, file=outfd)
            paper = None
            ref_line_list.clear()
            paper_refs = paper_refs + 1
            total_refs = total_refs + 1
            log_state(logfd, state, lineno, None, [paper_count, paper_refs, total_refs, refentry])
            state = ParserState.EXPECT_REF_HEAD
        elif state == ParserState.END_PAPER:
            paper_count = paper_count + 1
            log_state(logfd, state, lineno, None, [paper_count, paper_refs, total_refs])
            state = ParserState.EXPECT_PAPER
            paper_refs = 0
        else:
            log_state(logfd, state, lineno, None)
            raise RuntimeError('Unexpected state {} at line {}'.format(state, lineno))



def extract_ref_entries(infd, outfd, logfd):
    global lineno, state, paper_refs, total_refs, paper_count
    state = ParserState.EXPECT_PAPER
    stack = []
    for line in infd.readlines():
        lineno = lineno + 1
        line = line.strip()
        if is_blank(line):
            continue
        if is_comment(line):
            continue
        stack.append(line)
        parse(stack, outfd, logfd)
    if ref_line_list:
       refentry = ' '.join(ref_line_list)
       print(refentry, file=outfd)
       state = ParserState.END_REF_ENTRY
       paper_refs = paper_refs + 1
       total_refs = total_refs + 1
       log_state(logfd, state, lineno, None)
       state = ParserState.END_PAPER
       paper_count = paper_count + 1
       log_state(logfd, state, lineno, None, [paper_count, paper_refs, total_refs])
    state = ParserState.END
    log_state(logfd, state, lineno, None, [paper_count, paper_refs, total_refs])



def process_file(infile, outfile, logfile):
    with \
        open(infile, 'rt', encoding='utf-8') as infd, \
        open(outfile, 'wt', encoding='utf-8') as outfd, \
        open(logfile, 'wt', encoding='utf-8') as logfd:
        extract_ref_entries(infd, outfd, logfd)


def main(argv):
    if len(argv) < 4:
        infile = 'jitsdp_cited.txt'
        outfile = 'jitsdp_cited_entries.txt'
        logfile = 'extract_ref_data.log'
    else:
        [infile, outfile, logfile] = argv[1:4]

    process_file(infile, outfile, logfile)


if __name__ == '__main__':
    main(sys.argv)
