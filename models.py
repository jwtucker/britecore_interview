from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class RiskType(models.Model):
    name = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class GenericRiskFieldText(models.Model):
    risk_type = models.ForeignKey(RiskType, on_delete=models.CASCADE)
    label = models.CharField(max_length=50)
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class GenericRiskFieldNumber(models.Model):
    risk_type = models.ForeignKey(RiskType, on_delete=models.CASCADE)
    label = models.CharField(max_length=50)
    value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class GenericRiskFieldDate(models.Model):
    risk_type = models.ForeignKey(RiskType, on_delete=models.CASCADE)
    label = models.CharField(max_length=50)
    value = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class GenericRiskFieldEnum(models.Model):
    risk_type = models.ForeignKey(RiskType, on_delete=models.CASCADE)
    label = models.CharField(max_length=50)
    _choices = (
        ('y', 'yes'),
        ('n', 'no'),
        ('m', 'maybe')
    )
    value = models.CharField(max_length=1, choices=_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
