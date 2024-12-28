from django.db import models

class CropPrice(models.Model):
    STATE_CHOICES = [
        ('AP', 'Andhra Pradesh'),
        ('TG', 'Telangana'),
        ('KL', 'Kerala'),
    ]
    
    commodity = models.CharField(max_length=100)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    modal_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    
    class Meta:
        unique_together = ('commodity', 'state', 'date')
    
    def __str__(self):
        return f"{self.commodity} - {self.state} - {self.date}"

class PricePrediction(models.Model):
    crop_price = models.ForeignKey(CropPrice, on_delete=models.CASCADE)
    predicted_date = models.DateField()
    predicted_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        unique_together = ('crop_price', 'predicted_date')
    
    def __str__(self):
        return f"{self.crop_price.commodity} - {self.predicted_date}"
