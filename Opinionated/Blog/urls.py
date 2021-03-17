
from django.urls import path
from Blog import views

urlpatterns = [
    path('',views.PostListView.as_view,name='post_list'),
    path('about/',views.AboutView.as_view,name='about'),
    path('<int:pk>/',views.PostDetailView.as_view,name='post_detail'),
]