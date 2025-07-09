from django.db import models
import uuid

class Offer(models.Model):
    offer_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    offer_type = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    priority = models.IntegerField(default=0)
    usage_limit = models.IntegerField(default=0)
    uses_count = models.IntegerField(default=0)
    applies_to = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Offers"
        ordering = ['-created_at']

class Discount(models.Model):
    discount_id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=255)
    discount_type = models.CharField(max_length=50, choices=[
        ('percentage', 'Percentage'),
        ('fixed_amount', 'Fixed Amount'),
    ])
    value = models.DecimalField(max_digits=10, decimal_places=2)
    min_purchase_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    max_purchase_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.discount_id})"

    class Meta:
        verbose_name_plural = "Discounts"
        ordering = ['-created_at']

class OfferDiscount(models.Model):
    offer_discount_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='offer_discounts')
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, related_name='offer_discounts')

    def __str__(self):
        return f"Offer '{self.offer.name}' linked to Discount '{self.discount.name}'"

    class Meta:
        verbose_name_plural = "Offer Discounts"
        unique_together = (('offer', 'discount'),) 
        ordering = ['offer']






class OfferProduct(models.Model):
    offer_product_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='offer_products')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, related_name='offer_products')

    def __str__(self):
        return f"Offer '{self.offer.name}' includes Product '{self.product.name}'"

    class Meta:
        verbose_name_plural = "Offer Products"
        unique_together = (('offer', 'product'),) 
        ordering = ['offer']
