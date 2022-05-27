from django.contrib import admin
from django.db import models
from django.forms import Textarea

from .models import Programme, Attendee, Mentor, Mentee, Ranking, MentorRanking, \
    MenteeRanking
from gale_shapley import find_stable_match


class AttendeeInline(admin.TabularInline):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':40})},
    }
    extra = 0
    classes = []


class MentorInline(AttendeeInline):
    model = Mentor


class MenteeInline(AttendeeInline):
    model = Mentee


@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    inlines = [MentorInline, MenteeInline]
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':40})},
    }

    readonly_fields = ["left_matches", "right_matches"]

    def extract_rankings(self, instance):
        def extract_attendee(instance):
            return f"{instance.pk}: {instance.name}"
        mentor_rankings = {
            extract_attendee(mentor): [extract_attendee(rank.mentee) for rank in
                        mentor.mentorrankings.all().order_by("-rank")]
            for mentor in instance.mentors.all()
        }
        mentee_rankings = {
            extract_attendee(mentee): [extract_attendee(rank.mentor) for rank in
                        mentee.menteerankings.all().order_by("-rank")]
            for mentee in instance.mentees.all()
        }
        return mentor_rankings, mentee_rankings

    def left_matches(self, instance):
        try:
            mentor_rankings, mentee_rankings = self.extract_rankings(instance)
            oree_matches = find_stable_match(mentor_rankings, mentee_rankings)
            return sorted(oree_matches)
        except Exception as e:
            return str(e)

    def right_matches(self, instance):
        try:
            mentor_rankings, mentee_rankings = self.extract_rankings(instance)
            eeor_matches = find_stable_match(mentee_rankings, mentor_rankings)
            return sorted([orm, eem] for eem, orm in eeor_matches)
        except Exception as e:
            return str(e)


class RankingInline(admin.TabularInline):
    # formfield_overrides = {
    #     models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':40})},
    # }
    extra = 0
    classes = []
    exclude = ("programme",)

    def has_add_permission(self, request, obj):
        return False


class MentorRankingInline(RankingInline):
    model = MentorRanking
    readonly_fields = ("mentee",)

class MenteeRankingInline(RankingInline):
    model = MenteeRanking
    readonly_fields = ("mentor",)


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_filter = ("programme", )
    inlines = [MentorRankingInline]


@admin.register(Mentee)
class MenteeAdmin(admin.ModelAdmin):
    fields = []
    list_filter = ("programme", )
    inlines = [MenteeRankingInline]
