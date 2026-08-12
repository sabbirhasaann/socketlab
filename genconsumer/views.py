from django.shortcuts import render

channels = [
    "bangladesh",
    "india",
    "nepal",
    "america",
]


def index(request):
    return render(request, "genconsumer/index.html")


def chatHome(request):
    return render(request, "genconsumer/chat_home.html", {
        "channels": channels
    })


def chat(request, channel):
    return render(request, "genconsumer/chat.html", {
        "channel": channel,
    })
