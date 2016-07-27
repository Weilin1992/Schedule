from django.contrib.auth.models import User,Group
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source = 'gender')
    username = serializers.CharField(source = 'user.username')
    email = serializers.CharField(source = 'user.email')
    password = serializers.CharField(source = 'user.password')

    class Meta:
        model = Account
        fields = ('id','username','email','password','gender')

    def update(self, instance, validated_data):
        instance.user.username = validated_data.get('user.username',instance.user.username)
        instance.user.password = validated_data.get('user.password',instance.user.userpassword)
        instance.user.email = validated_data.get('user.email',instance.user.email)
        instance.user.email = validated_data.get('gender',instance.gender)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data.get('user.username'),
            password=validated_data.get('user.password'),
            email=validated_data.get('user.email')
        )
        return Account(user=user,gender=validated_data.get('gender'))
