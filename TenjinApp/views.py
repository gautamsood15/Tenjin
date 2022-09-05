from django.shortcuts import render
from .models import Question
from .forms import RegisterUserForm

# Create your views here.


def registerPage(request):
    form = RegisterUserForm()
    context = {
        'form': form
    }
    return render(request, "register.html", context)



def homePage(request):
    questions = Question.objects.all().order_by('-created_at')
    context = {
        'questions': questions
    }
    return render(request, "homepage.html", context)


def questionPage(reuqest, id):
    return None