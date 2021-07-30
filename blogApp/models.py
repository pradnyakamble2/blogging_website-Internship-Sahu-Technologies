from django.db import models
from	django.utils	import timezone
from	django.urls	import	reverse

from django.contrib.auth.models import User
import uuid

class PublishedManager(models.Manager):
				def	get_queryset(self):
								return	super(PublishedManager,
														self).get_queryset()\
																		.filter(status='Published')

     


# Create your models here.
class Post(models.Model):
     STATUS_CHOICES=(
          ('Draft','Draft'),
          ('Published','Published')
     )
     images = models.ImageField(upload_to='images/%Y/%m/%d/',null=True,blank=True)
     title = models.CharField(max_length=250)
     slug = models.SlugField(max_length=250,unique_for_date='publish')
     author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
     body = models.TextField()
     publish = models.DateField(default=timezone.now)
     created = models.DateField(auto_now_add=True)
     updated = models.DateField(auto_now=True)
     status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='Draft')


     def get_absolute_url(self):
        return reverse('blogApp:post_detail',
        args=[self.publish.year,
             self.publish.strftime('%m'),
             self.publish.strftime('%d'),
             self.slug])

     class Meta:
          ordering = ("publish",)

     def __str__(self):
         return self.title

          #	...
     objects	=	models.Manager()	#	The	default	manager.
     published	=	PublishedManager()	#	Our	custom	manager.


     def post_detail(request,year,month,day,post):
          image = models.ImageField(upload_to='images/%Y/%m/%d/',null=True,blank=True)
          post	=get_object_or_404(Post,slug=post,
                                             status='published',
                                             publish__year=year,
                                             publish__month=month,
                                             publish__day=day)
          return render(request,'blog/post/details.html',{'post':post})

class Comment(models.Model):
     post = models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
     name = models.CharField(max_length=80)
     email=models.EmailField()
     body = models.TextField()
     created = models.DateTimeField(auto_now_add=True)
     updated=models.DateTimeField(auto_now=True)
     active = models.BooleanField(default=True)

     class Meta:
          ordering = ('created',)
     
     def __str__(self):
         return 'Commented by {} on {}'.format(self.name,self.post)
     
     


