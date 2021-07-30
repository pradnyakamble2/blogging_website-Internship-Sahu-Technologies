from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect
from .models import Post,Comment
from	django.core.paginator import Paginator,	EmptyPage,PageNotAnInteger
from .forms import EmailPostForm,CommentForm,PostForm
from django.contrib.auth.forms import UserCreationForm
from	django.core.mail	import	send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required

def LoginView(request):
    # return HttpResponse("Hello")
    return render(request, "blog/registeration/login.html")

def register(request):
    if request.method == "POST":
        forms = UserCreationForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('login')
    else:
        forms = UserCreationForm()
    return render(request, "registration/register.html", {'form': forms})

@login_required
# Create your views here.
def	post_list(request):
    
	object_list = Post.published.all()
	paginator	= Paginator(object_list,	1)	
	page	=request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
			posts = paginator.page(1)
	except EmptyPage:
	
	     posts = paginator.page(paginator.num_pages)
	return render(request,'blog/post/list.html',{'page':page,'posts':posts})
     



def post_detail(request,year,month,day,post):

    post=get_object_or_404(Post,slug=post,status='Published',publish__year=year,publish__month=month,publish__day=day)
    #  print(post)
    #list of all active comments
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        #A comment was posted
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # #create the comment object but dont save yet
            # print(comment_form)
            # new_comment = comment_form.save(commit=False)
            # #Assign the current post to the comment
            # new_comment.post = post
            # #save Comment to the database
            Comment.objects.create(post=post,name=comment_form.cleaned_data['name'],email=comment_form.cleaned_data['email'],body=comment_form.cleaned_data['body'])
            
            comment_form = CommentForm()
            data = {'post':post,
                'comments':	comments,
                'new_comment':	new_comment,
                'comment_form':	comment_form }

        return render(request,"blog/post/detail.html",data)
   
    else:
        comment_form = CommentForm()
    data = {'post':post,
                'comments':	comments,
                'new_comment':	new_comment,
                'comment_form':	comment_form }
    return render(request,"blog/post/detail.html",data)



def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='Published')
    sent=False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(
                cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments:{}'.format(
                post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, settings.EMAIL_FROM, [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post, 'form': form,"sent":sent})


def AddPost(request):
    comment_form = PostForm(request.POST)
    if request.method == 'POST':
        #create the comment object but dont save yet
            print(comment_form)
            new_comment = comment_form.save(commit=False)
            #Assign the current post to the comment
            new_comment.post = post
            #save Comment to the database