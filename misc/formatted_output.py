'''
 string modulo "%" is still available in Python3. But it is very likely that one day this old style of formatting will be removed from the language. So you should get used to str.format().

 The general syntax for a format placeholder is %[flags][width][.precision]type
'''
#format string    %(string modulo operator)  Tuple with values
print("art:%5d,Price per Unit:%8.2f" % (453,59.098))
print("%5.4x"% (47))
print("Only one percentage sign: %% " % ())

print("%#5X"% (47)) #using flags - # : 	Used with o, x or X specifiers the value is preceded with 0, 0o, 0O, 0x or 0X respectively.
s = "Price: $ %8.2f"% (356.08977)
print(s)

#The pythonic way: the string method "format"
'''
 |  format(...)
 |      S.format(*args, **kwargs) -> str
 |
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |
'''
print("First argument: {0}, second one: {1}".format(47,11) )
print("Second argument: {1}, first one: {0}".format(47,11) )
print("various precisions: {0:6.2f} or {0:6.3f}".format(1.4148))
print( "First argument: {}, second one: {}".format(47,11) )
print("The capital of {0:s} is {1:s}".format("Ontario","Toronto"))#We could have used empty curly braces in the previous example!
print("The capital of {province} is {capital}".format(province="Ontario",capital="Toronto"))#keyword parameters

data = dict(province="Ontario",capital="Toronto")#using a dictionary
#The double "*" in front of data turns data automatically into the form 'province="Ontario",capital="Toronto"'.
print("The capital of {province} is {capital}".format(**data))

capital_country = {"United States" : "Washington",
                   "US" : "Washington",
                   "Canada" : "Ottawa",
                   "Germany": "Berlin",
                   "France" : "Paris",
                   "England" : "London",
                   "UK" : "London",
                   "Switzerland" : "Bern",
                   "Austria" : "Vienna",
                   "Netherlands" : "Amsterdam"}
print("Countries and their capitals:")
for c in capital_country:
    print("{country}: {capital}".format(country=c, capital=capital_country[c]))

print("Countries and their capitals using a dictionary:")
for c in capital_country:
    format_string = c + ": {" + c + "}"
    print(format_string.format(**capital_country))

#Using Local Variable Names in "format"
#locals()
#a= 34, b = 43,  def f: return 3344
#print("a={a}, b={b} and f={f}".format(**locals()))

'''
The string class contains further methods, which can be used for formatting purposes as well: ljust, rjust, center and zfill
'''
#formatted string literals
'''
Python 3.6 introduces formatted string literals. They are prefixed with an 'f'. The formatting syntax is similar to the format strings accepted by str.format(). Like the format string of format method, they contain replacement fields formed with curly braces. The replacement fields are expressions, which are evaluated at run time, and then formatted using the format() protocol.
'''
#price = 11.12
 #f"Price in Euro: {price}"
