from Bio import SeqIO
from Bio import pairwise2

# Read sequences

human = SeqIO.read("data/human.fasta", "fasta")
mouse = SeqIO.read("data/mouse.fasta", "fasta")
cow = SeqIO.read("data/cow.fasta", "fasta")
chicken = SeqIO.read("data/chicken.fasta", "fasta")

# Convert to strings

human_seq = str(human.seq)
mouse_seq = str(mouse.seq)
cow_seq = str(cow.seq)
chicken_seq = str(chicken.seq)

# Pairwise alignments

hm = pairwise2.align.globalxx(human_seq, mouse_seq)[0]

hc = pairwise2.align.globalxx(human_seq, cow_seq)[0]

hh = pairwise2.align.globalxx(human_seq, chicken_seq)[0]

print("=" * 60)
print("Human vs Mouse")
print("=" * 60)

print(hm.seqA)
print(hm.seqB)
print("Score:", hm.score)

print()

print("=" * 60)
print("Human vs Cow")
print("=" * 60)

print(hc.seqA)
print(hc.seqB)
print("Score:", hc.score)

print()

print("=" * 60)
print("Human vs Chicken")
print("=" * 60)

print(hh.seqA)
print(hh.seqB)
print("Score:", hh.score)