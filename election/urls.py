from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.home, name='home'),  # Add a root URL pattern
    path('polling_unit/<int:polling_unit_id>/', views.polling_unit_results, name='polling_unit_results'),
    path('lga_results/', views.lga_results, name='lga_results'),
    path('add_results/', views.add_results, name='add_results'),
    path('success/', views.success, name='success'),  # Add this line

]
