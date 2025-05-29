from django.http import HttpResponse, HttpResponseNotFound

month_challenges = {
    "january": "New year resolutions.",
    "february": "2nd month blues.",
    "march": "3rd month blues.",
    "april": "We've all been fooled."
}

def monthly_challenges(request, month):
    try:
        challenge_text = month_challenges[month.lower()]
        return HttpResponse(challenge_text)
    except KeyError:
        return HttpResponseNotFound("This month is not supported")
