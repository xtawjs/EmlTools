# English Version | [中文版](./README.zh_cn.md)

## EML File Processing Tools

This project contains two Python scripts for processing `.eml` files. `eml_load.py` is used to extract attachments from `.eml` files and save them to a specified folder. `eml_read.py` is used to read basic information from `.eml` files (such as email subject, sender, recipient, CC, date, etc.) and export this information to a CSV file.

### Script Features

1. **eml_load.py**:
   - Traverse all `.eml` files in the current directory.
   - Extract attachments from each `.eml` file and save them to the `attachments` folder.
   - Attachments from each `.eml` file are saved in a subfolder named after the `.eml` file.
   - Supports handling non-ASCII characters in filenames and ensures unique filenames to avoid overwriting.
2. **eml_read.py**:
   - Traverse all `.eml` files in the current directory.
   - Extract basic information from each `.eml` file (such as email subject, sender, recipient, CC, date, etc.).
   - Export the extracted information to a CSV file named `emails_info.csv`.
   - The CSV file contains the following columns: Email Subject, Sender, Recipient, CC, Date, Attachment Names.

### Usage

1. Place `.eml` files in the same directory as the scripts.
2. Run `eml_load.py` to extract attachments.
3. Run `eml_read.py` to generate a CSV file containing email information.

### Dependencies

- Python 3.x
- Standard libraries: `os`, `glob`, `email`, `shutil`, `csv`

### Notes

- Ensure that the filenames of `.eml` files do not contain special characters to avoid path issues.
- If attachment filenames in `.eml` files are duplicated, the script will automatically append numbers to the filenames to avoid overwriting.