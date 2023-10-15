
from django.urls import path
from . import views
app_name='shop'
urlpatterns = [
    path('',views.allprodcat,name='allprodcat'),
    path('<slug:c_slug>/',views.allprodcat,name='productbycat'),
    path('<slug:c_slug>/<slug:p_slug>/',views.productdetail,name='productdetial'),
]