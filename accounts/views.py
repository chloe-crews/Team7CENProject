from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from .models import CustomUser


def home(request):
    return render(request, 'accounts/dashboard.html')


def signup(request):
    if request.method == 'POST':
        # If POST request, validate the form and create a new user using the serializer
        serializer = CustomUserSerializer(data=request.POST)

        if serializer.is_valid():
            # If form submission is valid, save the user to the database
            serializer.save()

            # Add a success message to inform the user
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('dashboard')  # Redirect to the dashboard or login page

        else:
            # If form submission is invalid, capture errors and pass them to the template for rendering
            errors = serializer.errors
            return render(request, 'accounts/signup.html', {'errors': errors})

    # Render the signup page for GET requests
    return render(request, 'accounts/signup.html')


class CreateUserView(APIView):
    def post(self, request):
        # Validate the POST request user data using the serializer.
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Return success response if the user is created successfully
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # Return error details if validation fails
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteUserView(APIView):
    def delete(self, request, user_id):
        # Retrieve the user by ID using get_object_or_404
        user = get_object_or_404(CustomUser, id=user_id)

        # Delete the user if found
        user.delete()

        # Return success message if user is found, 404 error if user does not exist.
        return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
