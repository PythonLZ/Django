from django.conf.urls import url

from request_response import views

urlpatterns=[
    #正则组取值
    url(r"weather1/([a-z]+)/(\d{4})",views.weather1),
    #根据关键字取值
    url(r"weather2/(?P<city>[a-z]+)/(?P<year>\d{4})",views .weather2),
    #根据查询关键字取值
    url(r"weather3/(?P<city>[a-z]+)/(?P<year>\d{4})",views.weather3),
    #演示获取请求体中的表单数据
    url(r"^get_body_form/$",views.get_body_form),
    #演示获取请求体中的非表单数据
    url(r"^get_body_json/$",views.get_body_json)

]