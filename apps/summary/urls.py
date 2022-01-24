from django.urls import path

from .views import SummaryView


urlpatterns = [
    path('<int:year>/<int:month>', SummaryView.as_view(), name='summary'),
]
