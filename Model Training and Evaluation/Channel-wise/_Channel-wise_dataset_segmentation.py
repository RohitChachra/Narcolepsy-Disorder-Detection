import pandas as pd

# Input and output
input_file = "Narcolepsy_dataset.csv"
output_files = {
    0: "Fp2_dataset.csv",
    1: "F4_dataset.csv",
    2: "C4_dataset.csv",
    3: "P4_dataset.csv",
    4: "O4_dataset.csv"
}

# Load dataset
df = pd.read_csv(input_file)

# Always keep these
base_cols = ["subject_id", "epoch", "label"]

# Process each channel
for ch, out_file in output_files.items():
    # Select columns that belong to this channel
    ch_cols = [col for col in df.columns if col.endswith(f"_{ch}")]
    
    # Create new dataframe for this channel
    channel_df = df[base_cols + ch_cols]
    
    # Save to CSV
    channel_df.to_csv(out_file, index=False)
    print(f"Saved {out_file} with {channel_df.shape[1]} columns")
