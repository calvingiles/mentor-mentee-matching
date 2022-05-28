# Generated by Django 4.0.4 on 2022-05-28 05:58

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('event_time', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MentorRanking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('mentee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', related_query_name='%(class)s', to='programme.mentee')),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', related_query_name='%(class)s', to='programme.mentor')),
                ('programme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programme.programme')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='mentor',
            name='programme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', related_query_name='%(class)s', to='programme.programme'),
        ),
        migrations.CreateModel(
            name='MenteeRanking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('mentee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', related_query_name='%(class)s', to='programme.mentee')),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', related_query_name='%(class)s', to='programme.mentor')),
                ('programme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programme.programme')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='mentee',
            name='programme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', related_query_name='%(class)s', to='programme.programme'),
        ),
    ]
