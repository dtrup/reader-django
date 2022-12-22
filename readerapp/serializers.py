from rest_framework import serializers
from .models import Text, Sentence


class TextSerializer(serializers.ModelSerializer):

    class Meta:
        model = Text
        fields = '__all__'



class SentenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sentence
        fields =  fields = '__all__'
        ordering_fields = ['sentence_id']

