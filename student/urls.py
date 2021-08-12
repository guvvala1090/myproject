from .views import *
from django.urls import path

stu_urls = [
    path('details/', details),
    path('create/', create),
    path('update/<int:id>/', update),
    path('delete/<int:id>', delete),

    path('create1/', create1),
    path('update/<int:id>/',update),
    path('delete/<int:id>/',delete),
    path('details/',details),

    path('create1/',create1),
    path('update/<int:id>/',update),
    path('delete/<int:id>',delete),
    path('details/',details),


    ]