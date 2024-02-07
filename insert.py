import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from project.models import Tutorial, Video

path = 'media/videos/'


for x in Video.objects.all():
    print(x.video)

# os.listdir(path)

# files = []


# for x in os.listdir(path):
#     print(os.path.join(path, x))
#     print(os.path.isfile(os.path.join(path, x)))
