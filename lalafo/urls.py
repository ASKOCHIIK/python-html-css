from pyexpat import native_encoding

from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path(               #/uslugi/
        'kyrgyzstan/<slug:slug>/', #динамический маршрут
        views.category_products,
        name='category_products',
    )
    # path('kyrgyzstan/transport/', views.my_transport, name='transport'),
    # path('kyrgyzstan/nedvizhimost/', views.nedvijimost, name='nedvijimost'),
]