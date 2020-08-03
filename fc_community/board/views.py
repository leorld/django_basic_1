from django.shortcuts import render, redirect
from .models import Board
from .forms import BoardForm
from fcuser.models import Fcuser
from django.http import Http404
from django.core.paginator import Paginator

# Create your views here.


def board_list(request):
    # 모든 게시글을 가지고오고 시간역순(최신순)으로 (-:역순) 정렬하겠다.
    all_boards = Board.objects.all().order_by('-id')
    page = int(request.GET.get('p', 1))  # page = p라는 변수로 하나의 숫자를 받음
    paginator = Paginator(all_boards, 2)  # Paginator()함수로 all_boards중 2개씩 나타냄

    boards = paginator.get_page(page)  # 나타난 boards page를 가져옴
    # boards에 page정보가 추가되어있음 -> list페이지에서 활용가능

    return render(request, 'board_list.html', {'boards': boards})


def board_write(request):
    if not request.session.get('user'):
        return redirect('/fcuser/login/')

    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            fcuser = Fcuser.objects.get(pk=user_id)

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser
            board.save()

            return redirect('/board/list/')

    else:
        form = BoardForm()

    return render(request, 'board_write.html', {'form': form})


def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('해당 게시글을 찾을 수 없습니다.')
    return render(request, 'board_detail.html', {'board': board})
