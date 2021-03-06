# Generated by Django 3.2.5 on 2021-08-04 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BussinessCustomer',
            fields=[
                ('bcid', models.IntegerField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=200)),
                ('cemail', models.EmailField(max_length=254)),
                ('cadd', models.CharField(max_length=200)),
                ('pwd', models.CharField(max_length=20)),
                ('cpwd', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=200)),
                ('pcost', models.DecimalField(decimal_places=4, max_digits=10)),
                ('pmfd', models.DateField(auto_now_add=True)),
                ('quantity', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('bcid', models.IntegerField()),
                ('otime', models.DateField(auto_now_add=True)),
                ('q', models.IntegerField()),
                ('p', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.product')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('ctime', models.DateField(auto_now_add=True)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.bussinesscustomer')),
                ('p', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.product')),
            ],
        ),
    ]
