from django.urls import path
from . import views  # views.py 를 import

urlpatterns = [
    # views내의 register함수를 호출 -> register.html페이지 호출
    path('list/', views.board_list),
    path('write/', views.board_write),
    path('detail/<int:pk>', views.board_detail),
    # 숫자가 pk 변수값으로 int형태로 들어오면서 views의 board_detail함수에서 받음
]
