from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from.models import Post
from .forms import NewPostForm
from django.views import generic
from django.urls import reverse_lazy


# def post_list_view(request):
#     posts_list=Post.objects.filter(status='pub').order_by('datetime_modified')
#     return render(request,'blog/posts_list.html',{'posts_list':posts_list})
class PostListView(generic.ListView):
    #  model=Post
     template_name='blog/posts_list.html'
     context_object_name='posts_list'

     def get_queryset(self):
          return Post.objects.filter(status='pub').order_by('datetime_modified')

# def post_detail_view(request,pk):
#     print(pk)
#     post=get_object_or_404(Post, pk=pk)
#     # try:
#     #      post= Post.objects.get(id=pk)
#     # except Post.DoesNotExist:
#     #      post=None
#     return render (request, 'blog/post_detail.html', {'post':post})

class PostDetailView(generic.DetailView):
     model=Post
     template_name='blog/post_detail.html'
     context_object_name='post'


class PostCreatVeiew(generic.CreateView):
      form_class=NewPostForm
      template_name='blog/post_create.html'
    

class PostUpdateView(generic.UpdateView):
     form_class=NewPostForm
     template_name= 'blog/post_create.html'
     model=Post

class PostDeleteView(generic.DeleteView):
     model=Post
     template_name= 'blog/post_delete.html'
    #  success_url='/blog/'
     success_url=reverse_lazy('posts_list')


     

# def post_create_view(request):
#     if request.method=="POST":
#         form=NewPostForm(request.POST)
#         print(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('posts_list')
#     else:
#         form=NewPostForm()
#     return render(request,'blog/post_create.html', context={'form':form})

# def post_update_view(request,pk):
#           post=get_object_or_404(Post, pk=pk)
#           print(post)
#           form= NewPostForm(request.POST or None, instance=post)
#           print(request.POST)
#           if form.is_valid():
#               form.save()
#               return redirect('posts_list')
#           return render(request,'blog/post_create.html', context={'form':form})

# def post_delete_view(request, pk):
#       post=get_object_or_404(Post, pk=pk)
#       if request.method=='POST':
#            post.delete()
#            return redirect('posts_list')
#       return render(request,'blog/post_delete.html', context={'post':post})
     
