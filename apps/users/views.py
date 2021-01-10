import redis
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import View
from mxonline.settings import yp_apikey, REDIS_HOST, REDIS_PORT
from apps.users.forms import LoginForm, DynamicLoginForm, DynamicLoginPostForm
from apps.users.forms import RegisterGetForm, RegisterPostForm
from apps.users.models import UserProfile
from apps.utils.YunPian import send_single_sms
from apps.utils.random_str import generate_random


class RegisterView(View):

    def get(self, request, *args, **kwargs):
        register_get_form = RegisterGetForm()
        return render(request, 'register.html', {'register_get_form ': register_get_form})

    def post(self, request, *args, **kwargs):
        register_post_form = RegisterPostForm(request.POST)
        if register_post_form.is_valid():
            mobile = RegisterPostForm.clean_data['mobile']
            password = RegisterPostForm.clean_data('password')
            # 新建一个用户
            user = UserProfile(username=mobile)
            user.set_password(password)
            user.mobile = mobile
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            register_get_form = RegisterGetForm()
            return render(request, 'register.html', {'register_get_form': register_get_form,
                                                     'register_post_form': register_post_form})


class DynamicLoginView(View):
    def post(self, request, *args, **kwargs):
        login_form = DynamicLoginPostForm(request.POST)
        dynamic_login = True
        if login_form.is_valid():
            # 没有账号动态验证码登录，也可以登录
            mobile = DynamicLoginPostForm.cleaned_data['mobile']
            existed_users = UserProfile.objects.filter(mobile=mobile)
            if existed_users:
                user = existed_users[0]
            else:
                user = UserProfile(username=mobile)
                password = generate_random(10, 2)
                user.set_password(password)
                user.mobile = mobile
                user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            dynamic_form = DynamicLoginForm()
            return render(request, 'login.html', {'login_form': login_form,
                                                  'dynamic_form': dynamic_form,
                                                  'dynamic_login': dynamic_login})


class SendSmsView(View):
    def post(self, request, *args, **kwargs):
        send_sms_form = DynamicLoginForm(request.POST)
        re_dict = {}
        if send_sms_form.is_valid():
            mobile = DynamicLoginForm.cleaned_data['mobile']
            # 随机生成数字验证码
            code = generate_random(4, 0)
            re_json = send_single_sms(yp_apikey, code, mobile=mobile)
            if re_json['code'] == 0:
                re_dict['status'] = 'success'
                r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, charset='utf8', decode_responses=True)
                r.set(str(mobile), code)
                r.expire(str(mobile), 60 * 5)  # 设置验证码过期时间五分钟
            else:
                re_dict['msg'] = re_json('msg')
        else:
            for key, value in send_sms_form.errors.items():
                re_dict[key] = value
        return JsonResponse(re_dict)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))
        login_form = DynamicLoginForm()
        return render(request, 'login.html', {
            'login_form': login_form
        })

    def post(self, request, *args, **kwargs):
        # user_name = request.POST.get('username', '')
        # pass_word = request.POST.get('password', '')
        # 表单验证
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            pass_word = login_form.cleaned_data['password']

            # 如果用引入user的方法有两个问题：1.通过用户名检查用户不合理；2.密码是加密的，需要加密后对比
            # from  apps.users.models import UserProfile
            # user = UserProfile.objects.get(user_name = user_name, pass_word = pass_word)
            # 用于通过用户名和密码判断用户是否存在
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                # 查询到用户
                login(request, user)
                # 登录成功，返回首页
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误', 'login_form': login_form})
        else:
            return render(request, 'login.html', {'login_form': login_form})
