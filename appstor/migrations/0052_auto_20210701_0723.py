# Generated by Django 3.1.3 on 2021-07-01 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstor', '0051_auto_20210701_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='santri',
            name='marhalah',
            field=models.CharField(blank=True, choices=[('Mahad Aly', 'Mahad Aly'), ('Tamhidiyah', 'Tamhidiyah'), ('Idadiyah', 'Idadiyah')], max_length=30, null=True),
        ),
    ]
