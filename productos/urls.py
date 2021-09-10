from django.urls import path



from .views import ProductoListView, ProductoDetailView, ProductoCreate, ProductoUpdate, ProductoDelete

productos_patterns = ([
    # Paths de productos
    path('', ProductoListView.as_view(), name="list"),
    path('<int:pk>/<slug:slug>/', ProductoDetailView.as_view(), name="detail"),
    path('crear/', ProductoCreate.as_view(), name='create'),
    path('actualizar/<int:pk>', ProductoUpdate.as_view(), name='update'),
    path('borrar/<int:pk>', ProductoDelete.as_view(), name='delete'),
], 'productos')
