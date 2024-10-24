from django.shortcuts import render, redirect
from .models import Recipe

# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})

def recipe_details(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'recipe_details.html', {'recipe': recipe})

def add_recipe(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        ingredients = request.POST.get('ingredients')
        instructions = request.POST.get('instructions')

        new_recipe = Recipe.objects.create(name=name, ingredients=ingredients, instructions=instructions)

        new_recipe.save()

        return redirect('main_page')
    return render(request, 'add_recipe.html')

def edit_recipe(request, id):
    recipe = Recipe.objects.get(id=id)

    if request.method == 'POST':
        recipe.name = request.POST.get('name')
        recipe.ingredients = request.POST.get('ingredients')
        recipe.instructions = request.POST.get('instructions')

        recipe.save()

        return redirect('main_page')

    return render(request, 'edit_recipe.html', {'recipe': recipe})