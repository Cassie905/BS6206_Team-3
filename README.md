# BS6206_Team 3

This repository contains all code we used to complete two use cases in BS6206.

### Repository Structure

- `use_case_1.ipynb`: Contains data preprocess and evaluation, such as ROC, accuracy, recall, etc.

- `MixMHC2pred.ipynb`: Preprocess MHC name formats and run MixMHC2pred on the dataset.

- **case 2_task 1/**: Jupyter notebooks for clustering in task 1 of use case 2:
  - `peptides.ipynb`: Extract peptide sequences of lengths 15 and 20 from mutated protein sequences and generate peptides that contain the mutation by identifying mutation sites in the protein sequence.
  - `input_case2.ipynb`: Save the results from peptides.ipynb as an acceptable input form for netMHCIIpan and MixMHC2pred.

- **Clustering/**: Jupyter notebooks for clustering in task 3 of use case 2:
  - `formatadjust.py`: Extract peptides with rank > 60 and adjust the peptide file format to a peptide sequence list.
  - `Clusternet.py`: Cluster peptides based on whether the three amino acids before and after different peptides were the same.
  - `Clusterpred.py`: Adjust the peptide file format to a peptide sequence list and cluster peptides based on whether the three amino acids before and after different peptides were the same.

- `ranking.py`: Combine the results from MixMHC2pred and netMHCIIpan predictions to generate a comprehensive peptide ranking by using a weighted average score.

### Data Access
The benchmarking dataset is downloaded from IEDB.

---

This README provides an overview of the repository's contents and is designed to support the reproducibility of key analyses of two use cases.
