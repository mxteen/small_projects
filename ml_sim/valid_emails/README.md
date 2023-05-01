# Email Validator

This is a simple Python project that uses regular expressions to recognize valid emails.
The aim of this project was to optimize and improve the performance of the initial Python code for email validation by implementing various optimizations, ultimately resulting in a faster and more efficient implementation.

The original code used a for loop to iterate over a list of potential emails, applying a regular expression pattern to each one to determine if it was a valid email. The new implementation incorporated several optimizations to speed up this process.

Firstly, the regular expression pattern was precompiled outside of the function and passed in as an argument. This meant that the pattern was only compiled once, rather than every time the function was called, resulting in a significant performance boost.

Secondly, instead of using a for loop to append valid emails to a list, a list comprehension was used to create the list directly. List comprehensions are generally faster than for loops and can result in improved performance.

Lastly, the built-in filter() function was used to filter the list of strings based on the is_valid_email() function. This is generally faster than a for loop or list comprehension because it avoids creating a new list.

Overall, this project demonstrated how optimizations can be made to a Python implementation of email validation, resulting in a faster and more efficient implementation.



## Installation

To run this project, you need to have Python 3.x installed on your system.

## Usage

To use this email validator, you need to import the `validate_emails` function from `validate_email.py` file and call it with a list of strings that are supposed to be emails:

```python
from validate_email import validate_emails

emails = ["example@email.com", "invalid.email@.com", "anotherexample@email.com"]
valid_emails = validate_emails(emails)
print(valid_emails)
```

The `validate_emails` function will return a list of strings containing only the valid emails from the input list.

```python
["example@email.com", "anotherexample@email.com"]
```

If there are no valid emails in the input list, the function will return an empty list.

## Modules Used

This project uses the following modules:

- `re` - A module for working with regular expressions. In this project, regular expressions are used to match the email pattern.
- `typing` - A module for adding type hints to Python code. In this project, the `typing` module is used to specify the type of function arguments and return values.
