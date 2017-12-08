from django.contrib import admin
from britecore import models


class RiskTypeDateInline(admin.TabularInline):
    model = models.GenericRiskFieldDate


class RiskTypeNumberInline(admin.TabularInline):
    model = models.GenericRiskFieldNumber


class RiskTypeEnumInline(admin.TabularInline):
    model = models.GenericRiskFieldEnum


class RiskTypeTextInline(admin.TabularInline):
    model = models.GenericRiskFieldText


class RiskTypeAdmin(admin.ModelAdmin):
    inlines = [RiskTypeDateInline, RiskTypeEnumInline, RiskTypeTextInline, RiskTypeNumberInline]


class CompanyAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Company, CompanyAdmin)
admin.site.register(models.RiskType, RiskTypeAdmin)
