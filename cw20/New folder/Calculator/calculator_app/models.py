
from django.db import models

class Calculation(models.Model):
    operation = models.CharField(max_length=10)
    operand_a = models.FloatField()
    operand_b = models.FloatField()
    result = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.operand_a} {self.operation} {self.operand_b} = {self.result}"
