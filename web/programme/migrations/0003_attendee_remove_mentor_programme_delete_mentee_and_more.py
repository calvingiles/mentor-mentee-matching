# Generated by Django 4.0.4 on 2022-05-17 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programme', '0002_mentor_mentee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('role', models.TextField(choices=[('Mentor', 'Mentor'), ('Mentee', 'Mentee')])),
                ('programme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programme.programme')),
            ],
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='programme',
        ),
        migrations.DeleteModel(
            name='Mentee',
        ),
        migrations.DeleteModel(
            name='Mentor',
        ),
    ]
