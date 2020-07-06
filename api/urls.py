from django.urls import path

from django.conf.urls import url
from rest_framework_jwt.views import ObtainJSONWebToken, obtain_jwt_token

from api import views

urlpatterns = [
    url(r"login/", ObtainJSONWebToken.as_view()),  # 无视图 直接获取token,需调掉as_view
    url(r"obt/", obtain_jwt_token),                # 无视图 直接获取token,无需调掉as_view
    path("user/", views.UserAPIV.as_view()),       # 通过user 获取 token
    path("check/", views.MoreLoginAPIView.as_view()),  # 多方式登录签发token
]
