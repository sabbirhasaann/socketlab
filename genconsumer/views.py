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
    if channels.count(channel) == 1:
        return render(request, "genconsumer/chat.html", {
            "channel": channel,
        })
    return render(request, "genconsumer/404.html")
