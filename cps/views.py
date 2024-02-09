from django.shortcuts import render
from rest_framework import viewsets
from .serializer import FinishGoodSerializer
from .models import FinishGood
from .serializer import ComponenteSerializer
from .models import Componente
from .serializer import BOMSerializer
from .models import BOM
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class FinishGoodBOMView(APIView):
    def get(self, request, referencia):
        # Filtrar BOM por referencia de FinishGood
        bom_items = BOM.objects.filter(finish_good__Referencia=referencia).select_related('componente')
        componentes = [item.componente for item in bom_items]
        
        # Serializar los componentes
        serializer = ComponenteSerializer(componentes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Create your views here.
class FinishGoodView(viewsets.ModelViewSet):
    serializer_class = FinishGoodSerializer
    queryset = FinishGood.objects.all()
    
class ComponenteView(viewsets.ModelViewSet):
    serializer_class = ComponenteSerializer
    queryset = Componente.objects.all()
    
class BOMView(viewsets.ModelViewSet):
    serializer_class = BOMSerializer
    queryset = BOM.objects.all()