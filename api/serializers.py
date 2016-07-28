from django.contrib.auth.models import User,Group
from models import Account
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer):
    gender = serializers.CharField()
    username = serializers.CharField(source = 'user.username')
    email = serializers.CharField(source = 'user.email')
    password = serializers.CharField(source = 'user.password')

    class Meta:
        model = Account
        fields = ('id','username','email','password','gender')

    def update(self, instance, validated_data):
        print validated_data.get('user.username',instance.user.username)
        instance.user.username = validated_data.get('user.username',instance.user.username)
        instance.user.password = validated_data.get('user.password',instance.user.userpassword)
        instance.user.email = validated_data.get('user.email',instance.user.email)
        instance.user.email = validated_data.get('gender',instance.gender)

    def create(self, validated_data):
        #print validated_data
        user_data = validated_data.get('user')
        #print userr.get('username')
        #print userr
        #print validated_data.get('username')
        user = User.objects.create_user(
            username=user_data.get('username'),
            password=user_data.get('password'),
            email=user_data.get('email')
        )
        return Account(user=user,gender=validated_data.get('gender'))
