from django.contrib import admin
from django.urls import include, path

from polls import views as polls_v

urlpatterns = [
    path('polls/', polls_v.index),
    path('admin/', admin.site.urls),
    path('polls/add/', polls_v.getData),
    path('polls/add_post/', polls_v.postData),
    path('polls/rest/<int:num1>/<int:num2>/', polls_v.getRESTfulData),
    path('polls/speech_synthesis/', polls_v.speech_synthesis),
]