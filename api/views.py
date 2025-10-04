from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TrainingData, AnalysisResult
from .serializers import TrainingDataSerializer, AnalysisResultSerializer

@api_view(['POST'])
def training(request):
    serializer = TrainingDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def analyze(request):
    serializer = AnalysisResultSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
