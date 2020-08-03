from django.db import models

# Create your models here.


class Board(models.Model):
    title = models.CharField(max_length=128, verbose_name='제목')
    contents = models.TextField(verbose_name="내용")
    writer = models.ForeignKey(
        'fcuser.Fcuser', on_delete=models.CASCADE, verbose_name='작성자')
    # ForeignKey가 가르키고 있는 사용자정보가 삭제된 경우 on_delete = CASCADE 옵션: 같이삭제, SET_DEFAULT : 기본값으로 둠, SET_NULL : NULL값으로 둠
    # writer는 fcuser.Fcuser를 가르키도록 하는 ForeignKey()
    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        # 클래스를 문자열로 변환했을때 나오는 값(Fcuser Object)를 어떻게 변환할지(self.username) 바꿔주는 내장함수(__str__)
        return self.title

    class Meta:
        # 클래스 내 클래스로 db테이블 명 지정(기존 생성되는 앱과 구분을 위함)
        db_table = 'fastcampus_board'
        verbose_name = '패스트캠퍼스 게시글'  # admin 초기화면 표기수정
        verbose_name_plural = '패스트캠퍼스 게시글'
