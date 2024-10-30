from django.contrib import admin

# Register your models here.
# from django.contrib import admin
from .models import staffreg
from .models import studentreg
from .models import department
from .models import syllabusupload
from .models import events
from .models import staff_feedback
from .models import stud_feedback
from .models import staffapplyleave
from .models import stud_applyleave
from .models import replaystaffleav
from .models import replaystudleav,Qpaperupload
admin.site.register(department)
admin.site.register(staffreg)
admin.site.register(studentreg)
admin.site.register(syllabusupload)
admin.site.register(events)
admin.site.register(staff_feedback)
admin.site.register(stud_feedback)
admin.site.register(staffapplyleave)
admin.site.register(stud_applyleave)
admin.site.register(replaystaffleav)
admin.site.register(replaystudleav)
admin.site.register(Qpaperupload)



