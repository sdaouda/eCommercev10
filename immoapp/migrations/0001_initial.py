# Generated by Django 4.1.2 on 2022-10-24 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('slug', models.SlugField(null=True, unique=True)),
            ],
            options={
                'verbose_name': 'categorie',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=20)),
                ('cellphone_number', models.CharField(max_length=15)),
                ('adresse', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Commodite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Precisez un detail sur le bien', max_length=30)),
                ('slug', models.SlugField(max_length=30, null=True, unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Localite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localite', models.CharField(blank=True, max_length=20, null=True)),
                ('slug', models.SlugField(max_length=20, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(db_index=True, max_length=20)),
                ('slug', models.SlugField(max_length=20, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=30, null=True, unique=True)),
                ('idVendor', models.CharField(blank=True, max_length=5, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone1', models.CharField(max_length=15)),
                ('phone2', models.CharField(blank=True, max_length=15, null=True)),
                ('phone3', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('commentaire', models.TextField(blank=True, verbose_name='D')),
                ('localite', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='immoapp.localite', verbose_name='localit??')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_index=True, max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='immoapp/service/images/')),
                ('description', models.TextField(blank=True, verbose_name='Description du service')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='immoapp.vendor')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.AddField(
            model_name='localite',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='immoapp.region'),
        ),
        migrations.CreateModel(
            name='Immobilier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('reference', models.CharField(blank=True, db_index=True, max_length=15, null=True)),
                ('slug', models.SlugField(max_length=100, null=True, unique=True)),
                ('dimmension', models.CharField(blank=True, max_length=10, null=True)),
                ('numeroParcelle', models.CharField(blank=True, default='n/a', max_length=20, null=True)),
                ('lotissement', models.CharField(blank=True, default='n/a', max_length=50, null=True)),
                ('actsession', models.CharField(blank=True, max_length=15, null=True)),
                ('imageoriginal', models.ImageField(blank=True, upload_to='immoapp/images/', verbose_name='Image')),
                ('description', models.TextField(blank=True, verbose_name='Decrire l immobilier svp')),
                ('price', models.PositiveIntegerField(verbose_name='Prix')),
                ('available', models.BooleanField(default=False)),
                ('nbChambre', models.PositiveIntegerField(verbose_name='Nombre de Chambre(s)')),
                ('nbDouche', models.PositiveIntegerField(verbose_name='Nombre de Douches(s)')),
                ('action_type', models.CharField(blank=True, choices=[('LOCATION', 'LOCATION'), ('VENTE', 'VENTE')], default='LOCATION', help_text='Vente/Location', max_length=10, verbose_name='action')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('createdBy', models.CharField(blank=True, max_length=50, null=True)),
                ('payment', models.BooleanField(default=False)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='immoapp.category')),
                ('details', models.ManyToManyField(help_text='Select a genre for this book', related_name='commodite', to='immoapp.commodite')),
                ('localite', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='immoapp.localite', verbose_name='localit??')),
                ('vendeur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='immoapp.vendor')),
            ],
            options={
                'ordering': ('-created',),
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='ImmageDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, upload_to='immoapp/img_database/')),
                ('element', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='immoapp.immobilier')),
            ],
        ),
    ]
