from django.shortcuts import render
from django.core.cache import cache
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django_quickstart_app.models import Item
# from .serializers import ItemSerializer

# Create your views here.


class ItemListView(APIView):
    def get(self, request, *args, **kwargs):
        # Intenta obtener los datos del caché
        cached_items = cache.get('items_list')

        if not cached_items:
            items = Item.objects.all()
            # serializer = ItemSerializer(items, many=True)
            cached_items = []
            # Guarda los datos en el caché para futuras solicitudes
            cache.set('items_list', cached_items, timeout=300)  # Cache por 5 minutos

        return Response(cached_items, status=status.HTTP_200_OK)
