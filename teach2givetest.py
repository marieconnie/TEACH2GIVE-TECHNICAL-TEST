# Question: 
# Write a query that will display the results below (Note: some columns might be renamed 
# but use the column names above). It should only show 2020 data and order by driver 
# points.

import sqlite3

# Connect to the SQLite database (replace 'database.db' with your database file)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Query to display results for the year 2020, ordered by driver points
query = """
SELECT driver_name AS Driver, 
       points AS Points,
       team_name AS Team
FROM race_results
WHERE year = 2020
ORDER BY points DESC;
"""

# Execute the query
cursor.execute(query)

# Fetch and print the results
results = cursor.fetchall()
for row in results:
    print(row)

# Close the database connection
conn.close()


# Question 2: Write a Python function that checks whether a word or phrase is palindrome or not.
def is_palindrome(s):
    # Remove spaces and convert to lowercase
    cleaned = ''.join(s.split()).lower()
    return cleaned == cleaned[::-1]

# Example
print(is_palindrome("A man a plan a canal Panama"))  


# Question 3: Write a Python function to check whether a string is pangram or not.
def is_pangram(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet <= set(s.lower())

# Example
print(is_pangram("Pack my box with five dozen liquor jugs"))  


# Question 4: Write a program that takes an integer as input and returns an integer with reversed digit ordering.
def reverse_integer(n):
    sign = -1 if n < 0 else 1
    reversed_num = int(str(abs(n))[::-1])
    return sign * reversed_num

# Example
print(reverse_integer(-1234))  

# Question 5: Write a program that accepts a string as input, capitalizes the first letter of each word in the string.
def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

# Example
print(capitalize_words("hello world from python"))  


