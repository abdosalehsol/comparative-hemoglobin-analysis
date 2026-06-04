import pandas as pd

import matplotlib.pyplot as plt

# Similarity scores

data = {
    "Human": [100, 88, 85, 69]
}

species = [
    "Human",
    "Mouse",
    "Cow",
    "Chicken"
]

# Create DataFrame

df = pd.DataFrame(
    data,
    index=species
)

print(df)

# Plot heatmap

plt.figure(figsize=(6,4))

plt.imshow(df, aspect="auto")

plt.colorbar(label="Similarity Score")

plt.xticks([0], ["Human"])

plt.yticks(range(len(species)), species)

plt.title("Protein Similarity Heatmap")

plt.savefig(
    "results/charts/protein_similarity_heatmap.png"
)

plt.show()