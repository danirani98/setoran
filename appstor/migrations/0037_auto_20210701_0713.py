# Generated by Django 3.1.3 on 2021-07-01 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstor', '0036_auto_20210701_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='santri',
            name='marhalah',
            field=models.CharField(blank=True, choices=[('Idadiyah', 'Idadiyah'), ('Tamhidiyah', 'Tamhidiyah'), ('Mahad Aly', 'Mahad Aly')], max_length=30, null=True),
        ),
    ]
