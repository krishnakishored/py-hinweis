#####################################################################

'''
1. Simple decorators
Note how the decorating ... print statement appears when the function is defined, 
not when it is invoked. This is because Python calls the decorator function at the time the decorated function is declared. 
This decorator doesn't do anything, so obviously my_function() is unaffected by it and can be called as usual.
'''
def my_decorator(f):
    print('decorating', f)
    return f

@my_decorator
def my_function(a,b):
    return a+b

'''
2. Decorators that replace the decorated function
    - return a different function
    - Almost always, these decorators are implemented with inner functions
'''

def forty_two():
    return 42

def my_decorator_2(f):
    print('decorating', f)
    return forty_two

@my_decorator_2
def my_function_2(a,b): 
    return a+b



'''
3.  the returned function should act as a wrapper for the original function, not as a complete replacement.
'''

def my_decorator_3(f):
    # def wrapped(): # TypeError: wrapped() takes 0 positional arguments but 2 were given
    #     return f(1,2)
    def wrapped(*args,**kwargs):
        print('before function')
        response = f(*args,**kwargs)
        print('after function')
        return response
    print('decorating', f)
    return wrapped

@my_decorator_3
def my_function_3(a,b):
    # print('in function')
    return a+b
#####################################################################
# examples

# 1. injecting new arguments

from datetime import datetime

def add_current_time(f):
    def wrapped(*args,**kwargs):
        return f(datetime.utcnow(),*args,**kwargs)
    return wrapped

@add_current_time
def test_1(time,a,b): 
    print(f'I received args {a}, {b} at {time}')

# 2. Altering the Return Value of a Function
'''
The wrapped() function simply invokes the original function, called f in this context,
and then checks if the return value is a dictionary or list, in which case it calls jsonify(), 
effectively intercepting and fixing the return value before it is returned to the framework.
'''
def to_json(f):
    def wrapped(*args, **kwargs):
        response = f(*args, **kwargs)
        if isinstance(response, (dict,list)):
            response = jsonify(response)
        return response
    return wrapped


# 3. Validation 
''' 
A very common example in a web application is to authenticate the user. 
If the validation/authentication task ends in a failure, 
then the decorated function is not invoked, and instead the decorator raises an error
'''
ADMIN_TOKEN = 'my-secret-token'

def only_admins(f):
    def wrapped(*args,**kwargs):
        token = request.headers.get('X-Auth-Token')
        if token != ADMIN_TOKEN:
            abort(401) # not authorized
        return f(*args,**kwargs)
    return wrapped
'''
$ curl -H "X-Auth-Token: my-secret-token" http://localhost:5000/admin
   only admins can access this route% 
'''
#####################################################################
from flask import Flask, request, jsonify, abort

app = Flask(__name__)
all_request_loggers = []

def request_logger(f):
    all_request_loggers.append(f)
    return f

''' using the decorator allows the application to decouple the view function 
from the function or functions registered to log requests, which is a good design practice.'''
def invoke_request_loggers(request):
    for logger in all_request_loggers:
        logger(request)

@request_logger
def log_a_request(request):
    print(f"method:{request.method}, path: {request.path} ")        

@app.route('/')
def index():
    invoke_request_loggers(request)
    return "Hello World!"

# # AssertionError: View function mapping is overwriting an existing endpoint function: wrapped
# @app.route('/jsonify')
# @to_json
# def index_2():
#     return {'hello':'world'}    
#     # return jsonify({'hello': 'world'})
# # As of Flask version 1.1 you can, in fact, return a dictionary, and Flask automatically converts it to JSON.

@app.route('/admin')
@only_admins
def admin_route():
    return "only admins can access this route"



#####################################################################
if __name__ == "__main__":
    # app.run()    
    # print(my_function(6,8))
    # # print(my_function_2(6,8)) # TypeError: forty_two() takes 0 positional arguments but 2 were given
    # print(my_function_2()) # 42 -  my_function is now an alias to forty_two
    # print(my_function_3(7,9)) # 16

    # # the decorated function is written to accept a first time argument, but this argument is automatically added by the decorator, 
    # test_1(1,100) # I received args 1, 100 at 2019-10-29 09:59:29.643699


    app.run()