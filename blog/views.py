from django.shortcuts import render , redirect
from .models import Post , Comment
from .forms import PostForm , CommentForm
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView


# Create your views here.


class PostList(ListView): #django make tmplate auto = post_list name data and action (list) "defult django project"
    model = Post          # context ===> post_list , or object_list   "defult django project"

#class PostDetail(DetailView):
#    model = Post
def post_detail(request,pk):
    data = Post.objects.get(id=pk)
    post_comments = Comment.objects.filter(post=data)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.post = data
            myform.save()
    else:
        form = CommentForm()
    return render(request,'blog/post_detail.html',{'post':data , 'form':form , 'post_comments':post_comments})




class PostCreate(CreateView):
    model = Post
    fields = ['title','content','image','tags','create_date','draft','author']
    success_url ='/blog'

class PostUpdate(UpdateView):
    model = Post
    fields = ['title','content','image','tags','create_date','draft','author']
    success_url ='/blog'
    template_name = 'blog/edit_post.html'

class PostDelete(DeleteView):
    model = Post
    success_url ='/blog'



