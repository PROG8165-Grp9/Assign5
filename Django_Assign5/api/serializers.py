from rest_framework import serializers
from django.db.models import Q
from rest_framework.serializers import (
    EmailField,
    ModelSerializer,
    ValidationError,
    CharField
)
from .models import Transactions, Category
from django.contrib.auth.models import User

class UserCreateSerializer(ModelSerializer):
    email = EmailField(label='Email address')
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password')
        extra_kwargs = {"password":
                            {"write_only": True}
                        }
    def create(self, validated_data):
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = email
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data

class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank = True, read_only = True)
    username = CharField()
    class Meta:
        model = User
        fields = ('username','password', 'token')
        extra_kwargs = {"password":
                            {"write_only": True}
                        }
    def validate(self,data):
        user_obj = None
        username = data.get("username")
        password = data.get("password")
        user = User.objects.filter(
            Q(username = username)
        ).distinct()
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("Incorrect credentials")
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials")
        return data

class TransactionsSerializer(ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    Owner = serializers.ReadOnlyField(source='Owner.username')
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Transactions
        fields = ('id', 'Trans_Desc', 'Owner', 'Trans_Date', 'Trans_Type', 'Trans_Loc', 'Trans_Amnt')

class CategorySerializer(ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Category
        fields = ('id', 'Cate_Type', 'Cate_Desc')

class UserSerializer(ModelSerializer):
    """A user serializer to aid in authentication and authorization."""

    transactions = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Transactions.objects.all())

    class Meta:
        """Map this serializer to the default django user model."""
        model = User
        fields = ('id', 'username', 'transactions')