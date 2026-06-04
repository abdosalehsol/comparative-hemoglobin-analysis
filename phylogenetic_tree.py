import matplotlib.pyplot as plt

from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram

# Distance data
distances = [
    12,  # Human-Mouse
    15,  # Human-Cow
    31,  # Human-Chicken
    16,  # Mouse-Cow
    33,  # Mouse-Chicken
    35   # Cow-Chicken
]

species = [
    "Human",
    "Mouse",
    "Cow",
    "Chicken"
]

# Build tree
Z = linkage(distances, method="average")

# Plot tree
plt.figure(figsize=(8,5))

dendrogram(
    Z,
    labels=species
)

plt.title("Hemoglobin Phylogenetic Tree")

plt.ylabel("Evolutionary Distance")

plt.tight_layout()

plt.savefig(
    "results/charts/phylogenetic_tree.png"
)

plt.show()