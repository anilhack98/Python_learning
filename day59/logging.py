import logging
def log_function_call(func):
    def decorated(*args,**kwargs):
        logging.info(f"Calling {func.__name__} with args={args},kwargs={kwargs}")
        return result
    return decorated
@log_function_call
def my_function(a,b):
    return a+b
print(my_function(5,10))