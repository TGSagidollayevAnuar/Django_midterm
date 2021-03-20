from rest_framewwork import serializers


class BookSerializer(serializers.Modelserializer):
    class Meta:
        model = Book
        fields = '__all__'


class JournalSerializer(serializers.Modelserializer):
    class Meta:
        model = Journal
        fields = '__all__'
