from django.shortcuts import render

# Create your views here.


def main(request, template='app/main.html'):
    return render(request, template)