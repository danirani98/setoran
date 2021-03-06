# Generated by Django 3.1.3 on 2021-07-09 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appstor', '0084_auto_20210709_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='asatidz',
            name='terima_setor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appstor.santri'),
        ),
        migrations.AlterField(
            model_name='asatidz',
            name='status',
            field=models.CharField(blank=True, choices=[('salaf', 'salaf'), ('mahasiswa', 'mahasiswa'), ('siswa', 'siswa')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nubzah',
            name='juz',
            field=models.CharField(blank=True, choices=[('juz 1', 'juz 1'), ('juz 5', 'juz 5'), ('juz 2', 'juz 2'), ('takmilah', 'takmilah'), ('juz 4', 'juz 4'), ('juz 3', 'juz 3')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='santri',
            name='status',
            field=models.CharField(blank=True, choices=[('salaf', 'salaf'), ('mahasiswa', 'mahasiswa'), ('siswa', 'siswa')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='santri',
            name='takhossus',
            field=models.CharField(blank=True, choices=[('balaghoh', 'balaghoh'), ('qowaid fiqh', 'qowaid fiqh'), ('nubzah', 'nubzah'), ('fathul muin', 'fathul muin'), ('arudl', 'arudl'), ('fathul qorib', 'fathul qorib'), ('mantiq', 'mantiq'), ('faroid', 'faroid'), ('usul fiqh', 'usul fiqh')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='setoran',
            name='predikat',
            field=models.CharField(blank=True, choices=[('B', 'B'), ('A', 'A'), ('C', 'C')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strarudl',
            name='predikat',
            field=models.CharField(blank=True, choices=[('B', 'B'), ('A', 'A'), ('C', 'C')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strbalaghoh',
            name='predikat',
            field=models.CharField(blank=True, choices=[('B', 'B'), ('A', 'A'), ('C', 'C')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strfaroid',
            name='predikat',
            field=models.CharField(blank=True, choices=[('B', 'B'), ('A', 'A'), ('C', 'C')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strmantiq',
            name='predikat',
            field=models.CharField(blank=True, choices=[('B', 'B'), ('A', 'A'), ('C', 'C')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strmuin',
            name='predikat',
            field=models.CharField(blank=True, choices=[('B', 'B'), ('A', 'A'), ('C', 'C')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strnubzah',
            name='predikat',
            field=models.CharField(blank=True, choices=[('B', 'B'), ('A', 'A'), ('C', 'C')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strqorib',
            name='predikat',
            field=models.CharField(blank=True, choices=[('B', 'B'), ('A', 'A'), ('C', 'C')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strqowaid',
            name='predikat',
            field=models.CharField(blank=True, choices=[('B', 'B'), ('A', 'A'), ('C', 'C')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strusul',
            name='predikat',
            field=models.CharField(blank=True, choices=[('B', 'B'), ('A', 'A'), ('C', 'C')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='takhossus',
            name='tkh',
            field=models.CharField(blank=True, choices=[('balaghoh', 'balaghoh'), ('usul', 'usul'), ('qowaid', 'qowaid'), ('nubzah', 'nubzah'), ('fathul muin', 'fathul muin'), ('fathul qorib', 'fathul qorib'), ('Arudl', 'Arudl'), ('mantiq', 'mantiq'), ('faroid', 'faroid')], max_length=30, null=True),
        ),
    ]
