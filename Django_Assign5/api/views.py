from django.shortcuts import render
from rest_framework import generics
from .serializers import TransactionsSerializer, CategorySerializer, UserSerializer
from .models import Transactions, Category, User
from .permissions import IsOwner
from rest_framework import permissions

class CreateTransaction(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer
    permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (
        permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save(Owner=self.request.user)  # Add owner=self.request.user

class TransactionDetailsView(generics.ListAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner)


class CreateCategory(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class ViewCategory(generics.ListAPIView):
    """/categories/ -- return a list of all the categories"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailsView(generics.ListAPIView):
    """/categories/:id -- return the detail of a specific category"""
    serializer_class = CategorySerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Category.objects.filter(id=category_id)

class UserView(generics.ListAPIView):
    """/users/ -- return a list of users"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailsView(generics.ListAPIView):
    """/users/:id/ -- return the details of a specific user"""
    serializer_class = UserSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return User.objects.filter(id=user_id)

class UserTransactionsView(generics.ListAPIView):
    """/users/:user_id/transactions -- return the list of transactions of the user"""

    serializer_class = TransactionsSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Transactions.objects.filter(Owner_id=user_id)

class TransactionsCategoryView(generics.ListAPIView):
    """categories/:category_id/transactions -- Filter the transactions based on the category"""
    serializer_class = TransactionsSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Transactions.objects.filter(Trans_Type=Category.objects.filter(id=category_id))