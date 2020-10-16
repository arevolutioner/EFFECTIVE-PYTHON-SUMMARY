# EFFECTIVE-PYTHON-SUMMARY
This book's summary provides insight into the Pythonic way of writing programs: the best way to use Python. It builds on a fundamental understanding of the language that I assume you already have. Novice programmers will learn the best practices of Python’s capabilities. 

Brett Slatkin. Effective Python: 90 Specific Ways to Write Better Python, Second Edition (Nazeer Hussain Shaik's Library) (Kindle Locations 229-231). 

 EFFECTIVE PYTHON SUMMARY

# 1.PYTHONIC THINKING

# 1.1. Know the Differences Between bytes and str
#
#To convert Unicode data to binary data, you must call the encode method of str .
#To convert binary data to Unicode data, you must call the decode method of bytes .


# ✦ bytes contains sequences of 8-bit values, and str contains sequences of Unicode code
# points.
# ✦ Use helper functions to ensure that the inputs you operate on are the type of character sequence that you
# expect (8-bit values, UTF-8-encoded strings, Unicode code points, etc).
# ✦ bytes and str instances can’t be used together with operators (like > , == , + , and % ).
# ✦ If you want to read or write binary data to/from a file, always open the file using a binary mode
# (like 'rb' or 'wb' ).
# ✦ If you want to read or write Unicode data to/from a file, be careful about your system’s
# default text encoding. Explicitly pass the encoding parameter to open if you want to avoid surprises.

# 1.2. Prefer Interpolated F-Strings Over C-style Format Strings and str.format
#
# f_string = f'{key:<10} = {value:.2f}'
# c_tuple = '%-10s = %.2f' % (key, value)
# str_args = '{:<10} = {:.2f}' . format (key, value)
#
#
# str_kw = '{key:<10} = {value:.2f}' . format (key = key,
# value = value)
# c_dict = '%(key)-10s = %(value).2f' % { 'key' : key,
# 'value' : value}
# assert c_tuple == c_dict == f_string
# assert str_args == str_kw == f_string

# Things to Remember
# ✦ C-style format strings that use the % operator suffer from a variety of gotchas and verbosity problems.
# ✦ The str.format method introduces some useful concepts in its formatting
# specifiers mini language, but it otherwise repeats the mistakes of C-style format strings and should be avoided.
# ✦ F-strings are a new syntax for formatting values into strings that solves the biggest problems with
# C-style format strings.
# ✦ F-strings are succinct yet powerful because they allow for arbitrary Python expressions to be
# directly embedded within format specifiers.
#

# 1.3. Write Helper Functions Instead of Complex Expressions
#
# green_str = my_values.get( 'green' , [ '' ])
# if green_str[ 0 ]:
# green = int (green_str[ 0 ])
# else :
# green = 0
#
# def get_first_int(values, key, default = 0 ):
# found = values.get(key, [ '' ])
# if found[ 0 ]:
# return int (found[ 0 ])
# return default

# Things to Remember
# ✦ Python’s syntax makes it easy to write single-line expressions that are overly complicated and difficult to read.
# ✦ Move complex expressions into helper functions, especially if you need to use the same logic repeatedly.
# ✦ An if / else expression provides a more readable alternative to using the Boolean operators or and and in expressions.


# 1.3. Prefer Multiple Assignment Unpacking Over Indexing
#
# The values in tuples can be accessed through numerical indexes: \
# item = ( 'Peanut butter' , 'Jelly' )
# first = item[ 0 ]
# second = item[ 1 ]
# print (first, 'and' , second)

# item = ( 'Peanut butter' , 'Jelly' )
# first, second = item # Unpacking
# print (first, 'and' , second)

# Things to Remember
# ✦ Python has special syntax called unpacking for assigning multiple values in a single statement.
# ✦ Unpacking is generalized in Python and can be applied to any iterable, including many levels of iterables within iterables.
# ✦ Reduce visual noise and increase code clarity by using unpacking to avoid explicitly indexing into sequences.


# 1.4. Prefer enumerate Over range


# flavor_list = [ 'vanilla' , 'chocolate' , 'pecan' , 'strawberry' ]
# for flavor in flavor_list:
# print ( f'{flavor} is delicious' )
#
#
# for i in range (len(flavor_list)):
# flavor = flavor_list[i]
# print(f'{i + 1}:{flavor}')
#
# it = enumerate(flavor_list)
# print(next(it))
#
# print(next(it))


# Things to Remember
# ✦ enumerate provides concise syntax for looping over an iterator and getting the index of each item from the iterator as you go.
# ✦ Prefer enumerate instead of looping over a range and indexing into a sequence.
# ✦ You can supply a second parameter to enumerate to specify the number from which to begin counting (zero is the default).


# 1.5. Use ZIP to Process Iterators in Parallel

# names = ["Cecilia", "Lise", "Marie"]
# counts = [len(n) for n in names]
#
# longest_name = None
# max_count = 0
# for i in range(len(names)):
#     count = counts[i]
#     if count > max_count:
#         longest_name = names[i]
#         max_count = count
#
# print(longest_name)

#The problem is that this whole loop statement is visually noisy.

# To make this code clearer, Python provides the zip built-in function.
# zip wraps two or more iterators with a lazy generator.


# names = ["Andrey", "Blagovesta", "Boris", "Georgy"]
# counts = [len(n) for n in names]
#
# longest_name = None
# max_count = 0
#
# for name, count in zip(names, counts):
#     if count > max_count:
#         longest_name = name
#         max_count = count

# print(longest_name)
