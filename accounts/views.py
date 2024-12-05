from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from .models import CustomUser, Costume
from .forms import CostumeForm

def home(request):
    print("Login view called")  # Debug log
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f"Email: {email}, Password: {password}")  # Debug input

        user = authenticate(request, username=email, password=password)
        if user is not None:
            print("Login successful")  # Debug success
            login(request, user)
            return redirect('costume_list')
        else:
            print("Login failed")  # Debug failure
            messages.error(request, 'Invalid email or password.')

    return render(request, 'accounts/login.html')

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
    costumes = Costume.objects.filter(available=True).order_by('-date_listed')
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

@login_required
def user_profile(request, username):
    user = get_object_or_404(CustomUser, username=username)

    if request.method == 'POST':
        display_name = request.POST.get('display_name')
        profile_picture = request.FILES.get('profile_picture')

        if display_name:
            user.display_name = display_name
        if profile_picture:
            user.profile_picture = profile_picture

        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('user_profile', username=user.username)

    # Corrected to use the related_name
    costumes = user.costumes.all()
    return render(request, 'accounts/user_profile.html', {'user': user, 'costumes': costumes})

@login_required
def add_listing(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        price_per_day = request.POST['price_per_day']
        size = request.POST['size']
        category = request.POST['category']
        image = request.FILES.get('image')  # Get the image from request.FILES

        # Save the new listing
        Costume.objects.create(
            owner=request.user,
            title=title,
            description=description,
            price_per_day=price_per_day,
            size=size,
            category=category,
            image=image  # Save the image field
        )
        return redirect('user_profile', username=request.user.username)

    return render(request, 'accounts/add_listing.html')

@login_required
def update_profile_picture(request):
    if request.method == 'POST' and request.FILES.get('profile_picture'):
        profile_picture = request.FILES['profile_picture']
        user = request.user
        user.profile_picture = profile_picture
        user.save()
        messages.success(request, 'Profile picture updated successfully!')
        return redirect('user_profile', username=user.username)

    return render(request, 'accounts/update_profile_picture.html')

@login_required
def update_profile(request, username):
    user = get_object_or_404(CustomUser, username=username)

    if request.method == 'POST':
        display_name = request.POST.get('display_name')
        profile_picture = request.FILES.get('profile_picture')

        if display_name:
            user.display_name = display_name
        if profile_picture:
            user.profile_picture = profile_picture
        user.save()
        messages.success(request, 'Your profile has been updated!')
        return redirect('user_profile', username=user.username)

    return render(request, 'accounts/update_profile.html', {
        'user': user,
    })

def costume_detail(request, pk):
    costume = get_object_or_404(Costume, pk=pk)
    return render(request, 'accounts/costumes/costume_detail.html', {'costume': costume})

@login_required
def delete_costume_confirmation(request, pk):
    costume = get_object_or_404(Costume, pk=pk)
    if request.method == 'POST':
        costume.delete()
        return redirect('costume_list')
    return render(request, 'accounts/costumes/delete_costume.html', {'costume': costume})

@login_required
def edit_costume(request, pk):
    costume = get_object_or_404(Costume, pk=pk)
    if request.method == 'POST':
        form = CostumeForm(request.POST, request.FILES, instance=costume)
        print(request.FILES)  # Debug: To see what file is being uploaded
        if form.is_valid():
            form.save()
            messages.success(request, 'Costume updated successfully!')
            return redirect('costume_detail', pk=costume.pk)
        else:
            print("Form errors:", form.errors)  # Debug: Print form errors if validation fails
    else:
        form = CostumeForm(instance=costume)
    return render(request, 'accounts/costumes/edit_costume.html', {'form': form, 'costume': costume})
