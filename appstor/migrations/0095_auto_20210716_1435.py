# Generated by Django 3.2.5 on 2021-07-16 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstor', '0094_auto_20210716_0723'),
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
            field=models.CharField(blank=True, choices=[('Idadiyah', 'Idadiyah'), ('Mahad Aly', 'Mahad Aly'), ('Tamhidiyah', 'Tamhidiyah')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='asatidz',
            name='profile_pic',
            field=models.ImageField(blank=True, default='fotokosong.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='asatidz',
            name='status',
            field=models.CharField(blank=True, choices=[('mahasiswa', 'mahasiswa'), ('salaf', 'salaf'), ('siswa', 'siswa')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nubzah',
            name='juz',
            field=models.CharField(blank=True, choices=[('juz 4', 'juz 4'), ('juz 2', 'juz 2'), ('juz 3', 'juz 3'), ('juz 1', 'juz 1'), ('takmilah', 'takmilah'), ('juz 5', 'juz 5')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='santri',
            name='jk',
            field=models.CharField(blank=True, choices=[('laki-laki', 'laki-laki'), ('perempuan', 'perempuan')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='santri',
            name='marhalah',
            field=models.CharField(blank=True, choices=[('Idadiyah', 'Idadiyah'), ('Mahad Aly', 'Mahad Aly'), ('Tamhidiyah', 'Tamhidiyah')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='santri',
            name='status',
            field=models.CharField(blank=True, choices=[('mahasiswa', 'mahasiswa'), ('salaf', 'salaf'), ('siswa', 'siswa')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='santri',
            name='takhossus',
            field=models.CharField(blank=True, choices=[('fathul qorib', 'fathul qorib'), ('nubzah', 'nubzah'), ('arudl', 'arudl'), ('fathul muin', 'fathul muin'), ('balaghoh', 'balaghoh'), ('faroid', 'faroid'), ('mantiq', 'mantiq'), ('qowaid fiqh', 'qowaid fiqh'), ('usul fiqh', 'usul fiqh')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='takhossus',
            name='tkh',
            field=models.CharField(blank=True, choices=[('fathul qorib', 'fathul qorib'), ('nubzah', 'nubzah'), ('usul', 'usul'), ('fathul muin', 'fathul muin'), ('balaghoh', 'balaghoh'), ('faroid', 'faroid'), ('qowaid', 'qowaid'), ('mantiq', 'mantiq'), ('Arudl', 'Arudl')], max_length=30, null=True),
        ),
    ]
