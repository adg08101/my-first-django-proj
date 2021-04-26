from django.urls import path, register_converter

from . import views, yearConverter

register_converter(yearConverter.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/<yyyy:year>/<slug:bla>/results', views.results, name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),
]