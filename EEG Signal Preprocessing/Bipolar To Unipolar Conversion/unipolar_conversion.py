import pandas as pd

# Function to convert bipolar signals to unipolar (referential) using A1 as reference
def convert_bipolar_to_unipolar(bipolar_signals):
    # Assuming A1 as the reference and its voltage V(A1) is 0
    v_A1 = 0
    
    # Extract the bipolar signals from the input
    Fp2_F4 = bipolar_signals['Fp2-F4']
    F4_C4 = bipolar_signals['F4-C4']
    C4_P4 = bipolar_signals['C4-P4']
    P4_O2 = bipolar_signals['P4-O2']
    C4_A1 = bipolar_signals['C4-A1']
    
    # Step 1: Calculate unipolar values
    v_C4 = C4_A1 + v_A1  # V(C4) = C4-A1 + V(A1)
    v_F4 = F4_C4 + v_C4  # V(F4) = F4-C4 + V(C4)
    v_Fp2 = Fp2_F4 + v_F4  # V(Fp2) = Fp2-F4 + V(F4)
    v_P4 = v_C4 - C4_P4  # V(P4) = V(C4) - C4-P4
    v_O2 = v_P4 - P4_O2  # V(O2) = V(P4) - P4-O2
    
    # Step 2: Return the calculated unipolar values as a dictionary
    unipolar_signals = {
        'Fp2': v_Fp2,
        'F4': v_F4,
        'C4': v_C4,
        'P4': v_P4,
        'O2': v_O2
    }
    
    return unipolar_signals

# Read the bipolar signals from the CSV file
input_file = 'narco4_data.txt'  # Assuming narco1.csv contains the bipolar signals
bipolar_df = pd.read_csv(input_file)

# Initialize a list to store the unipolar signals for each row
unipolar_data = []

# Loop over each row in the dataframe to process the bipolar signals
for index, row in bipolar_df.iterrows():
    # Create a dictionary of the bipolar signals for this row
    bipolar_signals = {
        'Fp2-F4': row['1'],  
        'F4-C4': row['2'],   
        'C4-P4': row['3'],  
        'P4-O2': row['4'],   
        'C4-A1': row['5']   
    }
    
    # Convert the bipolar signals to unipolar
    unipolar_signals = convert_bipolar_to_unipolar(bipolar_signals)
    
    # Append the unipolar signals to the list
    unipolar_data.append(unipolar_signals)

# Create a DataFrame from the unipolar data
unipolar_df = pd.DataFrame(unipolar_data)

output_file = 'narco4_unipolar.csv'
unipolar_df.to_csv(output_file, index=False)

print(f"Unipolar signals have been saved to {output_file}")