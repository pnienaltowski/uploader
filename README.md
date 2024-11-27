# GitHub File Uploader

This is a simple **GUI-based Python application** to upload files to a specified GitHub repository. The tool allows users to provide repository details, a file path, and a commit message, and then uploads the file to GitHub.

## Requirements

- Python 3.x
- Required Python libraries:
  - `tkinter`
  - `Pillow`
  - `github`
  - `os`
 
## Usage
- Clone or download the repository containing this script.
- Run the script using Python:
    `python script_name.py`
- Enter the following details in the GUI:
  - GitHub Token: Your personal access token for authentication.
  - Repository Name: The name of the repository  `username/repo`.
  - Branch: The branch to which the file will be uploaded `main`.
  - File Path: Use the "Browse" button to select the file.
  - Commit Message: Enter a meaningful message for the commit.
- Click the Upload button to upload the file.
- Use the Exit button to close the application.


## Example Workflow
- File Path Input:
  - Select a file using the "Browse" button, and the selected file's path will be displayed in the input field.

- Repository Details:
  - Repository: `username/repo_name`
  - Branch: `main` or `master`
- Commit Message:
  - Add a commit message.

- Upload to GitHub:
  - Click the Upload button to upload the file.
