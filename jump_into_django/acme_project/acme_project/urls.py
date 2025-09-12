from django.urls import include, path

urlpatterns = [    
    # Если на сервер пришёл запрос к главной странице,
    # Django проверит на совпадение с запрошенным URL 
    # все path() в файле urls.py приложения homepage.
    path('', include('homepage.urls')),

    # Если в приложении homepage не найдётся совпадений,
    # Django продолжит искать совпадения здесь, в корневом файле urls.py.

    # Если запрос начинается с catalog/, 
    # Django будет искать совпадения в файле urls.py
    # приложения catalog.
    path('catalog/', include('catalog.urls')),
]