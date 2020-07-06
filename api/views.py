import re
#
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated  # 导入权限模块
from rest_framework_jwt.authentication import JSONWebTokenAuthentication  # 导入JWT模块
from api.serializers import UserModelSerializer  #导入反序列化器
from utils.response import APIResponse

# 获取token 两种url
class UserAPIV(APIView):
    permission_classes = [IsAuthenticated]  # 权限：只允许认证通过的用户访问   游客无权访问

    authentication_classes = [JSONWebTokenAuthentication]

    def get(self, request, *args, **kwargs):

        return APIResponse(results={"username": request.user.username})

# 多方式登录签发token
class MoreLoginAPIView(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        user_ser = UserModelSerializer(data=request.data)
        user_ser.is_valid(raise_exception=True)

        return APIResponse(data_message="成功", token=user_ser.token, results=UserModelSerializer(user_ser.obj).data)

