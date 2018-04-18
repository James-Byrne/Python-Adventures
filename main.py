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
#     return map(lambda s: s.replace("’", "'").lstrip(digits).rstrip(), data)
#
# This has the advantage of only iterating over the array
# a single time and chains the function calls together
# so we don't need to assign temporary variables
def sanitize_data(data):
    step1 = map(trim_digits, data)
    step2 = map(trim_newlines, step1)
    return map(replace_apostrophes, step2)

# trip newlines from the string
# rstrip by default will strip all
# whitespace and newlines from the
# right of the string
def trim_newlines(str):
    return str.rstrip()

# trim leading digits from the
# string if they exist
def trim_digits(str):
    return str.lstrip(digits)

# Replace the apostrophes in the string
# where they exist
def replace_apostrophes(str):
    return str.replace("’", "'")

# We call the functions above here

# Get the file we want to read
file = get_file()

# Sanitize the data in the file
data = sanitize_data(load_data(file))

# Print the data to the console
list(map(print,data))
