from django.urls import path
from . import views

urlpatterns = [
    # path('all', views.show_all),
    # path('single', views.show_one)
    # path('', views.show_all),
    path('my', views.show_my),
    path('<aid>', views.show_all),


]