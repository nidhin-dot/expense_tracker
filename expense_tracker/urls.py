"""
URL configuration for expense_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from accounts.views import SignUpview


from transactions.views import ExpenselisteCreateView
from transactions.views import ExpenseRetrieveUpdateDeleteView
from transactions.views import ExpenseSummeryView
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),

    #accounts
    path("accounts/register/",SignUpview.as_view()),

    #expenses
    path("expenses/",ExpenselisteCreateView.as_view()),


    path("expenses/<int:pk>/",ExpenseRetrieveUpdateDeleteView.as_view()),

    path("expenses/summery/",ExpenseSummeryView.as_view()),

    path("token/",ObtainAuthToken.as_view())
]
