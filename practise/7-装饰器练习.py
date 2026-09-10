"""
写一个登陆装饰器对一个函数进行装饰，要求输入账号和密码才能运行该函数:

def run():
    print("开始执行...")
"""

def auth(usr,pwd):
    if usr == "" or pwd == "":
        raise ValueError("usr and pwd are required")
    if usr!= "abc" or pwd != "123":
        raise ValueError("usr and pwd are not valid")
    def inner(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return inner

@auth(usr="user",pwd="pass")
def run():
    print("开始执行...")

run()