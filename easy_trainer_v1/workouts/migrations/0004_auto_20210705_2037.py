# Generated by Django 3.2.3 on 2021-07-05 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Tytuł danego pliku', max_length=100, verbose_name='tytuł pliku')),
                ('upload', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.RemoveField(
            model_name='training',
            name='rating',
        ),
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], help_text='Rating of a training', null=True, verbose_name='Rating'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(auto_now=True, verbose_name='Data komentarza'),
        ),
        migrations.AlterField(
            model_name='training',
            name='category',
            field=models.CharField(choices=[('Amator', 'Amator'), ('Podstawowy', 'Podstawowy'), ('Średni', 'Średni'), ('Zaawansowany', 'Zaawansowany')], max_length=100),
        ),
        migrations.AlterField(
            model_name='training',
            name='date_posted',
            field=models.DateTimeField(auto_now=True, verbose_name='Data publikacji'),
        ),
        migrations.AlterField(
            model_name='training',
            name='title',
            field=models.CharField(help_text='Tytuł danego treningu', max_length=100, verbose_name='tytuł treningu'),
        ),
        migrations.AddField(
            model_name='training',
            name='media',
            field=models.ManyToManyField(blank=True, help_text='Pliki treningu', to='workouts.Media', verbose_name='Plik'),
        ),
    ]
