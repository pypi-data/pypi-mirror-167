from django.urls import path
from huscy.consents import views

urlpatterns = [
    path('<int:consent_id>', views.ConsentView.as_view(), name="consent-view"),
]
