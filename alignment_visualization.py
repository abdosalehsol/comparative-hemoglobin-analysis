import matplotlib.pyplot as plt

comparisons = [
    "Human vs Mouse",
    "Human vs Cow",
    "Human vs Chicken"
]

scores = [88, 85,76]

plt.figure(figsize=(8,5))

plt.bar(comparisons, scores)

plt.title("Sequence Alignment Scores")

plt.xlabel("Comparisons")

plt.ylabel("Alignment Score")

plt.savefig(
    "results/charts/alignment_scores.png"
)

plt.show()