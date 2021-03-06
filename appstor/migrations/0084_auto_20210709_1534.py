# Generated by Django 3.1.3 on 2021-07-09 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstor', '0083_auto_20210709_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='setoran',
            name='hal',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='asatidz',
            name='marhalah',
            field=models.CharField(blank=True, choices=[('Idadiyah', 'Idadiyah'), ('Tamhidiyah', 'Tamhidiyah'), ('Mahad Aly', 'Mahad Aly')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='nubzah',
            name='juz',
            field=models.CharField(blank=True, choices=[('juz 1', 'juz 1'), ('juz 5', 'juz 5'), ('juz 3', 'juz 3'), ('juz 4', 'juz 4'), ('juz 2', 'juz 2'), ('takmilah', 'takmilah')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='santri',
            name='marhalah',
            field=models.CharField(blank=True, choices=[('Idadiyah', 'Idadiyah'), ('Tamhidiyah', 'Tamhidiyah'), ('Mahad Aly', 'Mahad Aly')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='santri',
            name='takhossus',
            field=models.CharField(blank=True, choices=[('balaghoh', 'balaghoh'), ('mantiq', 'mantiq'), ('nubzah', 'nubzah'), ('arudl', 'arudl'), ('fathul muin', 'fathul muin'), ('qowaid fiqh', 'qowaid fiqh'), ('fathul qorib', 'fathul qorib'), ('faroid', 'faroid'), ('usul fiqh', 'usul fiqh')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='setoran',
            name='predikat',
            field=models.CharField(blank=True, choices=[('C', 'C'), ('A', 'A'), ('B', 'B')], max_length=30, null=True),
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
        migrations.AlterField(
            model_name='takhossus',
            name='tkh',
            field=models.CharField(blank=True, choices=[('balaghoh', 'balaghoh'), ('usul', 'usul'), ('Arudl', 'Arudl'), ('mantiq', 'mantiq'), ('nubzah', 'nubzah'), ('fathul muin', 'fathul muin'), ('qowaid', 'qowaid'), ('fathul qorib', 'fathul qorib'), ('faroid', 'faroid')], max_length=30, null=True),
        ),
    ]
