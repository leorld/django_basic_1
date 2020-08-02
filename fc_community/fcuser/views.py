from django.shortcuts import render
from .models import Fcuser
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

        if password != re_password:
            return HttpResponse('비밀번호가 다릅니다!')

        fcuser = Fcuser(
            username=username,
            password=password
        )
        # 입력받은 값으로 객체를 생성하고
        fcuser.save()
        # 생성한 객체를 데이터베이스에 저장

        return render(request, 'register.html')
