from django.shortcuts import render

# Create your views here.


def register(request):  # 함수를 url에 연결하면 request변수를 통해서 들어옴
    # template폴더를 이미 바라보고있기 때문에 그 안의 register.html로 바로 접근가능
    return render(request, 'register.html')
