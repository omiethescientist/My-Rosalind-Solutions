import sys
import bisect
import numpy as np
from collections import OrderedDict

fn = sys.argv[1]

with open(fn) as perm:
    n, pi_txt = perm_list = perm.readlines()
    pi_list = pi_txt.split()
    pi = [int(i) for i in pi_list]
    pi = np.array(pi)


def long_inc_subseq(pi):
    subseq_len = [1]
    subseq = [pi[0]]
    for idx in range(1, len(pi)):
        x = pi[idx]
        if x > subseq[-1]:
            subseq.append(x)
            subseq_len.append(len(subseq))
        else:
            j = bisect.bisect_right(subseq, x)
            subseq[j] = x
            subseq_len.append(j+1)
    rv_lis = []
    curr_len = len(subseq)
    for i in range(len(pi)-1, -1, -1):
        if curr_len == subseq_len[i]:
            rv_lis.append(pi[i])
            curr_len -= 1
    return rv_lis[::-1]


def long_dec_subseq(pi):
    pi = [-i for i in pi]
    subseq_len = [1]
    subseq = [pi[0]]
    for idx in range(1, len(pi)):
        x = pi[idx]
        if x > subseq[-1]:
            subseq.append(x)
            subseq_len.append(len(subseq))
        else:
            j = bisect.bisect_right(subseq, x)
            subseq[j] = x
            subseq_len.append(j+1)
    rv_lds = []
    curr_len = len(subseq)
    for i in range(len(pi)-1, -1, -1):
        if curr_len == subseq_len[i]:
            rv_lds.append(pi[i])
            curr_len -= 1
    return [-1*i for i in rv_lds[::-1]]

print(*long_inc_subseq(pi))
print(*long_dec_subseq(pi))

