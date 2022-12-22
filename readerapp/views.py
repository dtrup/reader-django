from rest_framework import generics
from .models import Text, Sentence
from .serializers import TextSerializer, SentenceSerializer



class TextListView(generics.ListAPIView):
    queryset = Text.objects.all().order_by('text_order')
    serializer_class = TextSerializer

class TextDetailView(generics.ListAPIView):
    serializer_class = TextSerializer

    def get_queryset(self):
        text_id = self.kwargs['text_id']
        queryset = Text.objects.filter(text_id=text_id)
        return queryset

class ChapterListView(generics.ListAPIView):
    serializer_class = SentenceSerializer

    def get_queryset(self):
        text_id = self.kwargs['text_id']
        chapter = self.kwargs['chapter_number']
        queryset = Sentence.objects.filter(text_id=text_id, chapter_number=chapter).order_by('sentence_id')
        return queryset
    