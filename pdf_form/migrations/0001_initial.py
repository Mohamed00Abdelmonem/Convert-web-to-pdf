# Generated by Django 5.1.7 on 2025-03-23 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlightItinerary',
            fields=[
                ('trip_id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='رمز الرحلة')),
                ('flight_number', models.CharField(max_length=20, verbose_name='رقم الرحلة')),
                ('departure_city', models.CharField(max_length=100, verbose_name='مدينة المغادرة')),
                ('arrival_city', models.CharField(max_length=100, verbose_name='مدينة الوصول')),
                ('departure_date', models.DateField(verbose_name='تاريخ المغادرة')),
                ('arrival_date', models.DateField(verbose_name='تاريخ الوصول')),
                ('airline', models.CharField(max_length=100, verbose_name='الخطوط الجوية')),
                ('seat_preference', models.CharField(choices=[('window', 'مقعد نافذة'), ('aisle', 'مقعد ممر'), ('middle', 'مقعد وسط')], max_length=50, verbose_name='تفضيل المقعد')),
                ('travel_class', models.CharField(choices=[('economy', 'الدرجة الاقتصادية'), ('business', 'درجة رجال الأعمال'), ('first', 'الدرجة الأولى')], max_length=50, verbose_name='فئة السفر')),
                ('number_of_passengers', models.PositiveIntegerField(default=1, verbose_name='عدد المسافرين')),
                ('passenger_name', models.CharField(max_length=100, verbose_name='اسم المسافر')),
                ('passenger_age', models.IntegerField(verbose_name='عمر المسافر')),
                ('passenger_gender', models.CharField(choices=[('male', 'ذكر'), ('female', 'أنثى')], max_length=10, verbose_name='جنس المسافر')),
                ('destination_name', models.CharField(max_length=100, verbose_name='اسم الوجهة')),
                ('destination_description', models.TextField(blank=True, null=True, verbose_name='وصف الوجهة')),
                ('day_1_activity', models.TextField(blank=True, null=True, verbose_name='النشاط في اليوم الأول')),
                ('day_2_activity', models.TextField(blank=True, null=True, verbose_name='النشاط في اليوم الثاني')),
                ('day_3_activity', models.TextField(blank=True, null=True, verbose_name='النشاط في اليوم الثالث')),
                ('day_4_activity', models.TextField(blank=True, null=True, verbose_name='النشاط في اليوم الرابع')),
                ('day_5_activity', models.TextField(blank=True, null=True, verbose_name='النشاط في اليوم الخامس')),
                ('day_6_activity', models.TextField(blank=True, null=True, verbose_name='النشاط في اليوم السادس')),
                ('day_7_activity', models.TextField(blank=True, null=True, verbose_name='النشاط في اليوم السابع')),
                ('transport_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='نوع النقل')),
                ('transport_departure_location', models.CharField(blank=True, max_length=100, null=True, verbose_name='مكان مغادرة النقل')),
                ('transport_arrival_location', models.CharField(blank=True, max_length=100, null=True, verbose_name='مكان وصول النقل')),
                ('transport_departure_time', models.DateTimeField(blank=True, null=True, verbose_name='وقت مغادرة النقل')),
                ('transport_arrival_time', models.DateTimeField(blank=True, null=True, verbose_name='وقت وصول النقل')),
                ('cost_description', models.CharField(blank=True, max_length=200, null=True, verbose_name='وصف التكلفة')),
                ('cost_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='مبلغ التكلفة')),
                ('notification_message', models.TextField(blank=True, null=True, verbose_name='نص الإشعار')),
                ('notification_sent_at', models.DateTimeField(auto_now_add=True, verbose_name='وقت إرسال الإشعار')),
                ('special_requests', models.TextField(blank=True, null=True, verbose_name='طلبات خاصة')),
            ],
        ),
    ]
