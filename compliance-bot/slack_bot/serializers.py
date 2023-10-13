from rest_framework import serializers 

from slack_bot.models import ApiQuery

class ApiQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiQuery
        fields = ['query']
