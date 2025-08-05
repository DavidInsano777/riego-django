from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Lectura
from .serializers import LecturaSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Lectura
import json
from datetime import datetime

# Create your views here.
@api_view(['GET', 'POST'])
def lectura_api(request):
    if request.method == 'GET':
        lecturas = Lectura.objects.all().order_by('-fecha')[:50]
        serializer = LecturaSerializer(lecturas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LecturaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "✅ Lectura guardada",
                "datos": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def recibir_lectura(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            humedad = data.get('humedad')
            riego = data.get('riego')

            if humedad is None or riego is None:
                return JsonResponse({'error': 'Faltan campos'}, status=400)

            lectura = Lectura(
                humedad=humedad,
                riego=riego,
                fecha=datetime.now()  # Hora actual local
            )
            lectura.save()

            return JsonResponse({'message': '✅ Lectura guardada exitosamente'}, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Método no permitido'}, status=405)