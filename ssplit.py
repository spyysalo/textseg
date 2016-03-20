#!/usr/bin/env python

# Run NLTK sentence splitter on input and apply heuristics for
# addressing some frequent issues.

import sys
import re
import nltk.data

ssplitter = nltk.data.load('tokenizers/punkt/english.pickle')

# rarely followed by a sentence split
ns_string = [
    'a.k.a.', 'approx.', 'ca.', 'cf.', 'e.g.', 'et al.', 'f.c.', 'i.e.',
    'lit.', 'vol.'
]

# rarely followed by a sentence split if the next character is a number
ns_num_string = [
    'fig.', 'ib.', 'no.',
]

ns_re = '|'.join(re.escape(s) for s in ns_string)
ns_num_re = '|'.join(re.escape(s) for s in ns_num_string)

for line in sys.stdin:
    split = '\n'.join(ssplitter.tokenize(line.strip()))
    split = re.sub(r'(?i)\b((?:' + ns_re + ')\s*)\n', r'\1 ', split)
    split = re.sub(r'(?i)\b((?:' + ns_num_re + ')\s*)\n(\d)', r'\1 \2', split)
    print split
