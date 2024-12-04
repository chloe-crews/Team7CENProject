from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomUserSerializer, CostumeSerializer
from .models import CustomUser, Costume


def home(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)  # Log the user in
            return redirect('costume_list')  # Redirect to the costume list page
        else:
            messages.error(request, 'Invalid email or password.')  # Show error if authentication fails

    return render(request, 'accounts/login.html')  # Render the login page for GET requests


def signup(request):
    if request.method == 'POST':
        # Extract form data
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check for conflicts
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'A user with this email already exists.')
        elif CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'A user with this username already exists.')
        else:
            try:
                # Create new user
                CustomUser.objects.create_user(email=email, username=username, password=password)
                messages.success(request, 'Account created successfully! You can now log in.')
                return redirect('login')  # Redirect to login upon successful sign up
            except Exception as e:
                messages.error(request, f'An unexpected error occurred: {e}')
    
    # Render the signup page with potential error messages
    return render(request, 'accounts/signup.html')


@login_required
def costume_list(request):
    costumes = Costume.objects.filter(available=True).order_by('-date_listed')  # Fetch available costumes
    return render(request, 'accounts/costumes/costume_list.html', {'costumes': costumes})


class CreateUserView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteUserView(APIView):
    def delete(self, request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)
        user.delete()
        return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


def user_profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    costumes = user.costumes.all().order_by('-date_listed')  # Explicitly order the costumes
    paginator = Paginator(costumes, 5)  # Show 5 costumes per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'accounts/user_profile.html', {'user': user, 'costumes': page_obj})


class AddCostumeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Add the currently logged-in user as the owner of the costume
        data = request.data.copy()
        data['owner'] = request.user.id  # Automatically associate the logged-in user
        serializer = CostumeSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
