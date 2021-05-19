from django.contrib import admin
from . models import Examine, FinalTest

admin.site.register([Examine, FinalTest])