from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .models import Producto
from .forms import ProductoForm

class ProductoListView(ListView):
    model = Producto
    paginate_by = 10

class ProductoDetailView(DetailView):
    model = Producto

@method_decorator(staff_member_required, name='dispatch')
class ProductoCreate(CreateView):
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy('productos:list')


    def form_valid(self, form):
        print ('Dentro de form valid')
        self.object = form.save(commit=False)
        self.object.idUsuario = self.request.user
        self.object.save()

        
        print (self.object)
        return super(ProductoCreate, self).form_valid(form)


@method_decorator(staff_member_required, name='dispatch')
class ProductoUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy('productos:list')    
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('productos:update', args=[self.object.id]) + '?ok'

    def form_valid(self, form):
        print ('Dentro de form valid')
        self.object = form.save(commit=False)
        self.object.idUsuario = self.request.user
        self.object.save()
        
        print (self.object)
        return super(ProductoUpdate, self).form_valid(form)


@method_decorator(staff_member_required, name='dispatch')
class ProductoDelete(SuccessMessageMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy('productos:list')
    
    
