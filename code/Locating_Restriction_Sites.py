import sys

fn = sys.argv[1]

def rev_comp(dna_seq:str):
    dna_dict = {"A":"T", "T":"A", "G":"C", "C":"G"}
    reverse = dna_seq[::-1]
    complement = "".join([dna_dict[n] for n in reverse])
    return complement

def find_rest_sites(seq):
    matches = []
    N = len(seq)
    for n in range(4, 13):
            seqs = [(i+1, n) for i in range(N-n+1) if seq[i:i+n] == rev_comp(seq[i:i+n])]
            matches += seqs
    return matches

with open(fn) as fasta:
    seq_list = fasta.read().split("\n")
    seq = "".join(seq_list[1:])

#seq = "TCAATGCATGCGGGTCTATATGCAT"
print(seq)
for rest_site in find_rest_sites(seq):
    print(*rest_site)
