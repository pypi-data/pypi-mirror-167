# encoding: utf-8
"""
@project: djangoModel->user_list
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis: 用户信息列表
@created_time: 2022/7/25 9:42
"""
from rest_framework.views import APIView

from xj_role.services.group_service import GroupService
from ..services.user_service import UserService
from ..utils.custom_response import util_response
from ..utils.custom_tool import is_number
from ..utils.model_handle import parse_data


class UserListAPIView(APIView):
    # 在有的框架中会出现传入3个参数的问题，原因不明，可能和两边使用的版本不同有关
    def get(self, request, *args):
        # token验证
        token = request.META.get('HTTP_AUTHORIZATION', None)
        token_serv, error_text = UserService.check_token(token)
        if error_text:
            return util_response(err=6045, msg=error_text)

        params = parse_data(request)

        # 分组筛选用户ID
        user_group_id = params.pop("user_group_id", None)
        if user_group_id and is_number(user_group_id):
            id_list, err = GroupService.get_user_from_group(user_group_id)
            params.setdefault("id_list", id_list)

        # 获取数据
        data, err_txt = UserService.user_list(params)
        if not error_text:
            return util_response(data=data)
        return util_response(err=47767, msg=error_text)
