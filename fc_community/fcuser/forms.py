from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password


class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={'required': '아이디를 입력해주세요'},
        max_length=32, label="사용자 이름")
    password = forms.CharField(
        error_messages={'required': '비밀번호를 입력해주세요'},
        widget=forms.PasswordInput, label="비밀번호")

    def clean(self):  # 비밀번호 일치 여부
        cleaned_data = super().clean()  # super()로 부모클래스(기존의 form)의 clean()함수 호출
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            fcuser = Fcuser.objects.get(username=username)
            if not check_password(password, fcuser.password):
                self.add_error('password', '비밀번호를 틀렸습니다.')
                # 특정 필드에 error를 삽입하는 함수 add_error()
            else:
                self.user_id = fcuser.id
