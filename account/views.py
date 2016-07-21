
from django.contrib.auth.models import User,Group
from rest_framework import viewsets
#from account.serializers import UserSerializer,GroupSerializer
from django.shortcuts import render_to_response


# Create your views here.

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#
# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

def sign_log(request):

    return render_to_response('account/sign_log.html')
