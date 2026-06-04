import pandas as pd
import matplotlib.pyplot as plt

# Similarity scores
data = {
    "Human":    [100, 88, 85, 69],
    "Mouse":    [88, 100, 84, 67],
    "Cow":      [85, 84, 100, 65],
    "Chicken":  [69, 67, 65, 100]
}

species = ["Human", "Mouse", "Cow", "Chicken"]

# Create DataFrame
df = pd.DataFrame(data, index=species)

print(df)

# Plot heatmap
plt.figure(figsize=(7,6))

heatmap = plt.imshow(df, cmap="viridis")

# Color bar
plt.colorbar(label="Similarity %")

# Labels
plt.xticks(range(len(species)), species)
plt.yticks(range(len(species)), species)

# Add numbers inside cells
for i in range(len(species)):
    for j in range(len(species)):
        plt.text(
            j,
            i,
            df.iloc[i, j],
            ha="center",
            va="center",
            color="white"
        )

# Title
plt.title("Advanced Protein Similarity Heatmap")

# Save figure
plt.savefig(
    "results/charts/advanced_similarity_heatmap.png"
)

# Show plot
plt.show()