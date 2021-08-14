# Generated by Django 3.1.3 on 2021-07-01 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstor', '0066_auto_20210702_0250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='santri',
            name='tkh',
        ),
        migrations.AddField(
            model_name='santri',
            name='takhossus',
            field=models.CharField(blank=True, choices=[('nubzah', 'nubzah'), ('faroid', 'faroid'), ('Arudl', 'Arudl'), ('fathul qorib', 'fathul qorib'), ('usul', 'usul'), ('qowaid', 'qowaid'), ('mantiq', 'mantiq'), ('balaghoh', 'balaghoh'), ('fathul muin', 'fathul muin')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='juznubzah',
            name='juz',
            field=models.CharField(blank=True, choices=[('juz 4', 'juz 4'), ('juz 2', 'juz 2'), ('juz 5', 'juz 5'), ('takmilah', 'takmilah'), ('juz 1', 'juz 1'), ('juz 3', 'juz 3')], max_length=30, null=True),
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
            model_name='strarudl',
            name='predikat',
            field=models.CharField(blank=True, choices=[('C', 'C'), ('B', 'B'), ('A', 'A')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strbalaghoh',
            name='predikat',
            field=models.CharField(blank=True, choices=[('C', 'C'), ('B', 'B'), ('A', 'A')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strfaroid',
            name='predikat',
            field=models.CharField(blank=True, choices=[('C', 'C'), ('B', 'B'), ('A', 'A')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strmantiq',
            name='predikat',
            field=models.CharField(blank=True, choices=[('C', 'C'), ('B', 'B'), ('A', 'A')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strmuin',
            name='predikat',
            field=models.CharField(blank=True, choices=[('C', 'C'), ('B', 'B'), ('A', 'A')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strnubzah',
            name='predikat',
            field=models.CharField(blank=True, choices=[('C', 'C'), ('B', 'B'), ('A', 'A')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strqorib',
            name='predikat',
            field=models.CharField(blank=True, choices=[('C', 'C'), ('B', 'B'), ('A', 'A')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strqowaid',
            name='predikat',
            field=models.CharField(blank=True, choices=[('C', 'C'), ('B', 'B'), ('A', 'A')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='strusul',
            name='predikat',
            field=models.CharField(blank=True, choices=[('C', 'C'), ('B', 'B'), ('A', 'A')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='takhossus',
            name='tkh',
            field=models.CharField(blank=True, choices=[('nubzah', 'nubzah'), ('faroid', 'faroid'), ('Arudl', 'Arudl'), ('fathul qorib', 'fathul qorib'), ('usul', 'usul'), ('qowaid', 'qowaid'), ('mantiq', 'mantiq'), ('balaghoh', 'balaghoh'), ('fathul muin', 'fathul muin')], max_length=30, null=True),
        ),
    ]
