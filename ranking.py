import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# File paths (use raw strings `r` or double backslashes)
mixmhcpred_file = r"C:\Users\86180\Desktop\DRB1_150101.xlsx"
netmhcii_file = r"D:\net_DRB1_150101.txt"
output_file = r"C:\Users\86180\Desktop\combined_rank_DRB1_150101.xlsx"

try:
    # Load MixMHCpred data
    mixmhcpred_data = pd.read_excel(mixmhcpred_file, engine="openpyxl")

    # Load NetMHCIIpan data, skipping the first row
    netmhcii_data = pd.read_csv(netmhcii_file, sep="\t", header=0, skiprows=1)

    # Merge data on the 'Peptide' column
    merged_data = pd.merge(mixmhcpred_data, netmhcii_data, on="Peptide", how="inner")

    # Normalize the ranking scores
    scaler = MinMaxScaler()
    merged_data["MixMHCpred_Rank_norm"] = scaler.fit_transform(merged_data[["%Rank"]])
    merged_data["NetMHCIIpan_Rank_norm"] = scaler.fit_transform(merged_data[["Rank"]])

    # Calculate the combined score with adjustable weights
    w1, w2 = 0.5, 0.5  # Weights for MixMHCpred and NetMHCIIpan
    merged_data["Combined_Score"] = w1 * merged_data["MixMHCpred_Rank_norm"] + w2 * merged_data["NetMHCIIpan_Rank_norm"]

    # Sort by combined score and assign final ranks
    merged_data = merged_data.sort_values(by="Combined_Score", ascending=True)
    merged_data["Final_Rank"] = range(1, len(merged_data) + 1)

    # Save the results to an Excel file
    merged_data.to_excel(output_file, index=False)
    print(f"Combined ranking has been saved to: {output_file}")

except Exception as e:
    print(f"An error occurred: {e}")
