from django.contrib import admin
from .models import CovidCase


# Register your models here.


class AdminCovidCase(admin.ModelAdmin):
    list_display = ["id", "case_id", "age", "gender", "nationality", "imported_local", "status", "date_of_confirmation",
                    "date_of_discharge"
                    ]
    list_filter = ["gender", "nationality", "imported_local", "status", "date_of_confirmation", "date_of_discharge"]
    search_fields = ["id", "casE_id", ]


admin.site.register(CovidCase, AdminCovidCase)
