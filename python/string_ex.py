# Define new string
# Single line
company_company_name = 'Sale Stock'
# Multiline
description = '''
Sale Stock Pte, Ltd is a fast-growing multinational tech start up company 
that is currently specialising in mobile-commerce.
'''
mission = ('Giving access to affordable,'
    ' high-quality clothes to everyone who needs it.')

# String operations
# Get the sub-string
print company_name[0] # Output: S
company_name[5:] # Output: Stock
# Concatenation
company_name + ' Engineering' # Output: Sale Stock Engineering
# 

# Returns the length of the string
company_name_len = len(company_name)
# Converts to lowercase
company_name_lower = company_name.lower()
# Converts to uppercase
company_name_upper = company_name.upper()

# Output
print 'company_name:', company_name
print 'company_name_len:', company_name_len
print 'company_name_lower:', company_name_lower
print 'company_name_upper:', company_name_upper
print 'company_name_split:', company_name_split
print 'company_name_sub:', company_name_sub
