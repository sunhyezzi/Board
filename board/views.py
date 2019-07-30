from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Board
from .forms import BoardForm
from .models import Comment
from .forms import CommentForm

# Create your views here.


def show(request): 
    return render(request, 'show.html')


def post(request):
    boards =Board.objects.order_by('-id') #쿼리셋
    return render(request, 'post.html', {'boards':boards})


def detail(request, board_id):
    board_detail = get_object_or_404(Myapp, pk = board_id )
    return render(request, 'detail.html', {'board':board_detail})



def new(request): #new.html 띄워주는 함수
    return render(request, 'new.html')


def create(request): #입력받은 내용을 데이터베이스에 넣어주는 함수
    board = Board()
    board.title = request.GET['title']
    board.body = request.GET['body']
    board.update_date = timezone.datetime.now()
    board.save()
    return redirect('/board/' + str(board.id))


def delete(request, pk):
        board = Board.objects.get(id=pk)
        board.delete()
        return redirect('index')


def edit(request,pk):
        board = get_object_or_404(Myapp, pk=pk)

        if request.method == "POST":
                form = BoardForm(request.POST, instance=board)
             
                if form.is_valid():
                        board = form.save(commit = False)
                        board.update_date=timezone.now()
                        board.save()
                        return redirect('post')
        else:
                form = BoardForm(instance=board)
                return render(request, 'edit.html', {'form': form})


def detail(request, board_id):
        board = get_object_or_404(Board, pk=board_id)
        
        if request.method == "POST":
                comment_form = CommentForm(request.POST)
                comment_form.instance.board_id = board_id
                
                if comment_form.is_valid():
                        comment = comment_form.save()

        comment_form = CommentForm()
        comments = board.comments.all()

                       
        return render(request, 'detail.html', {'board':board, 'comments':comments, 'comment_form':comment_form})
