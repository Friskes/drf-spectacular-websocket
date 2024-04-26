from rest_framework import serializers


class InputSerializer(serializers.Serializer):
    field1 = serializers.CharField()
    field2 = serializers.IntegerField()


class OutputSerializer(serializers.Serializer):
    field3 = serializers.CharField()
    field4 = serializers.IntegerField()


class BadOutputSerializer(serializers.Serializer):
    field5 = serializers.CharField()
    field6 = serializers.IntegerField()
