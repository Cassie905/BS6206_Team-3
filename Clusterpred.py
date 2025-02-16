import pandas as pd


data = pd.read_excel('D:/6206/pythonProject1/foutput_15.xlsx')


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

grouped = data.groupby('BestAllele')
results = {}
for allele, group in grouped:
    peptide_list = group['Peptide'].tolist()
    merged_peptides = merge_peptides(peptide_list)
    changed_peptides = [peptide for peptide in merged_peptides if peptide not in peptide_list]
    changed_peptides_sorted = sorted(changed_peptides, key=len, reverse=True)
    results[allele] = changed_peptides_sorted

for allele, changed_peptides in results.items():
    if changed_peptides:
        output_file = f"{allele}_changed_peptides.txt"
        with open(output_file, 'w') as f:
            for peptide in changed_peptides:
                f.write(peptide + '\n')

        print(f"Changed peptides for {allele} saved to {output_file}.")