
# LEGB rule does not apply when new name bindings happen
text = "global text"
def outer_func():
  text = "enclosing text"
  def inner_func():
    text = "inner text"
    print('inner_func:', text)	
  print('outer_func:', text)	# 2. outer_func: enclosing text
  inner_func() #3. inner_func: inner text
  print('outer_func:', text)	# 4. outer_func: enclosing text
 
#using global
text_1 = "global text"
def outer_func_1():
  text_1 = "enclosing text"
  def inner_func_1():
  	global text_1	# binds the global text to the local text
  	text_1 = "inner text"
  	print('inner_func_1:', text_1)	# 03.inner_func: inner text
  print('outer_func_1:', text_1)	# 02.outer_func: enclosing text
  inner_func_1()
  print('outer_func_1:', text_1)	# 04.outer_func: enclosing text
 


text_2 = "global text"
def outer_func_2():
  text_2 = "enclosing text"
  def inner_func_2():
  	nonlocal text_2	# binds the local text to the enclosing text
  	text_2 = "inner text"
  	print('inner_func_2:', text_2)	# 003.inner_func: inner text
  print('outer_func_2:', text_2)	# 002.outer_func: enclosing text
  inner_func_2()
  print('outer_func_2:', text_2)	# 004.outer_func: inner text


if __name__=="__main__":
    print('global:', text)	# 1. global: global text
    outer_func() 
    print('global:', text)	# 5. global: global text
    
    print('##################')
    print('global:', text_1)	# 01. global: global text
    outer_func_1()
    print('global:', text_1)	# 05.global: inner text 


    print('##################')    
    print('global:', text_2)	# 001.global: global text
    outer_func_2()
    print('global:', text_2)	# global: global text