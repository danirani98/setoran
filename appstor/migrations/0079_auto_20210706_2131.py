# Generated by Django 3.1.3 on 2021-07-06 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appstor', '0078_auto_20210706_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nubzah',
            name='juz',
            field=models.CharField(blank=True, choices=[('juz 5', 'juz 5'), ('juz 1', 'juz 1'), ('juz 4', 'juz 4'), ('takmilah', 'takmilah'), ('juz 2', 'juz 2'), ('juz 3', 'juz 3')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='santri',
            name='jk',
            field=models.CharField(blank=True, choices=[('laki-laki', 'laki-laki'), ('perempuan', 'perempuan')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='santri',
            name='marhalah',
            field=models.CharField(blank=True, choices=[('Tamhidiyah', 'Tamhidiyah'), ('Idadiyah', 'Idadiyah'), ('Mahad Aly', 'Mahad Aly')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='santri',
            name='status',
            field=models.CharField(blank=True, choices=[('siswa', 'siswa'), ('mahasiswa', 'mahasiswa'), ('salaf', 'salaf')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='santri',
            name='takhossus',
            field=models.CharField(blank=True, choices=[('qowaid fiqh', 'qowaid fiqh'), ('arudl', 'arudl'), ('mantiq', 'mantiq'), ('faroid', 'faroid'), ('nubzah', 'nubzah'), ('fathul qorib', 'fathul qorib'), ('fathul muin', 'fathul muin'), ('usul fiqh', 'usul fiqh'), ('balaghoh', 'balaghoh')], max_length=30, null=True),
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
            field=models.CharField(blank=True, choices=[('qowaid', 'qowaid'), ('mantiq', 'mantiq'), ('faroid', 'faroid'), ('usul', 'usul'), ('nubzah', 'nubzah'), ('fathul qorib', 'fathul qorib'), ('fathul muin', 'fathul muin'), ('balaghoh', 'balaghoh'), ('Arudl', 'Arudl')], max_length=30, null=True),
        ),
        migrations.CreateModel(
            name='Setoran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lafadz', models.CharField(blank=True, max_length=200, null=True)),
                ('tanggal', models.DateTimeField(auto_now_add=True, null=True)),
                ('predikat', models.CharField(blank=True, choices=[('A', 'A'), ('C', 'C'), ('B', 'B')], max_length=30, null=True)),
                ('nama', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appstor.santri')),
                ('takhossus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appstor.takhossus')),
            ],
        ),
    ]
