import tabula
import pandas as pd

def extract_table(pages, pdf_path):
    """
    Extract tables from specified pages of a PDF file.
    
    Args:
    - pages (list): List of page numbers from which to extract tables.
    - pdf_path (str): Path to the PDF file.
    
    Returns:
    - pandas.DataFrame: Combined DataFrame containing tables from all specified pages.
    """
    extracted_tables = []
    for page_num in pages:
        # Read tables from the PDF
        tables = tabula.read_pdf(pdf_path, pages=page_num, lattice=True, silent=True)

        # Select the appropriate table from the extracted tables
        if page_num in [66, 72, 42, 62]:
            df = pd.DataFrame(tables[0])
        else:
            df = pd.DataFrame(tables[-1])

        # Add the extracted DataFrame to the list
        if pages[0] == 40:
            extracted_tables.append(df)
        else:
            extracted_tables.append(df.iloc[:, 2:])

    # Combine all extracted tables into a single DataFrame
    combined_df = pd.concat(extracted_tables, ignore_index=True)
    return combined_df

def process_foreign_tourism(pdf_path):
    """
    Process foreign tourism data from a PDF file and save it to a CSV file.
    
    Args:
    - pdf_path (str): Path to the PDF file containing foreign tourism data.
    """
    # Define groups of pages containing required tables
    page_groups = [[40, 41, 42], [54, 55, 56], [60, 61, 62], [63, 64, 65, 66], [69, 70, 71, 72]]
    extracted_data = []

    # Extract data from each group of pages
    for group in page_groups:
        extracted_data.append(extract_table(group, pdf_path))

    # Combine data from all groups into a single DataFrame
    combined_data = pd.concat(extracted_data, ignore_index=True, axis=1)

    # Define column names for the DataFrame
    column_names = ["Country of Nationality", "Arrivals", "1st quarter", "2nd quarter", "3rd quarter", "Female", "Male", "0-14", "15-24", "25-34", "35-44", "45-54", "55-64", "65 and above", "Not Reported", "Business and professional", "Indian Diaspora", "Leisure holiday and recreation", "Medical", "Student", "Others", "", "0-1 Days", "2-3 Days", "4-7 Days", "1-2 Weeks", "2-4 Weeks", ">1 Month", "Not known"]

    # Create a DataFrame with column names
    column_df = pd.DataFrame([column_names])
    
    # Combine column names DataFrame with the extracted data DataFrame
    final_df = pd.concat([column_df, combined_data], ignore_index=True)

    # Define output CSV path
    output_csv_path = "./output.csv"
    
    # Save the consolidated data to a CSV file
    final_df.to_csv(output_csv_path, index=False)
    print(f"Consolidated data saved to {output_csv_path}")

def main():
    # Path to the PDF file containing foreign tourism data
    pdf_path = "./India Tourism Statistics English 2022.pdf"
    
    # Process the foreign tourism data
    process_foreign_tourism(pdf_path)

if __name__ == "__main__":
    main()