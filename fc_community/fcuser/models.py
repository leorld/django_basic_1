from django.db import models

# Create your models here.


class Fcuser(models.Model):
    # verbose_name 으로 필드 명명(admin 등에서 참조할 때 username이 아니라 사용자명으로 보임)
    username = models.CharField(max_length=32, verbose_name='사용자명')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간')  # auto_now_add : 저장되는 시점을 자동으로 저장

    def __str__(self):
        # 클래스를 문자열로 변환했을때 나오는 값(Fcuser Object)를 어떻게 변환할지(self.username) 바꿔주는 내장함수(__str__)
        return self.username

    class Meta:
        # 클래스 내 클래스로 db테이블 명 지정(기존 생성되는 앱과 구분을 위함)
        db_table = 'fastcampus_fcuser'
        verbose_name = '패스트캠퍼스 사용자'  # admin
        초기화면 표기수정
        verbose_name_plural = '패스트캠퍼스 사용자'
