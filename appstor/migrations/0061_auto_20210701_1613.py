# Generated by Django 3.1.3 on 2021-07-01 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstor', '0060_auto_20210701_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juznubzah',
            name='juz',
            field=models.CharField(blank=True, choices=[('takmilah', 'takmilah'), ('juz 5', 'juz 5'), ('juz 3', 'juz 3'), ('juz 2', 'juz 2'), ('juz 4', 'juz 4'), ('juz 1', 'juz 1')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='santri',
            name='marhalah',
            field=models.CharField(blank=True, choices=[('Idadiyah', 'Idadiyah'), ('Mahad Aly', 'Mahad Aly'), ('Tamhidiyah', 'Tamhidiyah')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strarudl',
            name='predikat',
            field=models.CharField(blank=True, choices=[('C', 'C'), ('A', 'A'), ('B', 'B')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strbalaghoh',
            name='predikat',
            field=models.CharField(blank=True, choices=[('C', 'C'), ('A', 'A'), ('B', 'B')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strfaroid',
            name='predikat',
            field=models.CharField(blank=True, choices=[('C', 'C'), ('A', 'A'), ('B', 'B')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strmantiq',
            name='predikat',
            field=models.CharField(blank=True, choices=[('C', 'C'), ('A', 'A'), ('B', 'B')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strmuin',
            name='predikat',
            field=models.CharField(blank=True, choices=[('C', 'C'), ('A', 'A'), ('B', 'B')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strnubzah',
            name='predikat',
            field=models.CharField(blank=True, choices=[('C', 'C'), ('A', 'A'), ('B', 'B')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strqorib',
            name='predikat',
            field=models.CharField(blank=True, choices=[('C', 'C'), ('A', 'A'), ('B', 'B')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strqowaid',
            name='predikat',
            field=models.CharField(blank=True, choices=[('C', 'C'), ('A', 'A'), ('B', 'B')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strusul',
            name='predikat',
            field=models.CharField(blank=True, choices=[('C', 'C'), ('A', 'A'), ('B', 'B')], max_length=30, null=True),
        ),
    ]
