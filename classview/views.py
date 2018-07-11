from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.http import HttpResponse,JsonResponse


# Create your views here
#模板的使用
class TempalteModel(View):
    def get(self,requst):
        context={
            'name':'BIG',
            'city':'Beijing',
            'alist':['ceshi','python','Django'],
            'dict1':{
                'python':'xiaobai'
            },
            'static':"KONG"

        }
        return render(requst,'index.html',context)
#定义类装饰器
def my_decorator(view_func):
    def wrapper(request,*args,**kwargs):
        print('类装饰器被调用')
        print(request.method,request.path)
        #调用被装饰的试图函数
        return view_func(request,*args,**kwargs)
    return wrapper

#定义类视图
#只对视图内的某些请求进行装饰，
# @method_decorator(my_decorator,name='get')
class DefineClassview(View):
    '''类视图的定义和使用'''
    #只装饰某些请求方法
    @method_decorator(my_decorator)
    def get(self,request):
        '''GET请求业务逻辑'''

        return HttpResponse('GET请求业务逻辑')
    def post(self,request):
        '''POST请求业务逻辑'''
        return HttpResponse('POST请求业务逻辑')