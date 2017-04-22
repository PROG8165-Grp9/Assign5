from rest_framework import serializers
from .models import Transactions, Category
from django.contrib.auth.models import User


class TransactionsSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    Owner = serializers.ReadOnlyField(source='Owner.username')
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Transactions
        fields = ('id', 'Trans_Desc', 'Owner', 'Trans_Date', 'Trans_Type', 'Trans_Loc', 'Trans_Amnt')

class CategorySerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Category
        fields = ('id', 'Cate_Type', 'Cate_Desc')

class UserSerializer(serializers.ModelSerializer):
    """A user serializer to aid in authentication and authorization."""

    transactions = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Transactions.objects.all())

    class Meta:
        """Map this serializer to the default django user model."""
        model = User
        fields = ('id', 'username', 'transactions')