from django.urls import path, register_converter, re_path, include

from . import views, yearConverter

register_converter(yearConverter.FourDigitYearConverter20Century, '20yy')
register_converter(yearConverter.FourDigitYearConverter21Century, '21yy')

extra = [
    path('goback/<str:desde>', views.index,  name='goback'),
]


urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'(?P<month_id>[0, 1]{1}[0, 1, 2]{1})(?P<question_id>[0-9]{2})/vote', views.vote, name='vote'),
    path('atras/', include(extra)),
    path('<int:question_id>', include(
        [
            path('', views.detail, name='detail'),
            path('/<20yy:year>/<slug:bla>/results', views.results, name='results20'),
            path('/<21yy:year>/<slug:bla>/results', views.results, {'theme': 'customized'}, name='results21'),
        ]
    )),
]
