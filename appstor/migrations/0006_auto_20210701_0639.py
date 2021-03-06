# Generated by Django 3.1.3 on 2021-06-30 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstor', '0005_auto_20210701_0636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='santri',
            name='jk',
            field=models.CharField(blank=True, choices=[('laki-laki', 'laki-laki'), ('perempuan', 'perempuan')], max_length=20, null=True),
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
