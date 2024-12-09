import pandas as pd
import sys


# Function to clean CSV
def clean_csv(input_file, output_file):
    try:
        # Load CSV into DataFrame
        df = pd.read_csv(input_file)

        # Remove rows with missing values or "-"
        cleaned_df = df.replace("-", pd.NA).dropna()

        # Save cleaned DataFrame to new CSV file
        cleaned_df.to_csv(output_file, index=False)

        print(f"Cleaned CSV file saved as: {output_file}")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python clean_csv.py <input_file.csv> <output_file.csv>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        clean_csv(input_file, output_file)
