from django.http import JsonResponse
from britecore import models
from django.db.models import Value, CharField


def get_all_risk_types(request):
    return_object = {'data': []}
    all_risk_types = models.RiskType.objects.filter(company__id=1)
    for risk_type_field_type in ['GenericRiskFieldDate', 'GenericRiskFieldEnum', 'GenericRiskFieldNumber', 'GenericRiskFieldText']:
        risk_field_objects = getattr(models, risk_type_field_type).objects.filter(risk_type__in=all_risk_types)
        risk_field_objects = risk_field_objects.values('label', 'value', 'risk_type__name').annotate(type=Value(risk_type_field_type, CharField()))
        return_object['data'] += list(risk_field_objects)
    return JsonResponse(return_object)


def get_risk_type(request):
    return_object = {'data': []}
    all_risk_types = models.RiskType.objects.filter(company__id=1, id=1)
    for risk_type_field_type in ['GenericRiskFieldDate', 'GenericRiskFieldEnum', 'GenericRiskFieldNumber', 'GenericRiskFieldText']:
        risk_field_objects = getattr(models, risk_type_field_type).objects.filter(risk_type__in=all_risk_types)
        risk_field_objects = risk_field_objects.values('label', 'value', 'risk_type__name').annotate(type=Value(risk_type_field_type, CharField()))
        return_object['data'] += list(risk_field_objects)
    return JsonResponse(return_object)
    pass
