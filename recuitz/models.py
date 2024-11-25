from django.db import models

class User(models.Model):
    fname = models.CharField(max_length=20, null=False, blank=False)
    mname = models.CharField(max_length=20, null=True, blank=True)
    lname = models.CharField(max_length=20, null=False, blank=False)
    course = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        default='CEIT',
        help_text="Enter your course (e.g., CEIT, TE, etc.)."
    )
    year_of_study = models.PositiveSmallIntegerField(
        choices=[
            (1, "1st Year"),
            (2, "2nd Year"),
            (3, "3rd Year"),
            (4, "4th Year"),
        ],
        null=False,
        blank=False,
        default=1,
        help_text="Choose your year of study."
    )

    def __str__(self):
        return f"{self.fname} {self.lname}"


class Project(models.Model):
    name = models.CharField(max_length=50, unique=True)
    decription = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="questions"
    )
    project = models.ForeignKey(
        'Project',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Choose a project to join."
    )
    clubs = models.JSONField(
        null=True,
        blank=True,
        help_text="List the clubs you are in, or enter 'None' if not in any club. For other descriptions, choose 'Other' and write about yourself."
    )
    motivation = models.TextField(
        null=False,
        blank=False,
        help_text="What motivates you?"
    )
    skills = models.JSONField(
        null=False,
        blank=False,
        help_text="Provide a list of your skills (e.g., ['Python', 'Django'])."
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

    def __str__(self):
        return f"Questions for {self.user.fname} {self.user.lname}"





class Result(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="result")
    score = models.FloatField(null=False, blank=False, help_text="Score out of 100.")
    comments = models.TextField(null=True, blank=True)
    recruited = models.BooleanField(default=False, help_text="Recruited (Yes/No).")

    def __str__(self):
        return f"Result for {self.user}"