# Generated by Django 4.2.18 on 2025-02-10 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservisas', '0005_uzsakymas_uzsakovas'),
    ]

    operations = [
        migrations.AddField(
            model_name='uzsakymas',
            name='grazinimo_terminas',
            field=models.DateField(blank=True, null=True, verbose_name='Gražinimo terminas'),
        ),
    ]
