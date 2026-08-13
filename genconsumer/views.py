from django.shortcuts import render
from .models import GenChat, GenGroup

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
        group = GenGroup.objects.filter(group=channel).first()
        messages = ["Empty box"]
        if group:
            group = GenGroup.objects.get(group=channel)
            chats = GenChat.objects.filter(group=group)
            for chat in chats:
                messages.append(chat.content)

        else:
            print("Group not exists...")
            group = GenGroup(group=channel)
            group.save()
        # print("Group object...", group)

        return render(request, "genconsumer/chat.html", {
            "channel": channel,
            "messages": messages,
        })
    return render(request, "genconsumer/404.html")
