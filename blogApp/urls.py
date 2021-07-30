from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView
from . import views
from django.contrib.auth import views as auth_view
from django.urls import reverse_lazy
# app_name = 'blogApp'
urlpatterns = [

    # path('login/',LogoutView.as_view()),
    path('login/',LoginView.as_view(),name="login"),    
    path('register/',views.register,name="register"),   
    path('logout/',LogoutView.as_view(next_page='blogApp:login'),name="logout"),
    path('password_reset/',auth_view.PasswordResetView.as_view(template_name='registration/password_reset.html'),name="password_reset"),
    path('password_reset/done',auth_view.PasswordResetDoneView.as_view(template_name='password_done.html'),name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>',auth_view.PasswordResetConfirmView.as_view(template_name='registration/password_confirm.html',success_url=reverse_lazy('blogApp:password_reset_complete')),name="password_reset_confirm"),
    path('password_reset-complete',auth_view.PasswordResetCompleteView.as_view(template_name='password_complete.html'),name="password_reset_complete"),
    
    path('',views.post_list,name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail,name='post_detail'),
    path('<int:post_id>/share/',views.post_share,	name='post_share'),
    path('add/',views.AddPost,name='add_post'),
]