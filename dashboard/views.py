from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import requests
from django.conf import settings

@login_required
def index(request):
    try:
        response = requests.get(settings.API_URL)
        posts = response.json()
        total_responses = len(posts)
    except Exception:
        total_responses = 0

    data = {
        "title": "Landing Page Dashboard",
        "total_responses": total_responses,
    }
    return render(request, "dashboard/index.html", data)