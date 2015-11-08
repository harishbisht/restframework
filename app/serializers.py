# from .models import StudentDetails
# from rest_framework import serializers
# class StudentDetailsSerializer(serializers.Serializer):
#     class Meta:
#         model = StudentDetails
#         fields = ('rollno', 'name', 'address')


from rest_framework import serializers
from .models import StudentDetails


# class StudentDetailsSerializer(serializers.Serializer):
#     pk = serializers.IntegerField(read_only=True)
#     rollno = serializers.IntegerField(default=100)
#     name = serializers.CharField(max_length=128)
#     address = serializers.CharField(max_length=128)
   
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return StudentDetails.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.rollno = validated_data.get('rollno', instance.rollno)
#         instance.name = validated_data.get('name', instance.name)
#         instance.address = validated_data.get('address', instance.address)
#         instance.save()
#         return instance

class StudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetails
        fields = ('id', 'rollno', 'name', 'address')