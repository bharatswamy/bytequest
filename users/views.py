from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegistrationForm, UserProfileForm, LoginForm
import requests
from allauth.socialaccount.models import SocialAccount, SocialToken


def register_user(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            password = user_form.cleaned_data["password"]
            user.set_password(password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect("profile")  # Redirect to dashboard or desired page
    else:
        user_form = UserRegistrationForm()
        profile_form = UserProfileForm()
    return render(
        request,
        "registration/register.html",
        {"user_form": user_form, "profile_form": profile_form},
    )


def login_user(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            authenticate(username=username, password=password)
            return redirect("profile")
        else:
            # print("errored")
            # print(login_form.errors)
            return render(
                request,
                "registration/login.html",
                {"error_message": "Incorrect Username or Password"},
            )
    else:
        login_form = LoginForm()
        context = {"login_form": login_form}
        return render(request, "registration/login.html", context=context)


def logout_user(request):
    logout(request)
    return render(request, "registration/login.html")


def user_profile(request):
    user = request.user
    return render(
        request,
        "registration/profile.html",
    )


def fetch_facebook_user_profile(request):
    try:
        facebook_account = SocialAccount.objects.get(
            provider="facebook", user=request.user
        )
    except SocialAccount.DoesNotExist:
        # Handle case where the user has not connected their Facebook account
        # Redirect to connect Facebook account or display a message
        print("account doesnt exist")
    else:
        try:
            access_token = facebook_account.socialtoken_set.get(
                account=facebook_account
            ).token

            # Make an API request to Facebook Graph API's 'me' endpoint
            graph_api_url = f"https://graph.facebook.com/me"
            params = {
                "fields": "id,name,email",  # Fields you want to retrieve
                "access_token": access_token,
            }
            response = requests.get(graph_api_url, params=params)

            if response.status_code == 200:
                # Parse and use the retrieved user profile data
                user_profile = response.json()
                # Example: Print user profile data
                print(user_profile)
            else:
                # Handle API request error
                # Redirect, display a message, or perform error handling
                print("social token not found")
        except SocialToken.DoesNotExist:
            # Handle case where the access token is missing or expired
            # Redirect to reconnect Facebook account or display a message
            print("nothing found")
