from django.urls import path, include
from rest_framework import routers
from transaction import views

router = routers.DefaultRouter()
router.register(r'transactions', views.TransactionViewSet,basename='Transaction')
router.register(r'transactionslistitem', views.TransactionListItemViewSet,basename='TransactionLineItem')
router.register(r'inventory', views.InventoryViewSet,basename='Inventory')
router.register(r'allDetails', views.ViewAllTransactionDetailViewSet,basename='allDetails')

transaction_urls = [
    path('', include(router.urls)),
]