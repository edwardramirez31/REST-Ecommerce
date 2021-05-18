from .serializers import UserSerializer, TestSerializer, ListUserSerializer
from rest_framework import status
from rest_framework.views import APIView
from apps.users.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view

class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        # test serializer
        data = {
            "name": "Edward Ramírez",
            "email": "edwards@gmail.com",
        }
        serializer = TestSerializer(data=data)
        if serializer.is_valid():
            print("This is valid")
        else:
            print(serializer.errors)

        return Response(users_serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def user_api_view(request, pk):
    user = User.objects.filter(pk=pk).first()

    if user:

        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            user_serializer = UserSerializer(user, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == "DELETE":
            user.delete()
            return Response({"message": "User deleted successfully!"}, status=status.HTTP_200_OK)
    
    return Response({"message": "User not found"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def users_api_view(request):

    if request.method == 'GET':
        users = User.objects.all().values("id", "username", "email", "password")
        users_serializer = ListUserSerializer(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        users_serializer = UserSerializer(data=request.data)
        if users_serializer.is_valid():
            users_serializer.save()
            return Response(users_serializer.data, status=status.HTTP_201_CREATED)

        return Response(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


