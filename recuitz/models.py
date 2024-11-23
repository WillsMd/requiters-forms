from django.db import models

class User(models.Model):
    DEPARTMENT_CHOICES = [
        ('ETE', 'Electronics and Telecommunication Engineering'),
        ('CSE', 'Computer Sciences and Engineering'),
    ]
    fname = models.CharField(max_length=20, null=False, blank=False)
    mname = models.CharField(max_length=20, null=True, blank=True)
    lname = models.CharField(max_length=20, null=False, blank=False)
    regno = models.CharField(max_length=13, null=False, blank=False, unique=True)
    department = models.CharField(max_length=3, choices=DEPARTMENT_CHOICES, null=False, blank=False)

    def __str__(self):
        return f"{self.fname} {self.lname} ({self.regno})"


class Question(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="questions"
    )
    clubs = models.JSONField(
        null=True,
        blank=True,
        default=dict,
        help_text="Choose the list of clubs you are in."
    )
    motivation = models.TextField(
        null=False,
        blank=False,
        help_text="What motivates you?"
    )

    picture_choice = models.CharField(
        max_length=50,
        default="nature",
        help_text="Choose a picture."
    )
    github_link = models.URLField(
        null=True,
        blank=True,
        help_text="Provide your GitHub profile link (optional)."
    )
    skills = models.JSONField(
        null=False,
        blank=False,
        default=dict,
        help_text="Provide a list of your skills (e.g., ['Python', 'Django', 'React'])."
    )
    big_project = models.TextField(
        null=True,
        blank=True,
        help_text="Explain one big project or solution you have done."
    )
    reason_to_join = models.TextField(
        null=False,
        blank=False,
        default="I am just interested",
        help_text="Explain why you want to join."
    )



class Result(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="result")
    score = models.FloatField(null=False, blank=False, help_text="Score out of 100.")
    comments = models.TextField(null=True, blank=True)
    recruited = models.BooleanField(default=False, help_text="Recruited (Yes/No).")

    def __str__(self):
        return f"Result for {self.user}"