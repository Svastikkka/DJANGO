import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "seventh_project.settings")

import django

django.setup()

# Fake population script
import random
from seventh_app.models import AccessRecord, Topic, Webpage
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'News', 'Games', 'Marketplace']


def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        # get the topic for the entry
        fake_top = add_topic()
        # Create fake data
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create fake webpage entry
        webpg = Webpage.objects.get_or_create(topic=fake_top, url=fake_url, name=fake_url)[0]

        # Create fake access records
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


if __name__ == '__main__':
    print('populating script')
    populate(20)
    print('populating complete')
