from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import os
import matplotlib.pyplot as plt

data_folder = "data"

species_names = []
protein_lengths = []
molecular_weights = []

for file in os.listdir(data_folder):

    if file.endswith(".fasta"):

        file_path = os.path.join(data_folder, file)

        for record in SeqIO.parse(file_path, "fasta"):

            sequence = str(record.seq)

            analysis = ProteinAnalysis(sequence)

            species = file.replace(".fasta", "")

            species_names.append(species)

            protein_lengths.append(len(sequence))

            molecular_weights.append(
                analysis.molecular_weight()
            )

# Protein Length Chart
plt.figure(figsize=(8,5))

plt.bar(species_names, protein_lengths)

plt.title("Protein Length Comparison")

plt.xlabel("Species")

plt.ylabel("Protein Length")

plt.savefig(
    "results/charts/protein_length.png"
)

plt.show()
# Molecular Weight Chart

plt.figure(figsize=(8,5))

plt.bar(species_names, molecular_weights)

plt.title("Molecular Weight Comparison")

plt.xlabel("Species")

plt.ylabel("Molecular Weight")

plt.savefig(
    "results/charts/molecular_weight.png"
)

plt.show()
# Amino Acid Frequency Plot

human_file = "data/human.fasta"

for record in SeqIO.parse(human_file, "fasta"):

    sequence = str(record.seq)

    analysis = ProteinAnalysis(sequence)

    amino_acids = analysis.count_amino_acids()

    acids = list(amino_acids.keys())

    counts = list(amino_acids.values())

    plt.figure(figsize=(10,5))

    plt.bar(acids, counts)

    plt.title(
        "Human Hemoglobin Amino Acid Frequency"
    )

    plt.xlabel("Amino Acids")

    plt.ylabel("Frequency")

    plt.savefig(
        "results/charts/amino_frequency.png"
    )

    plt.show()
    # Amino Acid Frequency Plot

cow_file = "data/cow.fasta"

for record in SeqIO.parse(cow_file, "fasta"):

    sequence = str(record.seq)

    analysis = ProteinAnalysis(sequence)

    amino_acids = analysis.count_amino_acids()

    acids = list(amino_acids.keys())

    counts = list(amino_acids.values())

    plt.figure(figsize=(10,5))

    plt.bar(acids, counts)

    plt.title("cow hemoglobin Amino acid Frequency")
    
    plt.xlabel("Amino Acids")

    plt.ylabel("Frequency")

    plt.savefig(
        "results/charts/amino_frequency.png"
    )

    plt.show()
    import pandas as pd

# Heatmap Data

heatmap_data = {}

for file in os.listdir(data_folder):

    if file.endswith(".fasta"):

        file_path = os.path.join(data_folder, file)

        for record in SeqIO.parse(file_path, "fasta"):

            sequence = str(record.seq)

            analysis = ProteinAnalysis(sequence)

            amino_acids = analysis.count_amino_acids()

            species = file.replace(".fasta", "")

            heatmap_data[species] = amino_acids

# Convert to DataFrame

df = pd.DataFrame(heatmap_data)

# Plot Heatmap

plt.figure(figsize=(10,8))

plt.imshow(df,
           aspect='auto')

plt.colorbar(label="Frequency")

plt.xticks(
    range(len(df.columns)),
    df.columns
)

plt.yticks(
    range(len(df.index)),
    df.index
)

plt.title(
    "Comparative Amino Acid Heatmap"
)

plt.xlabel("Species")

plt.ylabel("Amino Acids")

plt.savefig(
    "results/charts/heatmap.png"
)

plt.show()