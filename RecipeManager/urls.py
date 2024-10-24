from django.contrib import admin
from django.urls import path
from recipes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='main_page'),
    path('recipe/<int:id>/', views.recipe_details, name='recipe_details'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('edit/<int:id>', views.edit_recipe, name='edit_recipe'),
]
