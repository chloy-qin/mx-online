from captcha.fields import CaptchaField
from django import forms
import redis
from mxonline.settings import REDIS_HOST, REDIS_PORT
from apps.users.models import UserProfile


class RegisterGetForm(forms.Form):
    captcha = CaptchaField()


class RegisterPostForm(forms.Form):
    mobile = forms.CharField(required=True, min_length=11, max_length=11)
    code = forms.CharField(required=True, min_length=4, max_length=4)
    password = forms.CharField(required=True)

    def clean_mobile(self):
        mobile = self.data.get('mobile')
        users = UserProfile.objects.filter(mobile=mobile)
        # 验证号码是否已经注册
        if users:
            raise forms.ValidationError('该手机号码已经注册')
        return mobile

    def clean_code(self):
        mobile = self.data.get('mobile')
        code = self.data.get('code')
        r = redis.Redis(host = REDIS_HOST, port = REDIS_PORT, db = 0, charset = 'utf8', decode_response =True )
        redis_code = r.set(str(mobile))
        if code != redis_code:
            raise forms.ValidationError('验证码不正确')
        return code


class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=2, max_length=20)
    password = forms.CharField(required=True, min_length=3, max_length=13)


class DynamicLoginForm(forms.Form):
    mobile = forms.CharField(required=True, min_length=11, max_length=11)
    captcha = CaptchaField()


class DynamicLoginPostForm(forms.Form):
    mobile = forms.CharField(required=True, min_length=11, max_length=11)
    code = forms.CharField(required=True, min_length=4, max_length=4)

    def clean_code(self):
        mobile = self.data.get('mobile')
        code = self.data.get('code')
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, charset='utf8', decode_responses=True)
        redis_code = r.get(str(mobile))
        if code != redis_code:
            raise forms.ValidationError('验证码不正确')
        return self.cleaned_data
