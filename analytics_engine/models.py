from django.db import models


class Tower(models.Model):
    tower_id = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=255)
    line_name = models.CharField(max_length=255)
    installation_date = models.DateField()

    def __str__(self):
        return self.tower_id


class Inspection(models.Model):
    tower = models.ForeignKey(Tower, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/')
    inspection_date = models.DateTimeField(auto_now_add=True)
    engineer_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Inspection - {self.tower.tower_id}"


class Defect(models.Model):

    SEVERITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Critical', 'Critical'),
    ]

    inspection = models.ForeignKey(Inspection, on_delete=models.CASCADE)

    defect_type = models.CharField(max_length=100)

    confidence_score = models.FloatField()

    severity = models.CharField(
        max_length=20,
        choices=SEVERITY_CHOICES
    )

    bounding_box = models.JSONField()

    detected_image = models.ImageField(
        upload_to='results/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.defect_type


class Prediction(models.Model):

    RISK_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Critical', 'Critical'),
    ]

    tower = models.ForeignKey(Tower, on_delete=models.CASCADE)

    predicted_risk = models.CharField(
        max_length=20,
        choices=RISK_CHOICES
    )

    failure_probability = models.FloatField()

    predicted_failure_date = models.DateField()

    recommendation = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.predicted_risk