from Bio import SeqIO
import os
data_folder = "data"
for file in os.listdir(data_folder):
    if file.endswith(".fasta"):
        file_path = os.path.join(data_folder,file)
        for record in SeqIO.parse(file_path,"fasta"):
    
         print("=" *50)
         print("file:", file)
         print("ID:",record.id)
         print("Length:", len(record.seq))
         print("sequence:")
         print(record.seq[:50],"...")
        