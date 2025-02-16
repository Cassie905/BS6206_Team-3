import pandas as pd

#data = pd.read_csv('D:/6206/pythonProject1/peptide_DRB1_150101.txt', header=0, names=['Peptide'], sep='\t')
#data = pd.read_csv('D:/6206/pythonProject1/peptide_DRB1_110101.txt', header=0, names=['Peptide'], sep='\t')
#data = pd.read_csv('D:/6206/pythonProject1/peptide_HLA-DPA10103-DPB10401.txt', header=0, names=['Peptide'], sep='\t')
#data = pd.read_csv('D:/6206/pythonProject1/peptide_HLA-DQA10102-DQB10602.txt', header=0, names=['Peptide'], sep='\t')
#data = pd.read_csv('D:/6206/pythonProject1/peptide_HLA-DQA10102-DQB10301.txt', header=0, names=['Peptide'], sep='\t')
#data = pd.read_csv('D:/6206/pythonProject1/peptide_HLA-DQA10505_DQB10301.txt', header=0, names=['Peptide'], sep='\t')
data = pd.read_csv('D:/6206/pythonProject1/peptide_HLA-DQA10505_DQB10602.txt', header=0, names=['Peptide'], sep='\t')
print(len(data))

def merge_peptides(peptides, overlap_length=3):
    used = [False] * len(peptides)
    merged = []

    for i in range(len(peptides)):
        if used[i]:
            continue
        current = peptides[i]
        used[i] = True


        while True:
            merged_flag = False
            for j in range(len(peptides)):
                if used[j]:
                    continue


                if current[-overlap_length:] == peptides[j][:overlap_length]:
                    current += peptides[j][overlap_length:]
                    used[j] = True
                    merged_flag = True
                    break


            if not merged_flag:
                break


        merged.append(current)

    return merged

peptide_list = data['Peptide'].tolist()

merged_peptides = merge_peptides(peptide_list, overlap_length=3)

merged_peptides_sorted = sorted(merged_peptides, key=len, reverse=True)

merged_df = pd.DataFrame(merged_peptides_sorted, columns=['Merged_Peptide'])
merged_df.to_csv('merged_peptides.txt', index=False, header=True, sep='\t')
print(len(merged_peptides_sorted))
print("Merged peptides have been saved to 'merged_peptides.txt'.")
changed_peptides = [seq for seq in merged_peptides_sorted if seq not in peptide_list]
changed_df = pd.DataFrame(changed_peptides, columns=['Changed_Peptide'])

#changed_df.to_csv('changed_peptides_DRB1_150101.txt', index=False, header=True, sep='\t')
#changed_df.to_csv('changed_peptides_DRB1_110101.txt', index=False, header=True, sep='\t')
#changed_df.to_csv('changed_peptides_DPA10103-DPB10401.txt', index=False, header=True, sep='\t')
#changed_df.to_csv('changed_peptides_DQA10102-DQB10602.txt', index=False, header=True, sep='\t')
#changed_df.to_csv('changed_peptides_DQA10102-DQB10301.txt', index=False, header=True, sep='\t')
#changed_df.to_csv('changed_peptides_DQA10505_DQB10301.txt', index=False, header=True, sep='\t')
changed_df.to_csv('changed_peptides_DQA10505_DQB10602.txt', index=False, header=True, sep='\t')
print("Changed peptides have been saved to 'changed_peptides.txt'.")