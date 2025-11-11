from antlr4 import *
from lenguaje.GrammarLexer import GrammarLexer
from lenguaje.GrammarParser import GrammarParser
import io
import sys
from lenguaje.MyVisitor import MyVisitor
import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Importar el metodo run_code
from api.utils import run_code

@api_view(['POST'])
def main(request):
    # Definimos el metodo de la peticion
    if request.method != 'POST':
        return JsonResponse(
            {'code':''},
            status=405
        )
    
    try:
        # Parsear el cuerpo de la peticion en un Json
        body=request.body.decode('utf-8') if request.body else ''
        data = json.loads(body) if body else {}
    except Exception:
        return JsonResponse(
            {'code':'Json invalido'},
            status=405
        )
    
    # Del Json se obtine el que tenga 'text'
    code = data.get('text','')
    # Ejecutar las instrucciones con el metodo definido (run_code) 
    output = run_code(code)     
    # Damos una respuesta de tipo Json 
    return Response(
        {"output": output},
        status=status.HTTP_200_OK
    )