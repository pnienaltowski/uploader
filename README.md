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
1. Clone or download the repository containing this script.
2. Run the script using Python:
    python script_name.py
3. Enter the following details in the GUI:
- GitHub Token: Your personal access token for authentication.
- Repository Name: The name of the repository (e.g., username/repo).
- Branch: The branch to which the file will be uploaded (e.g., main).
- File Path: Use the "Browse" button to select the file.
- Commit Message: Enter a meaningful message for the commit.
4. Click the Upload button to upload the file.
5. Use the Exit button to close the application.


## Example Workflow
1. File Path Input:
Select a file using the "Browse" button, and the selected file's path will be displayed in the input field.

2. Repository Details:
Provide the GitHub repository details:

3. Repository: username/repo_name
Branch: main or master
Commit Message:
Add a commit message like Add new feature or Update script.py.

4. Upload to GitHub:
Click the Upload button to upload the file.
