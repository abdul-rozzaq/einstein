from django.shortcuts import render

from project.models import Tutorial, Video

# Create your views here.


def home_page(request):

    return render(request, 'index.html', {
        'tutorials': Tutorial.objects.all()
    })


def videos_page(request, pk):

    context = {
        'videos': Video.objects.filter(tutorial_id=pk)
    }

    return render(request, 'videos.html', context)


def player_page(request, pk):

    video = Video.objects.get(pk=pk)
    
    context = {
        'video': video,
        'other_videos': Video.objects.filter(tutorial=video.tutorial),
    }

    print(context)

    return render(request, 'player.html', context)
