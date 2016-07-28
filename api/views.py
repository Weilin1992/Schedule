from django.shortcuts import render
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response
from models import Account
from serializers import AccountSerializer
from rest_framework.decorators import detail_route
from rest_framework import status
# Create your views here.
#
# class AccountIsOwnerOrReadOnly(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#



class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (permissions.AllowAny,)


    def create(self, request):
        print request.data
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)
