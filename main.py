# EFFECTIVE PYTHON SUMMARY

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

# If you don’t expect the lengths of the lists passed to zip to be equal,
# consider using the zip_longest function from the itertools built-in module instead:

# Things to Remember

# ✦ The zip built-in function can be used to iterate over multiple iterators in parallel.
# ✦ zip creates a lazy generator that produces tuples, so it can be used on infinitely long inputs.
# ✦ zip truncates its output silently to the shortest iterator if you supply it with iterators of different lengths.
# ✦ Use the zip_longest function from the itertools
# built-in module if you want to use zip on iterators of unequal lengths without truncation.

# 1.5. Avoid else Blocks After for and while Loops

# WRONG
# a = 4
# b = 9
# for i in range ( 2 , min (a, b) + 1 ):
#     print ( 'Testing' , i)
#     if a % i == 0 and b % i == 0 :
#         print ( 'Not coprime' )
#         break
# else :
#     print ( 'Coprime' )


#BETTER

# def coprime(a,b):
#     for i in range(2, min(a,b) + 1):
#         if a % i ==0 and b % i ==0:
#             return False
#     return True


# print(coprime(4,9))
# print(coprime(3,6))
# assert coprime(4,9)
# assert not coprime(3,6)

# Things to Remember

# ✦ Python has special syntax that allows else blocks to immediately follow for and while loop interior blocks.
# ✦ The else block after a loop runs only if the loop body did not encounter a break statement.
# ✦ Avoid using else blocks after loops because their behavior isn’t intuitive and can be confusing.

 # 1.6. Prevent Repetition with Assignment Expressions
#

# def make_lemonade(count):
# ...
# def out_of_stock():
# ...
#
# fresh_fruit = {
# 'apple' : 10 ,
# 'banana' : 8 ,
# 'lemon' : 5 ,
# }
# #
# # counts = fresh_fruit.get("lemon", 0)
#
#
# if count := fresh_fruit.get( 'lemon' , 0 ):
#     make_lemonade(count)
# else :
#     out_of_stock()

# Things to Remember
# ✦ Assignment expressions use the walrus operator ( := ) to both assign and evaluate variable names in a single expression, thus reducing repetition.
# ✦ When an assignment expression is a subexpression of a larger expression, it must be surrounded with parentheses.
# ✦ Although switch/case statements and do/while loops are not available in Python,
# their functionality can be emulated much more clearly by using assignment expressions.

# 2. Lists and Dictionaries
#
# 2.1 Know How to Slice Sequences
# #
# Things to Remember
# ✦ Avoid being verbose when slicing: Don’t supply 0 for the start index or the length of the sequence for the end index.
# ✦ Slicing is forgiving of start or end indexes that are out of bounds, which means it’s easy to express slices on the front
# or back boundaries of a sequence (like a[:20] or a[-20:] ).
# ✦ Assigning to a list slice replaces that range in the original sequence with what’s referenced even if the lengths are different.


# 2.2 Avoid Striding and Slicing in a Single Expression

# x = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' ]
# x[:: 2 ]
# ['a', 'c', 'e', 'g'] x[:: 2 ] # ['h', 'f', 'd', 'b'] Here, ::2 means “Select every second item starting at the beginning.”
# Trickier, ::-2 means “Select every second item starting at the end and moving backward.” What do you think 2::2 means?
# What about 2::-2 vs. 2:2:-2 vs. 2:2:-2 ? Click here to view code image
# x[ 2 :: 2 ] #['c', 'e', 'g']
# x[ -2 :: -2 ] #['g', 'e', 'c', 'a']
# x[ -2 : 2 : -2 ] #['g', 'e']
# x[ 2 : 2 : 2 ] # []

# To prevent problems, I suggest you avoid using a stride along with start and end indexes.
# If you must use a stride, prefer making it a positive value and omit start and end indexes. If you must use a stride
# with start or end indexes, consider using one assignment for striding and another for slicing: Click here to view code image
# y = x[:: 2 ] # ['a', 'c', 'e', 'g']
# z = y[ 1 : 1 ] # ['c', 'e']

# Things to Remember
#
# ✦ Specifying start, end, and stride in a slice can be extremely confusing.
# ✦ Prefer using positive stride values in slices without start or end indexes. Avoid negative stride values if possible.
# ✦ Avoid using start, end, and stride together in a single slice. If you need all three parameters, consider doing two
# assignments (one to stride and another to slice) or using islice from the itertools built-in module.

# 2.3 Prefer Catch-All Unpacking Over Slicing
#

# To better handle this situation, Python also supports catch-all unpacking through a starred expression .
# This syntax allows one part of the unpacking assignment to receive all values that didn’t match any other part of the unpacking pattern.
# Here, I use a starred expression to achieve the same result as above without indexing or slicing:


# car_ages = [ 0 , 9 , 4 , 8 , 7 , 20 , 19 , 1 , 6 , 15 ]
#
# car_ages_descending = sorted(car_ages, reverse = True)
# #
# # oldest, second_oldest, *others = car_ages_descending
# # print (oldest, second_oldest, others)
#
# oldest, *others, youngest = car_ages_descending
# print (oldest, youngest, others)


# Things to Remember
# ✦ Unpacking assignments may use a starred expression to catch all values that
# weren’t assigned to the other parts of the unpacking pattern into a list.
# ✦ Starred expressions may appear in any position, and they will always become a
# list containing the zero or more values they receive.
# ✦ When dividing a list into non-overlapping pieces, catch-all unpacking is much less error prone than slicing and indexing.

# 2.4. Sort by Complex Criteria Using the key Parameter
#

# Things to Remember
# ✦ The sort method of the list type can be used to rearrange a list’s contents by the natural ordering of
# built-in types like strings, integers, tuples, and so on.
# ✦ The sort method doesn’t work for objects unless they define a natural ordering using special methods,
# which is uncommon.
# ✦ The key parameter of the sort method can be used to supply a helper function that returns the value to use
# for sorting in place of each item from the list .
# ✦ Returning a tuple from the key function allows you to combine multiple sorting criteria together.
# The unary minus operator can be used to reverse individual sort orders for types that allow it.
# ✦ For types that can’t be negated, you can combine many sorting criteria together by calling the sort method multiple times using
# different key functions and reverse values, in the order of lowest rank sort call to highest rank sort call.

# 2.5. Be Cautious When Relying on dict Insertion Ordering

# baby_names = {
# 'cat' : 'kitten' ,
# 'dog' : 'puppy' ,
# }
# print (baby_names)

# votes = {
# 'otter' : 1281 ,
# 'polar bear' : 587 ,
# 'fox' : 863 ,
# }
#
# def populate_ranks(votes, ranks):
#     names = list(votes.keys())
#     names.sort(key=votes.get, reverse=True)
#     for i, name in enumerate(names, 1):
#         ranks[name] = i
#
# def get_winner(ranks):
#     return next(iter(ranks))


# def get_winner(ranks):
#     for name, rank in ranks.items():
#         if rank == 1:
#             return name

#
# winner = get_winner(sorted_ranks)
# print (winner)
#
#
# ranks = {}
# populate_ranks(votes, ranks)
# print(ranks)
# winner = get_winner(ranks)
# print(winner)

    # Things to Remember
# ✦ Since Python 3.7, you can rely on the fact that iterating a dict instance’s
# contents will occur in the same order in which the keys were initially added.
# ✦ Python makes it easy to define objects that act like dictionaries but that aren’t dict instances.
# For these types, you can’t assume that insertion ordering will be preserved.
# ✦ There are three ways to be careful about dictionary-like
# classes: Write code that doesn’t rely on insertion ordering, explicitly check for the dict type at runtime,
# or require dict values using type annotations and static analysis.


#2.6. Prefer get Over in and KeyError to Handle Missing Dictionary Keys

# counters = {
# 'pumpernickel' : 2 ,
# 'sourdough' : 1 ,
# }
#
# key = "wheat"
# 1.way
# if key in counters:
#     count = counters[key]
# else :
#     count = 0
#
# counters[key] = count + 1
#2.way
# try :
#     count = counters[key]
# except KeyError:
#     count = 0
#
# counters[key] = count + 1
#
#3.way the RIGHT PYTHONIC WAY

# count = counters.get(key,0)
# counters[key] += count
# print(counters.items())

# data = {}
# key = 'foo'
# value = []
# data.setdefault(key, value)
# print ( 'Before:' , data)
# value.append( 'hello' )
# print ( 'After: ' , data)

# Things to Remember
# ✦ There are four common ways to detect and handle missing keys in dictionaries:
# using in expressions, KeyError exceptions, the get method, and the setdefault method.
# ✦ The get method is best for dictionaries that contain basic types like counters,
# and it is preferable along with assignment expressions when creating dictionary values has a high cost or may raise exceptions.
# ✦ When the setdefault method of dict seems like the best fit for your problem, you should consider using defaultdict instead.


# 2.7.Prefer default dict Over setdefault to Handle Missing Items in Internal State
#

# visits = {
# 'Mexico' : { 'Tulum' , 'Puerto Vallarta' },
# 'Japan' : { 'Hakone' },
# }
#
# visits.setdefault( 'France',set()).add('Arles')
#
# print(visits)
#
#
# if (japan := visits.get( 'Japan' )) is None : # Long
#     visits[ 'Japan'] = japan = set ()
# japan.add( 'Kyoto' )
# print (visits)
#
# Things to Remember
# ✦ If you’re creating a dictionary to manage an arbitrary set of potential keys, then you should prefer using a default dict instance
# from the collections built-in module if it suits your problem.
# ✦ If a dictionary of arbitrary keys is passed to you, and you don’t control its creation,
# then you, and you don’t control its creation,
# then you should prefer the get method to access its items. However,
# it’s worth considering using the setdefault method for
# the few situations in which it leads to shorter code.
#

# 2.8. Know How to Construct Key-Dependent Default Values with __missing__
#
# Things to Remember
# ✦ The setdefault method of dict is a bad fit when creating the default value has high
# computational cost or may raise exceptions.
# ✦ The function passed to defaultdict must not require any arguments, which makes it impossible to
# have the default value depend on the key being accessed.
# ✦ You can define your own dict subclass with a __missing__ method in order to construct default values that must know which key was being accessed.



# 3. FUNCTIONS

# 3.1. Never Unpack More Than Three Variables When Functions Return Multiple Values

# Things to Remember
# ✦ You can have functions return multiple values by putting them in a
# tuple and having the caller take advantage of Python’s unpacking syntax.
# ✦ Multiple return values from a function can also be unpacked by catch-all starred expressions.
# ✦ Unpacking into four or more variables is error prone and should be avoided;
# instead, return a small class or namedtuple instance.

# 3.1. Prefer Raising Exceptions to Returning None

# Things to Remember
# ✦ Functions that return None to indicate special meaning are error prone because
# None and other values (e.g., zero, the empty string) all evaluate to False in conditional expressions.
# ✦ Raise exceptions to indicate special situations instead of returning None .
# Expect the calling code to handle exceptions properly when they’re documented.
# ✦ Type annotations can be used to make it clear that a function will never return the value None , even in special situations.

# def careful_divided(a:float, b: float):
#     """ Divides a by b,
#     Raises:
#         ValueError: When the inputs cannot be divided
#     """
#     try:
#         return a/b
#     except ZeroDivisionError as e:
#         raise ValueError('Invalid Inputs')
#
#
# result = careful_divided(4,2)
# print(result)

# 3.2. Know How Closures Interact with Variable Scope
#
# def sort_priority(values, group):
#     def helper(x):
#         if x in group:
#             return 0, x
#         return 1, x
#     values.sort(key = helper)
#
# numbers = [ 8 , 3 , 1 , 2 , 5 , 4 , 7 , 6 ]
# group = { 2 , 3 , 5 , 7 }
#
# sort_priority(numbers, group)
# print(numbers)
#
# Things to Remember
# ✦ Closure functions can refer to variables from any of the scopes in which they were defined.
# ✦ By default, closures can’t affect enclosing scopes by assigning variables.
# ✦ Use the nonlocal statement to indicate when a closure can modify a variable in its enclosing scopes.
# ✦ Avoid using nonlocal statements for anything beyond simple functions.
#
# 3.3. Reduce Visual Noise with Variable Positional Arguments
#
# Things to Remember
# ✦ Functions can accept a variable number of positional arguments by using *args in the def statement.
# ✦ You can use the items from a sequence as the positional arguments for a function with the * operator.
# ✦ Using the * operator with a generator may cause a program to run out of memory and crash.
# ✦ Adding new positional parameters to functions that accept *args can introduce hard-to-detect bugs.
#
# 3.4. Provide Optional Behavior with Keyword Arguments
#
#Things to Remember
# ✦ Function arguments can be specified by position or by keyword.
# ✦ Keywords make it clear what the purpose of each argument is
# when it would be confusing with only positional arguments.
# ✦ Keyword arguments with default values make Things to Remember
# ✦ Function arguments can be specified by position or by keyword.
# ✦ Keywords make it clear what the purpose of each argument is when it would be confusing with only positional arguments.
# ✦ Keyword arguments with default values make it easy to add new behaviors
# to a function without needing to migrate all existing callers.
# ✦ Optional keyword arguments should always be passed by keyword instead of by position.
#
#3.5. Use None and Docstrings to Specify Dynamic Default Arguments

#Things to Remember
# ✦ A default argument value is evaluated only once:
# during function definition at module load time. This can cause odd behaviors for dynamic values
# (like {} , [] , or datetime.now() ).
# ✦ Use None as the default value for any keyword argument that has a dynamic value.
# Document the actual default behavior in the function’s docstring.
# ✦ Using None to represent keyword argument default values also works correctly with type annotations.

#3.6. Enforce Clarity with Keyword-Only and Positional-Only Arguments





























Brett Slatkin. Effective Python: 90 Specific Ways to Write Better Python, Second Edition (Nazeer Hussain Shaik's Library) (Kindle Locations 3187-3194).






























