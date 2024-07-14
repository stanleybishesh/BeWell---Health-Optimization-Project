from django.contrib import admin

from bewell.models import Exercise,Food,Sleep,Water


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    pass


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    pass



@admin.register(Sleep)
class FoodAdmin(admin.ModelAdmin):
    pass


@admin.register(Water)
class FoodAdmin(admin.ModelAdmin):
    pass