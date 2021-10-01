# Django
from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:


    def __init__(self, get_response):
        self.get_response = get_response
