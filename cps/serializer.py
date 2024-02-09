from rest_framework import serializers
from .models import FinishGood
from .models import Componente
from .models import BOM


class FinishGoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinishGood 
        fields = '__all__'

class ComponenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Componente
        fields = ['Referencia', 'Descripcion', 'Estado', 'Stock', 'Necesidad', 'Url']
        
class BOMSerializer(serializers.ModelSerializer):
    class Meta:
        model = BOM 
        fields = '__all__'