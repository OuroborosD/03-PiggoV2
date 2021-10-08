import datetime

def today_date():
    today = datetime.date.today()
    return today


def logged_user(request):
    return request.user
