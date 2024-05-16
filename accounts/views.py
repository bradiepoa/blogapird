from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import UserRegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from.utils import send_code_to_user
# Create your views here.

class ResgiterUserView(GenericAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        # recieve data from thr form
        user_data=request.data
        # validating data and saving in the db
        serializer=self.serializer_class(data=user_data)
        if serializer.is_valid(raise_exception=True):
            # and saving in the db
            serializer.save()
            user=serializer.data
            send_code_to_user(user['email'])
            return Response({
                'data':user,
                'message':f'hi {user.get("first_name", "User")}, thanks for signing up passcode is '
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


        