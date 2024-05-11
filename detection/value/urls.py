from django.urls import path
from .views import value_form_view, tuberc, covid, bacteria, virus, instructions

app_name='value'

urlpatterns = [
    path('', value_form_view, name='value'),
    path('tuberc/', tuberc, name='tuberc'),
    path('covid/', covid, name='covid'),
    path('bacteria/', bacteria, name='bacteria'),
    path('virus/', virus, name='virus'),
    path('instructions/', instructions, name='instructions')
]
