from django.contrib import admin
from .models import (Account, Funds, Beneficiary, Due, Notification)

admin.site.register(Account)
admin.site.register(Funds)
admin.site.register(Beneficiary)
admin.site.register(Due)
admin.site.register(Notification)
