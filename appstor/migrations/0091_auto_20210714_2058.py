# Generated by Django 3.2.5 on 2021-07-14 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstor', '0090_auto_20210714_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asatidz',
            name='jk',
            field=models.CharField(blank=True, choices=[('laki-laki', 'laki-laki'), ('perempuan', 'perempuan')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='asatidz',
            name='marhalah',
            field=models.CharField(blank=True, choices=[('Idadiyah', 'Idadiyah'), ('Tamhidiyah', 'Tamhidiyah'), ('Mahad Aly', 'Mahad Aly')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='asatidz',
            name='status',
            field=models.CharField(blank=True, choices=[('salaf', 'salaf'), ('siswa', 'siswa'), ('mahasiswa', 'mahasiswa')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nubzah',
            name='juz',
            field=models.CharField(blank=True, choices=[('juz 3', 'juz 3'), ('takmilah', 'takmilah'), ('juz 1', 'juz 1'), ('juz 4', 'juz 4'), ('juz 2', 'juz 2'), ('juz 5', 'juz 5')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='santri',
            name='jk',
            field=models.CharField(blank=True, choices=[('laki-laki', 'laki-laki'), ('perempuan', 'perempuan')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='santri',
            name='marhalah',
            field=models.CharField(blank=True, choices=[('Idadiyah', 'Idadiyah'), ('Tamhidiyah', 'Tamhidiyah'), ('Mahad Aly', 'Mahad Aly')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='santri',
            name='status',
            field=models.CharField(blank=True, choices=[('salaf', 'salaf'), ('siswa', 'siswa'), ('mahasiswa', 'mahasiswa')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='santri',
            name='takhossus',
            field=models.CharField(blank=True, choices=[('qowaid fiqh', 'qowaid fiqh'), ('usul fiqh', 'usul fiqh'), ('arudl', 'arudl'), ('balaghoh', 'balaghoh'), ('faroid', 'faroid'), ('mantiq', 'mantiq'), ('fathul qorib', 'fathul qorib'), ('nubzah', 'nubzah'), ('fathul muin', 'fathul muin')], max_length=30, null=True),
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
            field=models.CharField(blank=True, choices=[('usul', 'usul'), ('balaghoh', 'balaghoh'), ('Arudl', 'Arudl'), ('faroid', 'faroid'), ('mantiq', 'mantiq'), ('fathul qorib', 'fathul qorib'), ('nubzah', 'nubzah'), ('fathul muin', 'fathul muin'), ('qowaid', 'qowaid')], max_length=30, null=True),
        ),
    ]
