from django.db import models
from datetime import date

class Bird(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    birthday = models.DateField(null=True, blank=True)
    welcome_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='birds/', null=True, blank=True)

    @property
    def age_display(self):
        if not self.birthday:
            return "未登録"

        today = date.today()

        years = today.year - self.birthday.year
        months = today.month - self.birthday.month

        if today.day < self.birthday.day:
            months -= 1

        if months < 0:
            years -= 1
            months += 12

        if years == 0:
            return f"生後{months}か月"

        return f"{years}歳{months}か月"
    @property
    def days_since_welcome(self):
        if not self.welcome_date:
            return None

        today = date.today()
        return (today - self.welcome_date).days

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
        ('発情', '発情'),
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

    # 📷 行動記録の写真
    photo = models.ImageField(
        upload_to='behavior_photos/',
        blank=True,
        null=True
    )


    def __str__(self):
        return f"{self.bird.name} {self.date} {self.category}"

