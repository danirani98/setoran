# Generated by Django 3.2.5 on 2021-07-16 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstor', '0092_auto_20210716_0601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asatidz',
            name='marhalah',
            field=models.CharField(blank=True, choices=[('Tamhidiyah', 'Tamhidiyah'), ('Idadiyah', 'Idadiyah'), ('Mahad Aly', 'Mahad Aly')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='asatidz',
            name='profile_pic',
            field=models.ImageField(blank=True, default='fotokosong.gif', upload_to=''),
        ),
        migrations.AlterField(
            model_name='asatidz',
            name='status',
            field=models.CharField(blank=True, choices=[('mahasiswa', 'mahasiswa'), ('siswa', 'siswa'), ('salaf', 'salaf')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nubzah',
            name='juz',
            field=models.CharField(blank=True, choices=[('juz 3', 'juz 3'), ('juz 2', 'juz 2'), ('takmilah', 'takmilah'), ('juz 1', 'juz 1'), ('juz 4', 'juz 4'), ('juz 5', 'juz 5')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='santri',
            name='marhalah',
            field=models.CharField(blank=True, choices=[('Tamhidiyah', 'Tamhidiyah'), ('Idadiyah', 'Idadiyah'), ('Mahad Aly', 'Mahad Aly')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='santri',
            name='status',
            field=models.CharField(blank=True, choices=[('mahasiswa', 'mahasiswa'), ('siswa', 'siswa'), ('salaf', 'salaf')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='santri',
            name='takhossus',
            field=models.CharField(blank=True, choices=[('balaghoh', 'balaghoh'), ('arudl', 'arudl'), ('qowaid fiqh', 'qowaid fiqh'), ('fathul muin', 'fathul muin'), ('nubzah', 'nubzah'), ('faroid', 'faroid'), ('fathul qorib', 'fathul qorib'), ('mantiq', 'mantiq'), ('usul fiqh', 'usul fiqh')], max_length=30, null=True),
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
            field=models.CharField(blank=True, choices=[('usul', 'usul'), ('fathul muin', 'fathul muin'), ('nubzah', 'nubzah'), ('faroid', 'faroid'), ('qowaid', 'qowaid'), ('fathul qorib', 'fathul qorib'), ('Arudl', 'Arudl'), ('mantiq', 'mantiq'), ('balaghoh', 'balaghoh')], max_length=30, null=True),
        ),
    ]
