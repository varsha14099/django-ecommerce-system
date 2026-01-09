from django.db import models
from order_management.models import Order

class Payment(models.Model):

    PAYMENT_STATUS = [
        ('PENDING', 'Pending'),
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed'),
    ]

    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    method = models.CharField(max_length=50)  # UPI, Card, COD
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='PENDING')
    paid_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Payment for Order {self.order.id} - {self.status}"
