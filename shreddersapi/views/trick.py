"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from shreddersapi.models import Trick, TrickType, Skater
from django.core.exceptions import ValidationError

class TrickView(ViewSet):
    """Shredders Tricks view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single trick
        
        Returns:
            Response -- JSON serialized game type
        """
        try: 
            trick = Trick.objects.get(pk=pk)
            serializer = TrickSerializer(trick)
            return Response(serializer.data)
        except Trick.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
                
    def list(self, request):
        """Handle GET requests to get all trick types
        Returns:
            Response -- JSON serialized list of trick types
        """
        tricks = Trick.objects.all()
        trick_type = request.query_params.get('type', None)
        if trick_type is not None:
            tricks = tricks.filter(game_type_id=trick_type)
        serializer = TrickSerializer(tricks, many=True)
        return Response(serializer.data)

    
    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized game instance
        """
        skater = Skater.objects.get(user=request.auth.user)
        serializer = CreateTrickSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        saved_trick = serializer.save(skater=skater)
        response = TrickSerializer(saved_trick)
        return Response(response.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a trick
        Returns:
            Response -- Empty body with 204 status code
        """
        trick = Trick.objects.get(pk=pk)
        serializer = CreateTrickSerializer(trick, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        trick = Trick.objects.get(pk=pk)
        trick.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        


class TrickSerializer(serializers.ModelSerializer):
    """JSON serializer for trick types
    """
    class Meta:
        model = Trick
        fields = ('id', 'trick_type', 'name', 'skater', 'skill_level')
        depth = 1

class CreateTrickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trick 
        fields = ('id', 'trick_type', 'name', 'skill_level')