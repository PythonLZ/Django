def my_middleware(get_response):
    #此处编写的代码在Django第一次配置和初始化的时候运行一次
    print('init被调用')
    def middleware(request):
        #代码会在每个请求处理视图前被调用
        print('before request 被调用')
        response = get_response(request)
        #代码会在每个请求处理视图后被调用
        print('after request 被调用')
        return response
    return middleware

#测试多个中间件的执行顺序
def my_middleware2(get_response):
    #代码在Django第一次配置和初始化的时候运行一次
    print('init2 被调用')
    def middleware(request):
        #代码会在每个请求处理试图前被调用
        print('my_middleware2 之前被调用')
        response=get_response(request)
        #代码会在每个请求处理视图后被调用
        print('my_middleware2 之后被调用')
        return response
    return middleware
