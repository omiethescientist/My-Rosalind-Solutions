#Import protein sequence from uniprot
import sys
from urllib.request import urlopen

fn = sys.argv[1]


def n_glycosylation(string):
    if string[0] == "N":
        if string[1] == "P":
            return False
        elif (string[2] == "S") | (string[2] == "T"):
            if string[3] == "P":
                return False
            else:
                return True
        else:
            return False
    else:
        return False


#Not very efficient
with open(fn, "r") as uniprot_ids:
    uniprot_list = uniprot_ids.read().splitlines()
    #uniprot_list = ['A2Z669', 'B5ZC00', 'P07204_TRBM_HUMAN', 'P20840_SAG1_YEAST']
    for uniprot_id in uniprot_list:
        if "_" in uniprot_id:
            uniprot_id1 = uniprot_id.split("_")[0]
        else:
            uniprot_id1 = uniprot_id
        with urlopen(f'http://www.uniprot.org/uniprot/{uniprot_id1}.fasta') as fasta:
            aa_seq = "".join(fasta.read().decode('utf-8').splitlines()[1:])
            aa_bools = [n_glycosylation(aa_seq[i:i+4]) for i in range(len(aa_seq)-3)]
            inds = [i+1 for i, x in enumerate(aa_bools) if x]
            if len(inds) > 0:
                print(uniprot_id)
                print(*inds)
