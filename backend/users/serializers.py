from dj_rest_auth.serializers import LoginSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'avatar']
        write_only_fields = ['username']
        read_only = True


    def validate(self, data):
        # Making sure the username always matches the email
        email = data.get('email', None)
        if email:
            data['username'] = email
        return data



class UserBalanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['pk', 'email', 'username', 'wallet_address', 'balance']



class UpdateBalanceSerializer(serializers.ModelSerializer):


    token_amount = serializers.SerializerMethodField()

    def get_token_amount(self, obj):
        return obj.balance


    class Meta:
        model = User
        fields = ['email', 'username', 'wallet_address', 'token_amount']

