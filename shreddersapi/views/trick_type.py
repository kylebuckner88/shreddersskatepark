"""View module for handling requests about trick types"""
from django.http import HttpResponseServerError 
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from shreddersapi.models import TrickType


class TrickTypeView(ViewSet):
    """Shredders trick types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single trick type
        
        Returns:
            Response -- JSON serialized trick type
        """
        try:
            trick_type = TrickType.objects.get(pk=pk)
            serializer = TrickTypeSerializer(trick_type)
            return Response(serializer.data)
        except TrickType.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 
        
    def list(self, request):
        """Handle GET requests to get all trick types
        Returns:
            Response -- JSON serialized list of trick types
        """
        trick_types = TrickType.objects.all()
        serializer = TrickTypeSerializer(trick_types, many=True)
        return Response(serializer.data)

class TrickTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for trick types
    """
    class Meta:
        model = TrickType
        fields = ('id', 'label')