# Generated by Django 3.2.5 on 2021-07-14 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstor', '0089_auto_20210712_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asatidz',
            name='marhalah',
            field=models.CharField(blank=True, choices=[('Mahad Aly', 'Mahad Aly'), ('Tamhidiyah', 'Tamhidiyah'), ('Idadiyah', 'Idadiyah')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='nubzah',
            name='juz',
            field=models.CharField(blank=True, choices=[('juz 1', 'juz 1'), ('juz 5', 'juz 5'), ('takmilah', 'takmilah'), ('juz 2', 'juz 2'), ('juz 3', 'juz 3'), ('juz 4', 'juz 4')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='santri',
            name='marhalah',
            field=models.CharField(blank=True, choices=[('Mahad Aly', 'Mahad Aly'), ('Tamhidiyah', 'Tamhidiyah'), ('Idadiyah', 'Idadiyah')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='santri',
            name='takhossus',
            field=models.CharField(blank=True, choices=[('mantiq', 'mantiq'), ('usul fiqh', 'usul fiqh'), ('arudl', 'arudl'), ('nubzah', 'nubzah'), ('fathul muin', 'fathul muin'), ('balaghoh', 'balaghoh'), ('qowaid fiqh', 'qowaid fiqh'), ('faroid', 'faroid'), ('fathul qorib', 'fathul qorib')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='setoran',
            name='predikat',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strarudl',
            name='predikat',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strbalaghoh',
            name='predikat',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strfaroid',
            name='predikat',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strmantiq',
            name='predikat',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strmuin',
            name='predikat',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strnubzah',
            name='predikat',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strqorib',
            name='predikat',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strqowaid',
            name='predikat',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strusul',
            name='predikat',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='takhossus',
            name='tkh',
            field=models.CharField(blank=True, choices=[('mantiq', 'mantiq'), ('usul', 'usul'), ('Arudl', 'Arudl'), ('qowaid', 'qowaid'), ('nubzah', 'nubzah'), ('fathul muin', 'fathul muin'), ('balaghoh', 'balaghoh'), ('faroid', 'faroid'), ('fathul qorib', 'fathul qorib')], max_length=30, null=True),
        ),
    ]
