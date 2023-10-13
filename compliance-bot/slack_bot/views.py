# slack_bot/views.py
import json

from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from django.http.response import JsonResponse

from slack_bot.models import ApiQuery
from slack_bot.serializers import ApiQuerySerializer
from django.core import serializers
from chat_bot.chat_bot import askChatBot
import urllib.parse




@api_view(['POST'])
def qeuryChatBot(request):
    payload = json.loads(request.body)
    print('*********', payload)
    parsedBody = dict(urllib.parse.parse_qsl(payload))
    print('##########', parsedBody)
    query = parsedBody['text']
    print('@@@@@@@', query)
    response = askChatBot(query)
    return JsonResponse({"response": response })