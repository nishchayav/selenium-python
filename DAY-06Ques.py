"""Question – Match, Search, Patterns, Meta-characters & Special Sequences
1. Uses re.match() to check whether a string starts with a valid employee ID in the format EMP followed by 3 digits (e.g., EMP123)
2. Uses re.search() to find the first occurrence of a valid email address in a given text
3. Demonstrates the use of meta-characters (., *, +, ?) and special sequences (\d, \w, \s) in the patterns
4. Prints matched groups using capturing parentheses"""


import re

# 1. re.match(): To check if string starts with valid employee ID (EMP followed by 3 digits)
employee_id = "EMP123 - John Doe"

match_emp = re.match(r"(EMP\d{3})", employee_id)
if match_emp:
    print("Valid Employee ID:", match_emp.group(1))
else:
    print("Invalid Employee ID")


# 2. re.search(): To find first valid email address in text
text = "Please contact us at support_team99@example.com for help."

email_match = re.search(r"(\w+@\w+\.\w+)", text)
if email_match:
    print("Email Found:", email_match.group(1))


# 3. Meta-characters & Special Sequences demonstration
pattern_demo = "User_01 logged in at 10:30 AM"

demo_match = re.search(r"(\w+_\d+)\s.*\s(\d+:\d+)", pattern_demo)
if demo_match:
    print("Username:", demo_match.group(1))
    print("Login Time:", demo_match.group(2))





'''Question – Assertions & Regular Expression Modifiers		
Write a Python program that:		
1. Validates a strong password using regular expressions with the following rules:		
Minimum 8 characters		
At least one uppercase letter		
At least one lowercase letter		
At least one digit		
At least one special character		
2. Uses lookahead assertions (?=)				
3. Uses regular expression modifiers such as:		
re.IGNORECASE		
re.MULTILINE		
re.DOTALL		
4. Demonstrates how modifiers affect pattern matching with examples		'''


import re

# 1️⃣ Strong password validation using lookahead assertions
password = input("enter your password: ")
pattern = r"""
^(?=.*[A-Z])        # at least one uppercase letter
 (?=.*[a-z])        # at least one lowercase letter
 (?=.*\d)           # at least one digit
 (?=.*[@$!%*?&])    # at least one special character
 .{8,}$             # minimum 8 characters
"""

if re.match(pattern, password, re.VERBOSE):
    print("Strong Password")
else:
    print("Weak Password")


# 2️⃣ IGNORECASE modifier demonstration
text_case = "Python is Powerful"
match_case = re.search(r"python", text_case, re.IGNORECASE)
print("IGNORECASE Match:", match_case.group() if match_case else "No Match")


# 3️⃣ MULTILINE modifier demonstration
text_multiline = """Hello World
Python Programming
Welcome"""

match_multiline = re.search(r"^Python", text_multiline, re.MULTILINE)
print("MULTILINE Match:", match_multiline.group() if match_multiline else "No Match")


# 4️⃣ DOTALL modifier demonstration
text_dotall = "Start\nEnd"
match_dotall = re.search(r"Start.*End", text_dotall, re.DOTALL)
print("DOTALL Match:", match_dotall.group() if match_dotall else "No Match")
