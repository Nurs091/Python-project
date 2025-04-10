from django.shortcuts import render
from django.contrib.auth.models import User  # Импортируем модель User

def home(request):
    users = User.objects.all()  # Получаем всех пользователей
    return render(request, 'home.html', {'users': users})  # Передаем пользователей в шаблон

# Create your views here.

