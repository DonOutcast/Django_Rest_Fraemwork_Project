from django.contrib import admin
from restaurants.models import Menu, Mac

classes = [Mac, Menu]

for class_ in classes:
    admin.site.register(class_)
