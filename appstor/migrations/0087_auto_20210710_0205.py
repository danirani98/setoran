# Generated by Django 3.1.3 on 2021-07-09 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appstor', '0086_auto_20210709_2223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asatidz',
            name='terima_setor',
        ),
        migrations.AddField(
            model_name='setoran',
            name='ustad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='appstor.asatidz'),
        ),
        migrations.AlterField(
            model_name='asatidz',
            name='marhalah',
            field=models.CharField(blank=True, choices=[('Mahad Aly', 'Mahad Aly'), ('Tamhidiyah', 'Tamhidiyah'), ('Idadiyah', 'Idadiyah')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='asatidz',
            name='status',
            field=models.CharField(blank=True, choices=[('mahasiswa', 'mahasiswa'), ('siswa', 'siswa'), ('salaf', 'salaf')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nubzah',
            name='juz',
            field=models.CharField(blank=True, choices=[('juz 3', 'juz 3'), ('juz 1', 'juz 1'), ('juz 2', 'juz 2'), ('takmilah', 'takmilah'), ('juz 4', 'juz 4'), ('juz 5', 'juz 5')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='santri',
            name='marhalah',
            field=models.CharField(blank=True, choices=[('Mahad Aly', 'Mahad Aly'), ('Tamhidiyah', 'Tamhidiyah'), ('Idadiyah', 'Idadiyah')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='santri',
            name='status',
            field=models.CharField(blank=True, choices=[('mahasiswa', 'mahasiswa'), ('siswa', 'siswa'), ('salaf', 'salaf')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='santri',
            name='takhossus',
            field=models.CharField(blank=True, choices=[('faroid', 'faroid'), ('fathul muin', 'fathul muin'), ('usul fiqh', 'usul fiqh'), ('qowaid fiqh', 'qowaid fiqh'), ('balaghoh', 'balaghoh'), ('arudl', 'arudl'), ('fathul qorib', 'fathul qorib'), ('mantiq', 'mantiq'), ('nubzah', 'nubzah')], max_length=30, null=True),
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
            field=models.CharField(blank=True, choices=[('faroid', 'faroid'), ('qowaid', 'qowaid'), ('fathul muin', 'fathul muin'), ('usul', 'usul'), ('balaghoh', 'balaghoh'), ('fathul qorib', 'fathul qorib'), ('Arudl', 'Arudl'), ('mantiq', 'mantiq'), ('nubzah', 'nubzah')], max_length=30, null=True),
        ),
    ]
