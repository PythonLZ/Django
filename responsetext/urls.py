from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^responsetext/onere/$',views.onere),
    url(r"^responsetext/twore/$",views.twore),
    url(r'^responsetext/jsonre/$',views.jsonre),
    url(r'^responsetext/resp/$',views.resp),
    url(r'^responsetext/demo_red/$',views.demo_red),
    #设置cookies路由
    url(r'^responsetext/setcook/$',views.setcook),
    #获取cookies
    url(r'^responsetext/getcook/$',views.getcook),
    #设置sessions
    url(r'^responsetext/session_demo/$',views.session_demo)
]