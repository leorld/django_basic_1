from django.shortcuts import render
from .models import Fcuser
from django.contrib.auth.hashers import make_password  # 암호화함수
from django.http import HttpResponse

# Create your views here.


def register(request):  # 함수를 url에 연결하면 request변수를 통해서 들어옴
    # template폴더를 이미 바라보고있기 때문에 그 안의 register.html로 바로 접근가능
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        re_password = request.POST['re-password']

        res_data = {}
        if password != re_password:
            res_data['error'] = "비밀번호가 다릅니다!"  # res_data의 error라는 키에 문자열을 삽입
        else:
            fcuser = Fcuser(
                username=username,
                password=make_password(password)  # 암호화해서 저장
            )
        # 입력받은 값으로 객체를 생성하고
            fcuser.save()
        # 생성한 객체를 데이터베이스에 저장

        # res_data가 html코드로 전달되고 res_data에 error가 있으면 메세지가 출력됨
        return render(request, 'register.html', res_data)
