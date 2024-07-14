from django.shortcuts import render
from django.core.mail import send_mail 
from django.db.models import F
from decouple import config
from django.db.models import FloatField, ExpressionWrapper

from bewell.models import Exercise, Food, Sleep,Water

def home(request):
    context = {}
    return render(request, 'home.html', context)

def closest_food(gender, height, weight):
    closest_food = Food.objects.annotate(
        distance=ExpressionWrapper(
            (F('height') - height) ** 2 +
            (F('weight') - weight) ** 2,
            output_field=FloatField()
        )
    ).filter(gender=gender).order_by('distance').first()

    return closest_food

def closest_match(age, gender, height, weight):
    closest_exercise = Exercise.objects.annotate(
        distance=ExpressionWrapper(
            (F('age') - age) ** 2 +
            (F('height') - height) ** 2 +
            (F('weight') - weight) ** 2,
            output_field=FloatField()
        )
    ).order_by('distance').first()

    return closest_exercise

def survey(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = int(request.POST.get('age'))
        gender = request.POST.get('gender')
        height = float(request.POST.get('height'))
        weight = float(request.POST.get('weight'))
        trouble_sleeping = request.POST.get('trouble_sleeping')
        water = request.POST.get('water')
        water_interval = request.POST.get('water_interval')
        wake_up_time = request.POST.get('wake_up_time')
        sleep_hour = request.POST.get('sleep_hour')


        print('wake_up_time',wake_up_time)
        print('sleep_hour',sleep_hour)
        print("raw input", age, gender, height, weight,water)
        print('trouble_sleeping', trouble_sleeping)
        print('interval',water_interval)

        closest_exercise = closest_match(age, gender, height, weight)
        closest_food_obj = closest_food(gender, height, weight)

        if closest_exercise:
            print("age", closest_exercise.age)
            print("weight", closest_exercise.weight)
            print("height", closest_exercise.height)
        else:
            print("No matching exercise found")

        if closest_food_obj:
            print("food height", closest_food_obj.height)
            print("food weight", closest_food_obj.weight)
        else:
            print("No matching food found")

        sleep = Sleep.objects.filter(trouble_sleeping=trouble_sleeping).first()
        if sleep:
            print(sleep.title)
        
        context = {
            'closest_exercise': closest_exercise,
            'closest_food_obj': closest_food_obj,
            'sleep': sleep,
            'water':Water.objects.get(litre = water),
            'water_interval':water_interval,
            'wake_up_time':wake_up_time,
            'sleep_hour':sleep_hour,
        }
        # send_mail(
        #             subject="password reset",
        #             message="hi  {}".format(name),
        #             from_email=config('EMAIL_HOST_USER'),
        #             recipient_list=[email],
        #             fail_silently=False,
        #         )
        return render(request, 'result.html', context)

    context = {}
    return render(request, 'survey.html', context)
