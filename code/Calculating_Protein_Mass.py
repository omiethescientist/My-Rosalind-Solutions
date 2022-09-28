
fn  = "./data/monoisotopic_mass_table.txt"

def create_mass_dict(fn:str):
    with open(fn) as mass_text:
        mass_list = mass_text.readlines()
        mass_dict = {i.split("   ")[0]:float(i.split("   ")[1]) for i in mass_list}
    return mass_dict

def protein_mass(aa_seq:str, mass_dict:dict):
    n = 0 
    for aa in aa_seq:
        n += mass_dict[aa]
    return n

fn_aa_seq = "./data/rosalind_prtm.txt"

with open(fn_aa_seq) as aa_txt:
    aa_seq = aa_txt.read().strip()

mass_dict = create_mass_dict(fn)

print(protein_mass(aa_seq, mass_dict))
