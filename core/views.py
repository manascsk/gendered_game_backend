from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.http import JsonResponse
from.models import *
from.serializers import *
from rest_framework.response import Response

# Create your views here.

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def event(request):
    if request.method == 'GET':
        all_event = Game.objects.all()
        serializer = GameSerializer(all_event, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        Game.objects.create(game_name=request.data['gameName'],developer_name=request.data['developer'],event_name=request.data['eventName'],
        platform=request.data['platForm'],start_date=request.data['startDate'],end_date=request.data['endDate'])
        all_game = Game.objects.all()
        serializer = GameSerializer(all_game, many=True)
        return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([AllowAny])
def event_details(request, pk):
    try:
        event = Game.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    event.delete()
    all_event = Game.objects.all()
    serializer = GameSerializer(all_event, many=True)
    return Response(serializer.data)