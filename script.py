import os
import pandas as pd

# Main function
def main():
    try:
        import clr
    except ImportError:
        print("PythonNET seems to be not installed! To install use 'pip install pythonnet'")
        os._exit(0)

    # Add references to required DLLs
    try:
        clr.AddReference(os.getcwd() + "\\Fraunhofer.IKTS.Drivers.dll")
        clr.AddReference(os.getcwd() + "\\Fraunhofer.IKTS.Libs.Services.dll")
    except Exception as e:
        print("Error while loading drivers binaries:", e)
        os._exit(0)

    # Load data from Excel file
    excel_file = "test_with cell_13.02.24.pcus 1 hour_exported_S0_C1.xlsx"
    data = pd.read_excel(excel_file)

    # Perform rapidmess with the loaded data
    rapidmess(data)

# Function to perform rapidmess
def rapidmess(data):
    # Your rapidmess code here
    # This function should handle the processing of the data
    # and any other operations you need to perform

    # For demonstration, let's print the first few rows of the loaded data
    print("First few rows of the loaded data:")
    print(data.head())

if __name__ == "__main__":
    main()
