import json
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#weahter  city  year
#演示获取请求体中非标单数据
def get_body_json(request):
    #读取原非表单数据
    #读取json字符串的二进制信息
    json_str = request.body
    #将json二进制信息转换成字符串
    json_str = json_str.decode()
    #将json_str转换成字典
    json_data = json.loads(json_str)
    print(json_data['a'])
    print(json_data['b'])
    return HttpResponse('OK')


#演示获取请求体中的表单数据
def get_body_form(request):
    a = request.POST.get('a')
    b = request.POST.get('b')
    a_list = request.POST.getlist('a')
    print(a)
    print(b)
    print(a_list)
    return HttpResponse('ok')
#根据正则中的组提取参数
#未命名的参数按定义顺序传递
def weather1(request,city,year):
    print("city=%s"%city)
    print('year=%s'%year)
    return HttpResponse('OK')
#命名参数按名字传递，根据关键字提取参数

def weather2(request,year,city):
    print("city=%s"%city)
    print('year=%s'%year)
    return HttpResponse('ok')
# /weather3/beijing/2018/?a=10&b=20&a=30
#根据查询字符串获取参数
def weather3(requset,year,city):
    print('city=%s' %city)
    print('year=%s' %year)
    a = requset.GET.get('a')
    b = requset.GET.get('b')
    a_list = requset.GET.getlist('a')
    print(a,b,a_list)
    return HttpResponse('ok')