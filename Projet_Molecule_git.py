
## - Ouverture du fichier:
# nom du fichier
filename = "C:/Users/Miranda/Desktop/Documents/Centrale/Cours/Info/BE/TC3/Projet/Molécules/Molécules_MolView/Fichiers Mol/H2O.mol"

# lecture du fichier et interpréation des résultats
f = open(filename)
 
# Ligne 1 - Nom de la molécule
molecule_name = f.readline().strip("\n")

# Ligne 2 - This line has the format:
# IIPPPPPPPPMMDDYYHHmmddSSssssssssssEEEEEEEEEEEERRRRRR
# II = User's first and last initials
# PP = program name
# (M/D/Y,H:m) = date/time 
# dd = dimensional codes
# ...
line2 = "{:<53}".format(f.readline().strip("\n"))
user_initials = line2[0:2]
program_name = line2[2:10]

from datetime import datetime
info = line2[10:20]
date_time = datetime(2000+int(info[4:6]),int(info[0:2]),int(info[2:4]),int(info[6:8]),int(info[8:10]))
dim_codes = line2[20:22]


# Ligne 3 - Commentaires
comments = f.readline().strip("\n")

# Ligne 4 - Counts line
# aaabbblllfffcccsssxxxrrrpppiiimmmvvvvvv
# aaa = number of atoms (current max 255)*
# bbb = number of bonds (current max 255)*
# lll = number of atom lists (max 30)*
# ccc = chiral flag: 0=not chiral, 1=chiral
# ...
# vvv = V2000
line4 = "{:<40}".format(f.readline().strip("\n"))
nb_atoms = int(line4[0:3])
nb_bonds = int(line4[3:6])
nb_atom_lists = int(line4[6:9])
chiral = True if int(line4[12:15]) == 1 else False
version = line4[33:39].strip()

# Atom Block
# xxxxx.xxxxyyyyy.yyyyzzzzz.zzzz aaaddcccssshhhbbbvvvHHHrrriiimmmnnneee
# x, y, z = atom coordinates
# aaa = atom symbol
# ...

atoms = []
for n in range(nb_atoms):
    line = "{:<70}".format(f.readline().strip("\n"))
    atoms.append({
        'symbol': line[31:34].strip(),
        'x': float(line[0:10]),
        'y': float(line[10:20]),
        'z': float(line[20:30]),
    })

# Fermeture du fichier
f.close()


# compte-rendu
print("Molecule        : {}".format(molecule_name))
print("User initials   : {}".format(user_initials))
print("Program name    : {}".format(program_name))
print("Date and time   : {}".format(date_time))
print("Dim codes       : {}".format(dim_codes))
print("Comments        : {}".format(comments))
print("Number of atoms : {}".format(nb_atoms))
print("Number of bonds : {}".format(nb_bonds))
print("Number of lists : {}".format(nb_atom_lists))
print("Chiral          : {}".format('yes' if chiral else 'no'))
print("Version         : {}".format(version))
print()

for atom in atoms:
    print('Atom : {} ({:.3f}, {:.3f}, {:.3f})'.format(atom['symbol'],atom['x'],atom['y'],atom['z']))
    
## Création d'une scène à partir de la position des atomes:
from raytracer import *
scene = Scene('benzene', 0, 1)
scene.append(LightSource(vec3(-5., 4, -5), 1))

for a in atoms:
    scene.append(Sphere(vec3(a['x']/5,a['y']/5,a['z']/5), 0.08))

scene.initialize().trace().save_image()
pass