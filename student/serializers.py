from rest_framework import serializers
from .models import Student_Data,Group_Data


class Student1Serializer(serializers.ModelSerializer):
    group = serializers.SerializerMethodField()

    class Meta:
        model = Student_Data
        fields = '__all__'

    def get_group(self, obj):
        return obj.group.group



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Data
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Group_Data
        fields='__all__'








