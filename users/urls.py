from django.conf.urls import url
from . import views

urlpatterns=[
    # url(r"^index/$",views.index)
    #以下代码演示路由自上而下匹配规则
    # url(r"^say",views.say),
    # url(r"^sayhello",views.sayhello),
    #命名空间路由
    url(r"^index/$",views.index,name='index'),
    #正确的
    url(r'^say/$',views.say),
    url(r"^sayhello/$",views.sayhello),

]
