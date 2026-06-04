from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import os

data_folder = "data"

for file in os.listdir(data_folder):

    if file.endswith(".fasta"):

        file_path = os.path.join(data_folder, file)

        for record in SeqIO.parse(file_path, "fasta"):

            sequence = str(record.seq)

            analysis = ProteinAnalysis(sequence)

            print("=" * 50)
            print("File:", file)

            print("Protein Length:")
            print(len(sequence))

            print("Molecular Weight:")
            print(round(analysis.molecular_weight(), 2))

            print("Amino Acid Composition:")
            print(analysis.count_amino_acids())