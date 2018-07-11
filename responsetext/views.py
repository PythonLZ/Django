from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect

# Create your views here.
def onere(request):
    return HttpResponse("haha",content_type='string')

def twore(request):
    #创建响应对象
    respone = HttpResponse(content='itcast heima',status=400)
    #自定义响应头
    respone['itcast'] = 'python'


    respone.content='python'
    return respone
def jsonre(request):
    return JsonResponse({'A':'ITCAST','B':'HEIMA'})
def resp(request):
    return HttpResponse('测试一下')

#重定向
def demo_red(request):
    return redirect('/static/index.html')
#设置cookies
def setcook(request):
    response = HttpResponse('ok')
    response.set_cookie('python4','LZ',max_age=3600)
    response.set_cookie('python3','big')
    return response
def getcook(request):
    cookies1 = request.COOKIES.get('python4')
    print('cookes1=%s'%cookies1)
    return HttpResponse('cookies1=%s'%cookies1)
#设置session
def session_demo(request):
    #设置sessions
    request.session['name']='lz'
    #获取sessions
    name=request.session.get('name')
    print(name)
    return HttpResponse('OK')


