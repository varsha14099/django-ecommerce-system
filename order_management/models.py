from django.db import models
from django.contrib.auth.models import User
from accounts.models import Branch

class Order(models.Model):

    STATUS_CHOICES = [
        ('PLACED', 'Placed'),
        ('CONFIRMED', 'Confirmed by Branch'),
        ('PACKED', 'Packed by Vendor'),
        ('SHIPPED', 'Out for Delivery'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ]

    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="customer_orders"
    )

    branch = models.ForeignKey(
        Branch, on_delete=models.SET_NULL, null=True
    )

    vendor = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="vendor_orders"
    )

    delivery_person = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="delivery_orders"
    )

    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PLACED')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.status}"
