from transaction.models import TransactionTable, TransactionLineItem, InventoryItem
from rest_framework import viewsets
from transaction.serializers import (TransactionSerializer, TransactionLineItemSerializer, InventorySerializer, ViewAllTransactionDetailsSerializer,)
from django.http import JsonResponse


class TransactionViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            queryset = TransactionTable.objects.all()
            serializer = TransactionSerializer(queryset, many=True)
            return JsonResponse({'data' : serializer.data, 'message': 'success', 'status': 200})
        except Exception as ex:
            return JsonResponse({'message': str(ex), 'status': 400})

    def post(self, request):
        try:
            serializer = TransactionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'data': serializer.data, 'message': "success", 'status':201})
            return JsonResponse({'message': serializer.errors, 'status':400})
        except Exception as ex:
            return JsonResponse({'message': str(ex), 'status': 400})


class TransactionListItemViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            queryset = TransactionLineItem.objects.all()
            serializer = TransactionLineItemSerializer(queryset, many=True)
            return JsonResponse({'data' : serializer.data, 'message': 'success', 'status': 200})
        except Exception as ex:
            return JsonResponse({'message': str(ex), 'status': 400})

    def post(self, request):
        try:
            serializer = TransactionLineItemSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'data' : serializer.data, 'message': 'success', 'status': 200})
            return JsonResponse({'message':serializer.errors, 'status':400})
        except Exception as ex:
            return JsonResponse({'message': str(ex), 'status': 400})


class InventoryViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            queryset = InventoryItem.objects.all()
            serializer = InventorySerializer(queryset, many=True)
            return JsonResponse({'data' : serializer.data, 'message': 'success', 'status': 200})
        except Exception as ex:
            return JsonResponse({'message': str(ex), 'status': 400})

    def post(self, request):
        try:
            serializer = InventorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'data' : serializer.data, 'message': 'success', 'status': 200})
            return JsonResponse({'message':serializer.errors, 'status':400})
        except Exception as ex:
            return JsonResponse({'message': str(ex), 'status': 400})


class ViewAllTransactionDetailViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            queryset = InventoryItem.objects.all()
            serializer = ViewAllTransactionDetailsSerializer(queryset, many=True)
            return JsonResponse({'data' : serializer.data, 'message': 'success', 'status': 200})
        except Exception as ex:
            return JsonResponse({'message': str(ex), 'status': 400})