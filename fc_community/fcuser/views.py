from django.shortcuts import render
from .models import Fcuser
from django.contrib.auth.hashers import make_password, check_password  # 비밀번호 암호화함수, 확인함수
from django.http import HttpResponse

# Create your views here.


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)

        res_data = {}
        if not (username and password):
            res_data['error'] = 'ID와 비밀번호를 다시 확인해주세요.'
        else:
            # 모델 호출 objects.get(조건) // 조건 앞 변수 : 모델 , 뒷 변수 : 입력받은 내용
            fcuser = Fcuser.objects.get(username=username)
            if check_password(password, fcuser.password):
                # 비밀번호가 일치, 로그인 처리
                res_data['error'] = '로그인되었습니다.'
                pass
            else:
                res_data['error'] = '비밀번호를 틀렸습니다.'
        return render(request, 'login.html', res_data)


def register(request):  # 함수를 url에 연결하면 request변수를 통해서 들어옴
    # template폴더를 이미 바라보고있기 때문에 그 안의 register.html로 바로 접근가능
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        # 딕셔너리 형태이므로 get함수를 사용하여 빈 문자열일때 None 초기값 설정
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}

        if not(username and useremail and password and re_password):
            res_data['error'] = "모든 값을 입력하세요."
        elif password != re_password:
            res_data['error'] = "비밀번호가 다릅니다!"  # res_data의 error라는 키에 문자열을 삽입
        else:
            fcuser = Fcuser(
                username=username,
                useremail=useremail,
                password=make_password(password)  # 암호화해서 저장
            )
        # 입력받은 값으로 객체를 생성하고
            fcuser.save()
        # 생성한 객체를 데이터베이스에 저장

        # res_data가 html코드로 전달되고 res_data에 error가 있으면 메세지가 출력됨
        return render(request, 'register.html', res_data)
