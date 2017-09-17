# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')
#
# import django
# django.setup()
#
# from AppTwo.models import Users
# from faker import Faker
#
# fakegen = Faker()
#
#
# def populate(N=5):
#     for entry in range(N):
#
#         fake_first_name, fake_last_name = fakegen.name().split()[:2]
#         fake_email = fakegen.email()
#
#         user = Users.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)[0]
#
# if __name__ == '__main__':
#     print("populating script!")
#     populate(20)
#     print("populating complete")
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

from AppTwo.models import Users
from faker import Faker

fakegen = Faker()

def populate(N=5):

    for entry in range(N):
        fake_first_name, fake_last_name = fakegen.name().split()[:2]
        fake_email = fakegen.email()

        user = Users.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name, email=fake_email)[0]

if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete")
