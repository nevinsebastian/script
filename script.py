import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_data(data):
    plt.figure(figsize=(10, 6))

    for col in data.columns:
        if isinstance(col, str) and col.startswith('Samples'):
            plt.plot(data.index, np.abs(data[col]), label=col.split(':')[1].strip())

    plt.title('Sample Data Plot')
    plt.xlabel('Index')
    plt.ylabel('Absolute Value')
    plt.legend(loc='upper left')
    plt.grid(True)
    
    plt.tight_layout()
    plt.yscale('log')  # Set the y-axis scale to logarithmic
    plt.show()

def main():
    file_path = "test_with cell_13.02.24.pcus 1 hour_exported_S0_C1.xlsx"
    try:
        data = pd.read_excel(file_path, skiprows=118, header=None)
        data.dropna(inplace=True)
        plot_data(data)
    except Exception as e:
        print(f"Error processing data: {e}")

if __name__ == "__main__":
    main()
