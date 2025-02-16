import pandas as pd

#file_path = "D:/6206/pythonProject1/net_length_20/net_DRB1_110101.txt"# 替换为实际文件路径
file_path = "D:/6206/pythonProject1/net_length_20/net_DRB1_150101.txt"
#file_path = "D:/6206/pythonProject1/net_length_20/net_DPA10103_DPB10401.txt"
#file_path = "D:/6206/pythonProject1/net_length_20/net_DQA10102-DQB10602.txt"
#file_path = "D:/6206/pythonProject1/net_length_20/net_DQA10102-DQB10301.txt"
#file_path = "D:/6206/pythonProject1/net_length_20/net_DQA10505-DQB10301.txt"
#file_path = "D:/6206/pythonProject1/net_length_20/net_DQA10505_DQB10602.txt"

data = pd.read_csv(file_path, sep="\t", header=None, skiprows=1)
data.columns = data.iloc[0]
data = data[1:]
data.reset_index(drop=True, inplace=True)
print(data)

print(data.columns)
print(data['Rank'].dtype)
data['Rank'] = pd.to_numeric(data['Rank'], errors='coerce')
print(data['Rank'].isna().sum())

filtered_data = data[(data['Rank'] > 60) & (~data['Peptide'].str.contains('X', na=False, case=False))]
print(filtered_data)

peptide_data = filtered_data[['Peptide']]


#peptide_data.to_csv('peptide_DRB1_110101.txt', index=False, header=True, sep='\t')
peptide_data.to_csv('peptide_DRB1_150101.txt', index=False, header=True, sep='\t')
#peptide_data.to_csv('peptide_HLA-DPA10103-DPB10401.txt', index=False, header=True, sep='\t')
#peptide_data.to_csv('peptide_HLA-DQA10102-DQB10602.txt', index=False, header=True, sep='\t')
#peptide_data.to_csv('peptide_HLA-DQA10102-DQB10301.txt', index=False, header=True, sep='\t')
#peptide_data.to_csv('peptide_HLA-DQA10505_DQB10301.txt', index=False, header=True, sep='\t')
#peptide_data.to_csv('peptide_HLA-DQA10505_DQB10602.txt', index=False, header=True, sep='\t')
print("New file 'peptide_only.txt' has been created.")