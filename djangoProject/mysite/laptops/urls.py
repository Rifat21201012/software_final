from django.urls import path
from .import views
urlpatterns = [
    path('add_laptops', views.add_laptops, name='add_laptops'),
    path('update_laptops/<int:p_id>', views.update_laptops, name='update_laptops'),
    path('delete_laptops/<int:p_id>', views.delete_laptops, name='delete_laptops'),

]
