from django.shortcuts import render
from .models import Board
# Create your views here.


def board_list(request):
    # 모든 게시글을 가지고오고 시간역순(최신순)으로 (-:역순) 정렬하겠다.
    boards = Board.objects.all().order_by('-id')
    return render(request, 'board_list.html', {'boards': boards})
