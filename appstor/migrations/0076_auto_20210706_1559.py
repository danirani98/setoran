# Generated by Django 3.1.3 on 2021-07-06 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstor', '0075_auto_20210706_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='nubzah',
            name='halaman',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='nubzah',
            name='juz',
            field=models.CharField(blank=True, choices=[('juz 5', 'juz 5'), ('juz 1', 'juz 1'), ('takmilah', 'takmilah'), ('juz 4', 'juz 4'), ('juz 2', 'juz 2'), ('juz 3', 'juz 3')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='santri',
            name='jk',
            field=models.CharField(blank=True, choices=[('perempuan', 'perempuan'), ('laki-laki', 'laki-laki')], max_length=20, null=True),
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
            field=models.CharField(blank=True, choices=[('usul fiqh', 'usul fiqh'), ('balaghoh', 'balaghoh'), ('mantiq', 'mantiq'), ('qowaid fiqh', 'qowaid fiqh'), ('faroid', 'faroid'), ('nubzah', 'nubzah'), ('fathul qorib', 'fathul qorib'), ('arudl', 'arudl'), ('fathul muin', 'fathul muin')], max_length=30, null=True),
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
            field=models.CharField(blank=True, choices=[('balaghoh', 'balaghoh'), ('mantiq', 'mantiq'), ('usul', 'usul'), ('faroid', 'faroid'), ('nubzah', 'nubzah'), ('qowaid', 'qowaid'), ('fathul qorib', 'fathul qorib'), ('Arudl', 'Arudl'), ('fathul muin', 'fathul muin')], max_length=30, null=True),
        ),
    ]
