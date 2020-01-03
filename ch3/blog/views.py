from django.shortcuts import get_object_or_404, render
from .models import Post
from blog.form import PostForm
from django.shortcuts import redirect
# Create your views here.

def index(request):
    post = Post.objects.all()
    return render(request,'blog/index.html',{'post':post})

def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request,'blog/detail.html',{'post':post})

def create(request):
    if request.method == 'POST' :
        form = PostForm(request.POST)
        # form 인스턴스를 생성하고 요청(request.POST)에 의한 data를 넣는다 .
        if form.is_valid():
            form.save()
            return redirect('/blog/index/',pk=pk)
    else :
        form = PostForm()
    return render(request,'blog/create.html',{'form':form})

def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('blog:index')

def update(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post) #update 할 때는 instance=post로 filtering
        if form.is_valid():
            form.save()
            return redirect ('blog:detail',pk=pk) #redirect에는 view의 이름을 가져올 수 도 있지만 어떤 application인지 확인하자
    else:
        form = PostForm(instance=post)
    return render(request,'blog/update.html',{'form':form})

def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST,instance=post)
        if form.is_valid():
            comment = form.save()
