# log-to-csv
Extract useful information from a log file, and print it to CSV files

This is the code for the final assignment of the course "Using Python to Interact with the Operating System" offered by Google through Coursera.
Unlike previous assignments, there were minimal guidance from the Instructor on this assignment. The log file is provided by the instructor.

Input:
syslog.log (put it in the same directory as the .py file)

The code/script has the following steps:
1. Extract relevant information with RegEx from the log file
2. Put the extracted data into two dictionaries (error and user statistics)
3. Sort the dictionaries according to the requirement (error: number of occurrence (descending), user statistics: alphabetical order (ascending))
3. Write them to CSVs

Output:
error_message.csv
user_statistics.csv

Extra:
There are assert statements and error raising statments throughout the code.
There are also tests files to check the correctness of the script.
