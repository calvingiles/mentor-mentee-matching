# Generated by Django 4.0.4 on 2022-05-22 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programme', '0007_alter_mentee_programme_alter_mentor_programme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menteeranking',
            name='mentee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to='programme.mentee'),
        ),
        migrations.AlterField(
            model_name='menteeranking',
            name='mentor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to='programme.mentor'),
        ),
        migrations.AlterField(
            model_name='mentorranking',
            name='mentee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to='programme.mentee'),
        ),
        migrations.AlterField(
            model_name='mentorranking',
            name='mentor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to='programme.mentor'),
        ),
    ]