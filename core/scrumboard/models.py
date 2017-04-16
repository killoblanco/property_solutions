from django.db import models


# Create your models here.

class Requirements(models.Model):
    TYPE_CH = (
        ("New (Whole new)", "New (Whole new)"),
        ("Feature", "Feature"),
        ("Bug", "Bug"),
        ("Release", "Release"),
        ("Hot Fix (Bug in Prod)", "Hot Fix (Bug in Prod)"),
    )
    PRIOR_CH = ((n, n) for n in range(1, 6))

    detail = models.TextField()
    type = models.CharField(max_length=22, choices=TYPE_CH)
    priority = models.IntegerField(choices=PRIOR_CH)
    deadline = models.DateField()

    def __str__(self):
        return self.detail
