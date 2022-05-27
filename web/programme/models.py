from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Programme(models.Model):
    name = models.TextField()
    event_time = models.DateTimeField()

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Attendee(models.Model):
    programme = models.ForeignKey(
        Programme,
        on_delete=models.CASCADE,
        related_name="%(class)ss",
        related_query_name="%(class)s"
    )
    name = models.TextField()
    email = models.EmailField()
    # role = models.TextField(choices=[('Mentor', 'Mentor'), ('Mentee', 'Mentee')])

    def __repr__(self):
        return self.name
    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Mentor(Attendee):
    pass


class Mentee(Attendee):
    pass


class Ranking(models.Model):
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_query_name="%(class)s", related_name="%(class)ss")
    mentee = models.ForeignKey(Mentee, on_delete=models.CASCADE, related_query_name="%(class)s", related_name="%(class)ss")
    rank = models.IntegerField(
        null=True,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )

    class Meta:
        abstract = True


class MentorRanking(Ranking):
    pass


class MenteeRanking(Ranking):
    pass


@receiver(post_save, sender=Mentor)
def create_default_rankings(sender, instance, created, **kwargs):
    if created:
        MenteeRanking.objects.bulk_create(
            [
                MentorRanking(mentor=instance, mentee=mentee, programme=instance.programme)
                for mentee in instance.programme.mentees.all()
            ]
        )
        MentorRanking.objects.bulk_create(
            [
                MentorRanking(mentor=instance, mentee=mentee, programme=instance.programme)
                for mentee in instance.programme.mentees.all()
            ]
        )


@receiver(post_save, sender=Mentee)
def create_default_rankings(sender, instance, created, **kwargs):
    if created:
        MenteeRanking.objects.bulk_create(
            [
                MentorRanking(mentor=mentor, mentee=instance, programme=instance.programme)
                for mentor in instance.programme.mentors.all()
            ]
        )
        MentorRanking.objects.bulk_create(
            [
                MentorRanking(mentor=mentor, mentee=instance, programme=instance.programme)
                for mentor in instance.programme.mentors.all()
            ]
        )

