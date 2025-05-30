from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january":"Eat no meat for entire month.",
    "february":"Walk for atleast 20 minutes everyday.",
    "march":"Learn Django for at least 20 minutes everyday.",
    "april":"Eat no meat for entire month.",
    "may":"Walk for atleast 20 minutes everyday.",
    "june":"Learn Django for at least 20 minutes everyday.",
    "july":"Eat no meat for entire month.",
    "august":"Walk for atleast 20 minutes everyday.",
    "september":"Learn Django for at least 20 minutes everyday.",
    "october":"Eat no meat for entire month.",
    "november":"Walk for atleast 20 minutes everyday.",
    "december":"Learn Django for at least 20 minutes everyday."
}

def monthly_challenge_by_number(request,month):
    try:
        months = list(monthly_challenges.keys())
        redirect_month = months[month-1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("This month not supported.")


def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("This month not supported.")
        
    