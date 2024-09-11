from django.shortcuts import render,redirect

from .models import Post,Category
from .forms import PostForm
from django.contrib import messages







# create crud operaions by fbv

def post_list(request):
    posts=Post.objects.all()
    category=Category.objects.all()
 
    context={
        'posts':posts,
        'category':category
        
    }
    return render(request,'posts/post_list.html',context)

def add_post(request):
    if request.method=='POST':
        title=request.POST['title']
        content=request.POST['content']
        tags=request.POST['tags']
        image=request.FILES['files'].name
        
        draft=request.POST.get('draft') == 'on'
        category_id=request.POST.get('category')

        Post.objects.create(
            user=request.user,
            title=title,
            content=content,
            tags=tags,
            image=image,
            draft=draft,
            category_id=category_id
        )

        messages.success(request, 'Add post succesfuly')
        return redirect('/posts/')







def delete(request):
    if request.method=='POST':
        slug=request.POST['slug']
        post=Post.objects.get(slug=slug)
        post.delete()

        messages.error(request, 'Delete post succesfuly')
        return redirect('/posts/')
    


