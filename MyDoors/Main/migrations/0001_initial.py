# Generated by Django 4.2.1 on 2023-09-26 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Default Color', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Molding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Default Shape', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Portal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Default Portal', max_length=100)),
                ('molding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.molding')),
                ('shape', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.shape')),
            ],
        ),
        migrations.AddField(
            model_name='molding',
            name='shape',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.shape'),
        ),
        migrations.CreateModel(
            name='Door',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.color')),
                ('molding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.molding')),
                ('portal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.portal')),
                ('shape', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.shape')),
            ],
        ),
    ]