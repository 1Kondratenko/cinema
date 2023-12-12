from django.contrib import admin

from .models import (
    Actor,
    Genre,
    Cinema,
    MovieSession,
    Movie,
    Ticket,
    Order,
)

admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(MovieSession)
admin.site.register(Cinema)
admin.site.register(Ticket)
admin.site.register(Order)
admin.site.register(Movie)
