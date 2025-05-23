# Generated by Django 5.1.4 on 2024-12-14 21:39

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ban',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banso', models.IntegerField(unique=True)),
                ('tinhtrangban', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten', models.CharField(max_length=100)),
                ('mota', models.CharField(choices=[('starter', 'Khai vị'), ('main', 'Món chính'), ('dessert', 'Tráng miệng')], default='main', max_length=50)),
                ('gia', models.DecimalField(decimal_places=2, max_digits=10)),
                ('chi_phi', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tinhtrang', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('chucvu', models.CharField(choices=[('quanly', 'Quản Lý'), ('bep', 'Bếp'), ('phucvu', 'Phục Vụ'), ('admin', 'Admin')], default='phucvu', max_length=20)),
                ('groups', models.ManyToManyField(related_name='customuser_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='customuser_set', to='auth.permission')),
            ],
            options={
                'verbose_name': 'Nhân viên',
                'verbose_name_plural': 'Nhân viên',
                'db_table': 'rm_customuser',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='LichLamViec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngay', models.DateField()),
                ('ca', models.CharField(choices=[('sang', 'Sáng'), ('chieu', 'Chiều')], max_length=20)),
                ('giovao', models.DateTimeField(blank=True, null=True)),
                ('giora', models.DateTimeField(blank=True, null=True)),
                ('nhanvien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenKhach', models.CharField(default='Khách lẻ', max_length=100)),
                ('ngay', models.DateTimeField(auto_now_add=True)),
                ('ngay_thanh_toan', models.DateTimeField(blank=True, null=True)),
                ('tinhtrang', models.BooleanField(default=False)),
                ('ban', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rm.ban')),
                ('nhanvien_phucvu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='Nhân viên phục vụ')),
            ],
        ),
        migrations.CreateModel(
            name='ChiTietOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soluong', models.PositiveIntegerField()),
                ('gia', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tinhtrang', models.CharField(choices=[('chua_len', 'Chưa lên món'), ('da_len', 'Đã lên món'), ('da_nhan', 'Đã nhận món')], default='chua_len', max_length=10, verbose_name='Trạng thái')),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rm.menu')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='rm.order')),
            ],
        ),
        migrations.AddConstraint(
            model_name='customuser',
            constraint=models.UniqueConstraint(fields=('username', 'email'), name='unique_user'),
        ),
        migrations.AddConstraint(
            model_name='lichlamviec',
            constraint=models.CheckConstraint(condition=models.Q(('giora__gt', models.F('giovao')), ('giovao__isnull', True), ('giora__isnull', True), _connector='OR'), name='check_giora_giovao'),
        ),
        migrations.AddConstraint(
            model_name='lichlamviec',
            constraint=models.UniqueConstraint(fields=('nhanvien', 'ngay', 'ca'), name='unique_employee_shift'),
        ),
    ]
