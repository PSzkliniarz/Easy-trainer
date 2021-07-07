# Generated by Django 3.2.3 on 2021-07-01 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0002_alter_training_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('comment_text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='workouts.training')),
            ],
        ),
    ]