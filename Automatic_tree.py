from Bio import SeqIO
from Bio import pairwise2

from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram

import matplotlib.pyplot as plt

# Read sequences
species = ["human", "mouse", "cow", "chicken"]

sequences = {}

for sp in species:
    record = SeqIO.read(f"data/{sp}.fasta", "fasta")
    sequences[sp] = str(record.seq)

# Define all pairwise comparisons
pairs = [
    ("human", "mouse"),
    ("human", "cow"),
    ("human", "chicken"),
    ("mouse", "cow"),
    ("mouse", "chicken"),
    ("cow", "chicken")
]

# Calculate distances
distances = []

for a, b in pairs:

    alignment = pairwise2.align.globalxx(
        sequences[a],
        sequences[b],
        one_alignment_only=True
    )[0]

    score = alignment.score

    max_len = max(
        len(sequences[a]),
        len(sequences[b])
    )

    identity = (score / max_len) * 100

    distance = 100 - identity

    distances.append(distance)

    print(f"{a} vs {b}")
    print(f"score = {score}")
    print(f"identity = {identity:.2f}")
    print(f"distance = {distance:.2f}")
    print("-" * 30)

print("Final distances =", distances)
print("Final length =", len(distances))

# Build phylogenetic tree
Z = linkage(distances, method="average")

# Plot tree
plt.figure(figsize=(8, 5))

dendrogram(
    Z,
    labels=["Human", "Mouse", "Cow", "Chicken"]
)

plt.title("Automatic Hemoglobin Phylogenetic Tree")
plt.ylabel("Distance")

plt.tight_layout()

plt.show()