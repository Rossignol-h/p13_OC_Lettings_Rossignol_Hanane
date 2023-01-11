import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile, ProfileImage

# ====================================================== TEST PROFILE INDEX


@pytest.mark.django_db
def test_profiles_index(client):
    url = reverse('profiles:index')
    response = client.get(url)

    assert response.status_code == 200
    assert b"<title>Profiles</title>" in response.content

# ====================================================== TEST PROFILE RETRIEVE DETAILS


@pytest.mark.django_db
def test_profile_detail(client):
    user = User(
        username="MIB",
        password="meninblack",
        first_name="Will",
        last_name="Smith",
        email="w_smith@mib.com"
    )
    user.save()
    image = ProfileImage(
        image="profile.jpg"
    )
    image.save()
    profile = Profile(user=user, favorite_city="New York", image=image)
    profile.save()

    response = client.get(reverse('profiles:profile', args=["MIB"]))

    assert response.status_code == 200
    assert b"<h1>MIB</h1>" in response.content
