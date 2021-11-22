from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('online', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=32, null=True)),
                ('likes', models.IntegerField(blank=True, null=True)),
                ('content', models.CharField(blank=True, max_length=1024, null=True)),
                ('image', models.CharField(blank=True, max_length=1024, null=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('imageFile', models.ImageField(blank=True, null=True, upload_to='images')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lazy_dev_api.user')),
