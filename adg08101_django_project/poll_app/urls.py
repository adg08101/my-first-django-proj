from django.urls import path, register_converter, re_path, include

from . import views, yearConverter

register_converter(yearConverter.FourDigitYearConverter20Century, '20yy')
register_converter(yearConverter.FourDigitYearConverter21Century, '21yy')

extra = [
    path('goback/<str:desde>', views.index, name='goback'),
]

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('atras/', include(extra)),
    path('new', views.new, name='new'),
    path('<int:question_id>/', include(
        [
            path('', views.detail, name='detail'),
            path('vote', views.vote, name='vote'),
            path('details', views.details, name='details'),
            path('delete', views.delete, name='delete'),
            path('<20yy:year>/<slug:bla>/results', views.results, name='results20'),
            path('<21yy:year>/<slug:bla>/results', views.results, {'theme': 'customized'}, name='results21'),
        ]
    )),
]
