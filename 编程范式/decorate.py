# 修饰器
# #【1】
# def hello(fn):
#     def wrapper():
#         print("hello, %s" % fn.__name__)#fn.__name__就是函数fn的函数名字
#         fn()
#         print("goodbye, %s" % fn.__name__)
#     return wrapper#hello的结果是返回一个inner函数wrapper，相当于调用wrapper

# @hello
# def Hao():
#     print("I am Hao Chen")

# Hao()

'''
上面第10-14行代码就相当于运行
Hao=hello(Hao)
Hao()
output:
hello, Hao
I am Hao Chen
goodbye, Hao
'''

#【2】带参数的修饰器
# def makeHtmlTag(tag,*args,**kwds):
#     def real_decorator(fn):
#         css_class="class='{0}'".format(kwds["css_class"]) if "css_class" in kwds else ""

#         def wrapped(*args,**kwds):
#             return "<"+tag+css_class+">"+ fn(*args,**kwds)+"</"+tag+">"
#         return wrapped
#     return real_decorator

# @makeHtmlTag(tag="b",css_class="bold_css")
# @makeHtmlTag(tag="i",css_class="italic_css")
# def hello():
#     return "hello world"

# print(hello())

'''
上面第36-41行代码就相当于运行
hello=makeHtmlTag(makeHtmlTag(hello))
hello()
output:
<bclass='bold_css'><iclass='italic_css'>hello world</i></b>
'''

#【3】为其他函数加缓存
# from functools import wraps
# def memoization(fn):
#     cache={}#初始值，一个空字典
#     miss=object()#初始值，一个空object

#     @wraps(fn)
#     def wrapper(*args):
#         result=cache.get(args,miss)#取出args这个key，如果找不到则默认为miss
#         if result is miss:#如果真的找不到
#             result=fn(*args)#那么计算fib(args)
#             cache[args]=result#增加一个{"args":fib(args)}到字典cache中去
#         return result
#     return wrapper

# @memoization
# def fib(n):
#     if n<2:
#         return n
#     return fib(n-1)+fib(n-2)#递归，一个数据，等于前两个数据的和

# print(fib(5))
'''
首先fib=memoization(fib),即在运行fib的同时会运行memoization
然而调用memoization会返回wrapper，而wrapper=wraps(wrapper)
额，还是不太懂，但课程里面解释是：
由于当n不同时，实际上fib(n-1)和fib(n-2)会相等，那么f(3),f(2),f(1)在整个递归过程中计算了至少两次。
而这里的修饰器是在调用函数前先查询一下cache,如果没有找到才调用，如果有则直接从cache中返回值。
一下子，这个递归从二叉树式的递归成了线性的递归。
wraps的作用是保证fib的函数名不被wrapper所取代。
'''

#【4】类方式的decorator
class myDecorator(object):
    def __init__(self,fn):#它在给其他函数decorate的时候就会调用，即第93行
        print("inside myDecorator.__init__()")
        self.fn=fn

    def __call__(self):#在decorate的函数被调用的时候就会调用它，即第97行
        self.fn()
        print("inside myDecorator.__call__()")

@myDecorator
def aFunction():
    print("inside aFunction()")

print("Finished decorating aFunction()")

aFunction()#这里会先调用aFunction函数，再调用myDecorator.__call__
'''
inside myDecorator.__init__()
Finished decorating aFunction()
inside aFunction()
inside myDecorator.__call__()
'''