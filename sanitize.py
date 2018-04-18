from string import digits

# This function will take a file and
# return a list containing all of the
#lines inside the file
def load_data(file):
    return file.readlines()

# This function will find the file and open
# it for reading
def get_file():
    return open('sentences.txt', 'r')

# This function will sanatize the data
# from the file in 3 steps
# 1 - Remove trailing newlines and whitespace to the right
# 2 - Remove leading digits if they exist
# 3 - Replace apostrophes with the correct ones
#
# Note that this function could be implemented much
# more tersely and effieciently like:
#
# def sanitize_data(data)
#     return [lambda s: s.replace("’", "'").lstrip(digits).rstrip() for x in data]
#
# This has the advantage of only iterating over the array
# a single time and chains the function calls together
# so we don't need to assign temporary variables
def sanitize_data(data):
    step1 = [trim_digits(x) for x in data]
    step2 = [trim_newlines(x) for x in step1]
    return [replace_apostrophes(x) for x in step2]

# trip newlines from the string
# rstrip by default will strip all
# whitespace and newlines from the
# right of the string
def trim_newlines(str):
    return str.rstrip()

# trim leading digits from the
# string if they exist
def trim_digits(str):
    return str.lstrip(digits).lstrip()

# Replace the apostrophes in the string
# where they exist
def replace_apostrophes(str):
    return str.replace("’", "'")
