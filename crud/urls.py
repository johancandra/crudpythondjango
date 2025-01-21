from django.urls import path

from . import views

app_name = 'crud'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('adduser/', views.addUser, name='adduser'),
    #id hash
    #path(r'^(?P<id>\d)/$', views.deleteUser, name='deleteuser'),
    path('<int:user_id>/delete/', views.deleteUser, name='deleteuser'),
    path('<int:pk>/update/', views.UpdateView.as_view(), name='updateview'),
    path('<int:user_id>/updateproccess/', views.updateUser, name='updateuser'),
    path('product/', views.ProductView.as_view(), name='index_product'),
    path('addproduct/', views.addProduct, name='addproduct'),
    path('<int:product_id>/deleteproduct/', views.deleteProduct, name='deleteproduct'),
    path('<int:pk>/product/update/', views.UpdateView_product.as_view(), name='updateviewproduct'),
    path('<int:product_id>/updateproccessproduct/', views.updateProduct, name='updateproduct'),
]
#pip install mysql
#python manage.py makemigrations
#python manage.py migrate
#python manage.py createsuperuser
#python manage.py runserver