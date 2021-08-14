# Generated by Django 3.1.3 on 2021-07-09 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstor', '0082_auto_20210709_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='asatidz',
            name='marhalah',
            field=models.CharField(blank=True, choices=[('Mahad Aly', 'Mahad Aly'), ('Idadiyah', 'Idadiyah'), ('Tamhidiyah', 'Tamhidiyah')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='asatidz',
            name='jk',
            field=models.CharField(blank=True, choices=[('laki-laki', 'laki-laki'), ('perempuan', 'perempuan')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='asatidz',
            name='status',
            field=models.CharField(blank=True, choices=[('mahasiswa', 'mahasiswa'), ('salaf', 'salaf'), ('siswa', 'siswa')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nubzah',
            name='juz',
            field=models.CharField(blank=True, choices=[('juz 5', 'juz 5'), ('juz 4', 'juz 4'), ('juz 2', 'juz 2'), ('juz 1', 'juz 1'), ('juz 3', 'juz 3'), ('takmilah', 'takmilah')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='santri',
            name='jk',
            field=models.CharField(blank=True, choices=[('laki-laki', 'laki-laki'), ('perempuan', 'perempuan')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='santri',
            name='marhalah',
            field=models.CharField(blank=True, choices=[('Mahad Aly', 'Mahad Aly'), ('Idadiyah', 'Idadiyah'), ('Tamhidiyah', 'Tamhidiyah')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='santri',
            name='status',
            field=models.CharField(blank=True, choices=[('mahasiswa', 'mahasiswa'), ('salaf', 'salaf'), ('siswa', 'siswa')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='santri',
            name='takhossus',
            field=models.CharField(blank=True, choices=[('balaghoh', 'balaghoh'), ('nubzah', 'nubzah'), ('arudl', 'arudl'), ('fathul qorib', 'fathul qorib'), ('fathul muin', 'fathul muin'), ('mantiq', 'mantiq'), ('usul fiqh', 'usul fiqh'), ('qowaid fiqh', 'qowaid fiqh'), ('faroid', 'faroid')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='setoran',
            name='predikat',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('C', 'C'), ('B', 'B')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strarudl',
            name='predikat',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('C', 'C'), ('B', 'B')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strbalaghoh',
            name='predikat',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('C', 'C'), ('B', 'B')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strfaroid',
            name='predikat',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('C', 'C'), ('B', 'B')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strmantiq',
            name='predikat',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('C', 'C'), ('B', 'B')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strmuin',
            name='predikat',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('C', 'C'), ('B', 'B')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strnubzah',
            name='predikat',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('C', 'C'), ('B', 'B')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strqorib',
            name='predikat',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('C', 'C'), ('B', 'B')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strqowaid',
            name='predikat',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('C', 'C'), ('B', 'B')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strusul',
            name='predikat',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('C', 'C'), ('B', 'B')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='takhossus',
            name='tkh',
            field=models.CharField(blank=True, choices=[('balaghoh', 'balaghoh'), ('nubzah', 'nubzah'), ('Arudl', 'Arudl'), ('usul', 'usul'), ('fathul qorib', 'fathul qorib'), ('fathul muin', 'fathul muin'), ('mantiq', 'mantiq'), ('qowaid', 'qowaid'), ('faroid', 'faroid')], max_length=30, null=True),
        ),
    ]
