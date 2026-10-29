import re
from django.shortcuts import render

def login(request):
    msg = ""

    if request.method == "POST":
        u = request.POST['username']
        p = request.POST['password']

        if re.match("^[a-zA-Z]+$", u) and re.match("^[0-9]{4}$", p):
            msg = "Login Successful"
        else:
            msg = "Invalid Login"

    return render(request, "login.html", {"msg": msg})