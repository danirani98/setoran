# Generated by Django 3.1.3 on 2021-07-01 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstor', '0053_auto_20210701_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='santri',
            name='marhalah',
            field=models.CharField(blank=True, choices=[('Idadiyah', 'Idadiyah'), ('Tamhidiyah', 'Tamhidiyah'), ('Mahad Aly', 'Mahad Aly')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strarudl',
            name='predikat',
            field=models.CharField(blank=True, choices=[('C', 'C'), ('B', 'B'), ('A', 'A')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strbalaghoh',
            name='predikat',
            field=models.CharField(blank=True, choices=[('C', 'C'), ('B', 'B'), ('A', 'A')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strfaroid',
            name='predikat',
            field=models.CharField(blank=True, choices=[('C', 'C'), ('B', 'B'), ('A', 'A')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strmantiq',
            name='predikat',
            field=models.CharField(blank=True, choices=[('C', 'C'), ('B', 'B'), ('A', 'A')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strmuin',
            name='predikat',
            field=models.CharField(blank=True, choices=[('C', 'C'), ('B', 'B'), ('A', 'A')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strnubzah',
            name='predikat',
            field=models.CharField(blank=True, choices=[('C', 'C'), ('B', 'B'), ('A', 'A')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strqorib',
            name='predikat',
            field=models.CharField(blank=True, choices=[('C', 'C'), ('B', 'B'), ('A', 'A')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strqowaid',
            name='predikat',
            field=models.CharField(blank=True, choices=[('C', 'C'), ('B', 'B'), ('A', 'A')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strusul',
            name='predikat',
            field=models.CharField(blank=True, choices=[('C', 'C'), ('B', 'B'), ('A', 'A')], max_length=30, null=True),
        ),
    ]
