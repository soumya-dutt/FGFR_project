from Bio import PDB

# Load the PDB file
parser = PDB.PDBParser()
structure = parser.get_structure('my_structure', 'prot_dry.pdb')

# Initialize a new residue ID counter
new_residue_id = 0

# Iterate through the structure and change residue IDs
for model in structure:
    for chain in model:
        for residue in chain:
            # Change the residue ID to the new value
            residue.id = (' ', new_residue_id, ' ')

            # Increment the new residue ID
            new_residue_id += 1

# Save the modified structure to a new PDB file
io = PDB.PDBIO()
io.set_structure(structure)
io.save('new_pdbfile.pdb')