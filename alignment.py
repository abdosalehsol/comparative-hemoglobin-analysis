from Bio import SeqIO
from Bio import pairwise2

# Read sequences

human_record = SeqIO.read(
    "data/human.fasta",
    "fasta"
)

mouse_record = SeqIO.read(
    "data/mouse.fasta",
    "fasta"
)

human_seq = str(human_record.seq)

mouse_seq = str(mouse_record.seq)

# Perform alignment

alignments = pairwise2.align.globalxx(
    human_seq,
    mouse_seq
)

# Best alignment

best_alignment = alignments[0]

print("=" * 50)

print("Human vs Mouse Alignment")

print("=" * 50)

seqA = best_alignment.seqA

seqB = best_alignment.seqB

match_line = ""

for a, b in zip(seqA, seqB):

    if a == b:

        match_line += "|"

    else:

        match_line += " "

print(seqA)

print(match_line)

print(seqB)
# Calculate Identity Percentage

matches = 0

total = len(seqA)

for a, b in zip(seqA, seqB):

    if a == b:

        matches += 1

identity = (matches / total) * 100

print()

print("Percentage Identity:")

print(round(identity, 2), "%")