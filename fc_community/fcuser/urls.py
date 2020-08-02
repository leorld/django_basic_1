from django.urls import path
from . import views  # views.py 를 import

urlpatterns = [
    # views내의 register함수를 호출 -> register.html페이지 호출
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
]
