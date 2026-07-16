from django.db import models

class Bird(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class WeightRecord(models.Model):
    bird = models.ForeignKey(
        Bird,
        on_delete=models.CASCADE
    )

    date = models.DateField()

    weight = models.DecimalField(
        max_digits=4,
        decimal_places=1
    )

    memo = models.TextField(
        blank=True
    )

    def __str__(self):
        return f"{self.bird.name} {self.date}"

class BehaviorRecord(models.Model):

    CATEGORY_CHOICES = [
        ('換羽', '換羽'),
        ('健康', '健康'),
        ('通院', '通院'),
        ('放鳥', '放鳥'),
        ('食事', '食事'),
        ('その他', 'その他'),
    ]

    bird = models.ForeignKey(
        Bird,
        on_delete=models.CASCADE
    )

    date = models.DateField()

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    memo = models.TextField()

    def __str__(self):
        return f"{self.bird.name} {self.date} {self.category}"