# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data




def save_csv(csvpath, qualifying_loans):
    """Writes and saves data into a CSV file. 
    The CSV file is saved in the folder location that the end-user inputs.

    Args:
        csvpath (Path): The folder path where the CSV file must be saved.

    Returns:
        A CSV file which has the saved data.

    """
    header = ["Lender", "Max Loan Amount", "Max LTV", "Max DTI", "Min Credit Score", "Interest Rate"]
    with open(csvpath, "w", newline='') as csv_file:
        csvwriter = csv.writer(csv_file)

        # Write the headers in the CSV file
        csvwriter.writerow(header)
        
        # Write each qualifying loan in the CSV file
        for each_qualifying_loan in qualifying_loans:
            csvwriter.writerow(each_qualifying_loan)
    