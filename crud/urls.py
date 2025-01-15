from django.urls import path

from . import views

app_name = 'crud'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('adduser/', views.addUser, name='adduser'),
    # id hash
    # path(r'^(?P<id>\d)/$', views.deleteUser, name='deleteuser'),
    path('<int:user_id>/delete/', views.deleteUser, name='deleteuser'),
    path('<int:pk>/update/', views.UpdateView.as_view(), name='updateview'),
    path('<int:user_id>/updateproccess/', views.updateUser, name='updateuser'),
    #path('addproduct/', views.addProduct, name='addproduct'),
    #path('<int:user_id>/delete/', views.deleteProduct, name='deleteproduct'),
    #path('<int:user_id>/updateproccess/', views.updateProduct, name='updateproduct'),
]