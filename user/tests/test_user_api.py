import pytest

from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status

CREATE_USER_URL = reverse('user:create')
TOKEN_URL = reverse('user:token')
ADM_URL = reverse('user:adm')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


#Tests the public endpoint for unauthenticated users
@pytest.mark.django_db
class TestPublicUserApi:


    #Tests creating user with valid payload is successful
    def test_create_valid_user_success(self, client):

        payload = {
            'email': 'test@example.com',
            'password': 'testpass',
            'name': 'Test Name',
        }
        res = client.post(CREATE_USER_URL, payload)
        created_user = get_user_model().objects.get(email=payload['email'])

        # check the response status code
        assert res.status_code == status.HTTP_201_CREATED

        # check that the user is created in the db
        assert created_user.check_password(payload['password'])

        # check that the password is not returned in the response
        assert 'password' not in res.data

    #Test ensures creating a user that already exists fails
    def test_user_with_email_already_exists(self, client):


        payload = {
            'email': 'test@example.com',
            'password': 'testpass',
            'name': 'Test Name',
        }
        create_user(**payload)
        res = client.post(CREATE_USER_URL, payload)

        assert res.status_code == status.HTTP_400_BAD_REQUEST

    #Test for password length,must be more than 5 characters
    def test_password_too_short(self, client):

        payload = {
            'email': 'test@example.com',
            'password': 'pw',
            'name': 'Test Name',
        }
        res = client.post(CREATE_USER_URL, payload)
        user_exists = get_user_model().objects.filter(
            email=payload['email'],
        ).exists()

        assert res.status_code == status.HTTP_400_BAD_REQUEST
        assert not user_exists

    #Test that a token is created for the user
    def test_create_token_for_user(self, client):

        user_details = {
            'email': 'test@example.com',
            'name': 'Test Name',
            'password': 'testpass',
        }

        create_user(**user_details)

        payload = {
            'email': user_details['email'],
            'password': user_details['password'],
        }

        res = client.post(TOKEN_URL, payload)

        assert res.status_code == status.HTTP_200_OK
        assert 'token' in res.data

    #Test token is not created for invalid credentials
    def test_create_token_invalid_credentials(self, client):

        create_user(email='test@example.com', password='testpass')

        payload = {
            'email': 'wrong_email@example.com',
            'password': 'wrong_password',
        }

        res = client.post(TOKEN_URL, payload)

        assert res.status_code == status.HTTP_400_BAD_REQUEST
        assert 'token' not in res.data

    #Test that token is not created if user doesn't provide password
    def test_create_token_with_blank_password(self, client):

        payload = {
            'email': 'test@example.com',
            'password': '',
        }

        res = client.post(TOKEN_URL, payload)

        assert res.status_code == status.HTTP_400_BAD_REQUEST
        assert 'token' not in res.data

    #Test that authentication is required
    def test_retrieve_user_unauthorized(self, client):

        res = client.get(ADM_URL)

        assert res.status_code == status.HTTP_401_UNAUTHORIZED



#Test the private endpoints for authenticated users
@pytest.mark.django_db
class TestPrivateUserApi:

    #Test retrieving profile for logged in user
    def test_retrieve_user_success(self, authenticated_client, normal_user):

        res = authenticated_client.get(ADM_URL)

        assert res.status_code == status.HTTP_200_OK
        assert res.data == {
            'name': normal_user.name,
            'email': normal_user.email,
        }

    #Test that POST is not allowed on the adm url
    def test_post_adm_not_allowed(self, authenticated_client):

        res = authenticated_client.post(ADM_URL, {})

        assert res.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    #Test updating the user for authenticated user
    def test_update_user(self, authenticated_client, normal_user):

        payload = {
            'name': 'new name',
            'password': 'newpassword',
        }

        res = authenticated_client.patch(ADM_URL, payload)
        normal_user.refresh_from_db()

        assert res.status_code == status.HTTP_200_OK
        assert normal_user.name == payload['name']
        assert normal_user.check_password(payload['password'])
