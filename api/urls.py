from api.views import WheaterInformation
from django.urls import path

urlpatterns = [
    #path('transactions_document/update/<uuid:pk>', TransactionsDocumentUpdateAPIView.as_view(), name=TransactionsDocumentUpdateAPIView.name)
    path('v1/obtain_weather_info/', WheaterInformation.as_view(), name="WheaterInformation"),
]
