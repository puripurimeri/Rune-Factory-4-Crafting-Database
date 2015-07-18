from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Recipe, Ingredient

# Create your views here.
def index(request):
    return HttpResponse("index page")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username = username, password = password)
        if user is not None:
            if user.is_active:
                return redirect("index")
            else:
                print("The password is invalid, but the account has been disabled!")
        else:
            print("The username and password were incorrect.")

    return render(request, 'login.html')

def recipes(request, category_name):
    cat = Recipe.objects.values("subcategory").distinct()
    context = {"categories": list()}
    if len(cat) == 0:
        cat = [None]
    for c in cat:
        recipes = Recipe.objects.filter(category = category_name.title(), subcategory = c["subcategory"]).all()
        catdict = {"category_name":c["subcategory"], "Recipes":list()}
        print(catdict)
        print(recipes)
        print(c["subcategory"])
        for recipe in recipes:
            catdict["Recipes"].append({"Name":recipe.name, "Ingredients":recipe.ingredient.all(), "SkillLvl":recipe.skilllvl, "SellValue":recipe.sellvalue})
            print("something", recipe.ingredient.all())
        context["categories"].append(catdict)
        context["page_category"] = category_name.title()
    return render(request, 'recipes.html', context = context)
