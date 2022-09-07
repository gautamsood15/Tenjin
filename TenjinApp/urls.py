
from django.urls import path
from . import views


urlpatterns = [
    path("register", views.registerPage, name="register"),
    path("search", views.searchPage, name="search"),
    path("login", views.loginPage, name="login"),
    path("logout", views.logoutPage, name="logout"),
    path("new-question", views.newQuestionPage, name="new-question"),
    path("", views.homePage, name="index"),
    path("question/<int:id>", views.questionPage, name="question"),
    path("reply", views.replyPage, name="reply"),
    
]
