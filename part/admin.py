from django.contrib import admin
from .models import Bed
from .models import Bath
from .models import Door
from .models import Dressroom
from .models import Kitchen
from .models import Livingroom
from .models import Veranda


admin.site.register(Bed)
admin.site.register(Bath)
admin.site.register(Door)
admin.site.register(Dressroom)
admin.site.register(Kitchen)
admin.site.register(Livingroom)
admin.site.register(Veranda)
