from django.urls import path
from .views import Sheet
urlpatterns = [
    path('sheet/',Sheet.as_view(),name="sheet")
]


