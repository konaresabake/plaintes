# Generated by Django 5.1.7 on 2025-03-17 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plainte', '0003_alter_plainte_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plainte',
            name='status',
            field=models.CharField(choices=[('en attente', 'en attente'), ('en_cours', 'En cours de traitement'), ('resolu', 'Résolu')], default='en attente', max_length=20),
        ),
    ]
