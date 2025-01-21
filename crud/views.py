from django.http import HttpResponseRedirect
from django.views import generic
from crud.models import User
from crud.models import Product
from django.urls import reverse

from django.shortcuts import get_object_or_404, render


# generic views
class IndexView(generic.ListView):

    template_name = "crud/index.html"
    
    context_object_name = 'users'

    def get_queryset(self):
        """blabla"""
        return User.objects.all()

# 
def addUser(request):
    # jika field form ada yang kosong
    if len(request.POST['username']) == 0 or len(request.POST['first_name']) == 0 or len(request.POST['last_name']) == 0 :
        users = User.objects.all()
        # hanya redierect ke index
        return HttpResponseRedirect(reverse('crud:index'))
    else:
        # insert ke database
        new_user = User.objects.create(username=request.POST['username'].lower(), first_name=request.POST['first_name'].title(), last_name=request.POST['last_name'].title())
        # execute
        new_user.save()
        # redirect ke halaman index
        return HttpResponseRedirect(reverse('crud:index'))

# 
def deleteUser(request, user_id):
    user_delete = User.objects.get(id=user_id)
    user_delete.delete()
    return HttpResponseRedirect(reverse('crud:index'))

# 
class UpdateView(generic.DetailView):
    model = User
    # 
    template_name = "crud/update.html"
    
    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        # ini adalah context_object_name, context['users']
        context['users'] = User.objects.filter(pk=self.kwargs['pk'])
        return context

# 
def updateUser(request, user_id):
    # update data
    User.objects.filter(id=user_id).update(username=request.POST['username'].lower(), first_name=request.POST['first_name'].title(), last_name=request.POST['last_name'].title())
    # 
    return HttpResponseRedirect(reverse('crud:index'))
# generic views
class ProductView(generic.ListView):

    template_name = "crud/product.html"
    
    context_object_name = 'products'

    def get_queryset(self):
        """blabla"""
        return Product.objects.all()
# 
def addProduct(request):
    # jika field form ada yang kosong
    if len(request.POST['product_name']) == 0 :
        Products = Product.objects.all()
        # hanya redierect ke product
        return HttpResponseRedirect(reverse('crud:index_product'))
    else:
        # insert ke database
        new_product = Product.objects.create(product_name=request.POST['product_name'].lower())
        # execute
        new_product.save()
        # redirect ke halaman product
        return HttpResponseRedirect(reverse('crud:index_product'))

# 
def deleteProduct(request, product_id):
    user_delete = Product.objects.get(id=product_id)
    user_delete.delete()
    return HttpResponseRedirect(reverse('crud:index_product'))

# 
class UpdateView_product(generic.DetailView):
    model = Product
    # 
    template_name = "crud/update_product.html"
    
    def get_context_data(self, **kwargs):
        context = super(UpdateView_product, self).get_context_data(**kwargs)
        # ini adalah context_object_name, context['users']
        context['products'] = Product.objects.filter(pk=self.kwargs['pk'])
        return context

# 
def updateProduct(request, product_id):
    # update data
    Product.objects.filter(id=product_id).update(product_name=request.POST['product_name'].lower())
    # 
    return HttpResponseRedirect(reverse('crud:index_product'))