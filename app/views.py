from app.models import StudentDetails
from app.serializers import StudentDetailsSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# from app.models import StudentDetails
# from app.serializers import StudentDetailsSerializer
# from rest_framework import generics


# class studentList(generics.ListCreateAPIView):
#     queryset = StudentDetails.objects.all()
#     serializer_class = StudentDetailsSerializer


# class studentDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = StudentDetails.objects.all()
#     serializer_class = 





class studentList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        student = StudentDetails.objects.all()
        serializer = StudentDetailsSerializer(student, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class studentDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return StudentDetails.objects.get(pk=pk)
        except StudentDetails.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentDetailsSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentDetailsSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)