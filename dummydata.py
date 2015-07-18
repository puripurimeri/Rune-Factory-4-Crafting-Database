import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Rose.settings")
    from Rune.models import Recipe, Ingredient

    ingredientlist = ["Rice", "Salted Salmon"]

    recipelist = ["Onigiri", "Salmon Onigiri"]

    for ingredient in ingredientlist:
        ing = Ingredient.objects.create(name = ingredient, category = "Cooking")
        ing.save()

    for recipe in recipelist:
        rcp = Recipe.objects.create(name = recipe, category="Cooking")
        rcp.ingredient.add(Ingredient.objects.get(pk=1))
        rcp.save()
