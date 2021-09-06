from api.views import NodeInformation
from django.urls import path

urlpatterns = [
    #path('transactions_document/update/<uuid:pk>', TransactionsDocumentUpdateAPIView.as_view(), name=TransactionsDocumentUpdateAPIView.name)
    path('v1/node_information/', NodeInformation.as_view(), name="NodeInformation"),
]
