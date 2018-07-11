from django.conf.urls import url

from classview.views import my_decorator
from . import views
urlpatterns=[
    #将类视图转换成函数试图，并实现请求业务逻辑的分发
    url(r'^define_classview/$',views.DefineClassview.as_view()),
    #将在路由正则匹配中装饰类视图，本质是装饰类试图as_view()后的结果
    # url(r'^define_classview/$',my_decorator(views.DefineClassview.as_view()))
    url(r"^templatesview/$",views.TempalteModel.as_view()),
]