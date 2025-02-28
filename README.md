You can find two py files and one .txt file in my test repository at the moment.
The first one named keyword_arguments.py
## is Rainfall Data Analysis
This Python script processes rainfall data for the last quarter. It prints the rainfall for each month, updates December's data, and calculates the total rainfall.

### Features:
- Use of Python dictionary to store and update data.
- Conditional logic to handle missing entries.
- Summation of values to display the total rainfall.

### How to Run:
1. Copy the code into a Python file (e.g., `rainfall.py`).
2. Run it using `python3 rainfall.py`.

______________________________________________________________________________________________________________________________________________________________________________________________

The other one is comes together called, log_in.py and log_in.txt

# Login System Simulation

This Python script is a simple **login system simulation**. It demonstrates fundamental programming concepts such as user input validation, loops, conditional logic, and file handling.

## Features
- **Username and Password Registration**: Users can register a username and password.
- **Login Verification**:
  - The script verifies the entered username against the stored username.
  - If the username doesn't match, users are prompted to try again.
  - Password validation ensures the correct password is entered before granting access.
- **Simulated User Interaction**: 
  - The program includes delays (`time.sleep`) to simulate real-time processing.
- **Data Storage**: 
  - Registered credentials (username and password) are stored in a text file, `data_log_in.txt`.

## How It Works
1. The user registers a username and password.
2. The program prompts the user to log in:
   - The username is checked first. If it doesn't match, the user is asked to retry.
   - Once the username is correct, the user is prompted to enter their password.
3. If both the username and password are valid, access is granted.
4. The credentials (username and password) are written to a file for storage and can be read back from it.
