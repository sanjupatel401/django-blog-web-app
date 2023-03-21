from django.urls import path,include
from . import views

urlpatterns = [
   
   path('',views.home,name='home'),
   path('/login',views.login_user,name='login'),
   path('/logout',views.logout_user,name='logout'),
   path('/addblog',views.add_blog,name='add_blog'),
   path('blog-page/<slug:slug>/',views.blog_page,name='blog_page'),
   path('all-blogs',views.all_blogs,name='all_blogs'),
   path('<int:pk>',views.delete_blog,name='delete_blog'),
   

] 


