from django.db import models

class FlightItinerary(models.Model):
    trip_id = models.CharField(max_length=50, primary_key=True, verbose_name="رمز الرحلة")
    flight_number = models.CharField(max_length=20, verbose_name="رقم الرحلة")
    Passport_Number = models.CharField(max_length=20, verbose_name="رقم الجواز")
    departure_city = models.CharField(max_length=100, verbose_name="مدينة المغادرة")
    arrival_city = models.CharField(max_length=100, verbose_name="مدينة الوصول")
    departure_date = models.DateField(verbose_name="تاريخ المغادرة")
    arrival_date = models.DateField(verbose_name="تاريخ الوصول")
    airline = models.CharField(max_length=100, verbose_name="الخطوط الجوية")
    seat_preference = models.CharField(
        max_length=50,          
        choices=[           
            ('window', 'مقعد نافذة'),
            ('aisle', 'مقعد ممر'),              
            ('middle', 'مقعد وسط'),         
        ],      
        verbose_name="تفضيل المقعد"
    )
    travel_class = models.CharField(
        max_length=50,
        choices=[
            ('economy', 'الدرجة الاقتصادية'),
            ('business', 'درجة رجال الأعمال'),
            ('first', 'الدرجة الأولى'),
        ],
        verbose_name="فئة السفر"
    )
    number_of_passengers = models.PositiveIntegerField(default=1, verbose_name="عدد المسافرين")
    passenger_name = models.CharField(max_length=100, verbose_name="اسم المسافر")
    passenger_age = models.IntegerField(verbose_name="عمر المسافر")
    passenger_gender = models.CharField(
        max_length=10,
        choices=[
            ('male', 'ذكر'),
            ('female', 'أنثى'),
        ],
        verbose_name="جنس المسافر"
    )
    destination_name = models.CharField(max_length=100, verbose_name="اسم الوجهة")
    destination_description = models.TextField(blank=True, null=True, verbose_name="وصف الوجهة")
    day_1_activity = models.TextField(verbose_name="النشاط في اليوم الأول", blank=True, null=True)
    day_2_activity = models.TextField(verbose_name="النشاط في اليوم الثاني", blank=True, null=True)
    day_3_activity = models.TextField(verbose_name="النشاط في اليوم الثالث", blank=True, null=True)
    day_4_activity = models.TextField(verbose_name="النشاط في اليوم الرابع", blank=True, null=True)
    day_5_activity = models.TextField(verbose_name="النشاط في اليوم الخامس", blank=True, null=True)
    day_6_activity = models.TextField(verbose_name="النشاط في اليوم السادس", blank=True, null=True)
    day_7_activity = models.TextField(verbose_name="النشاط في اليوم السابع", blank=True, null=True)
    transport_type = models.CharField(max_length=100, verbose_name="نوع النقل", blank=True, null=True)
    transport_departure_location = models.CharField(max_length=100, verbose_name="مكان مغادرة النقل", blank=True, null=True)
    transport_arrival_location = models.CharField(max_length=100, verbose_name="مكان وصول النقل", blank=True, null=True)
    transport_departure_time = models.DateTimeField(verbose_name="وقت مغادرة النقل", blank=True, null=True)
    transport_arrival_time = models.DateTimeField(verbose_name="وقت وصول النقل", blank=True, null=True)
    cost_description = models.CharField(max_length=200, verbose_name="وصف التكلفة", blank=True, null=True)
    cost_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="مبلغ التكلفة", blank=True, null=True)
    notification_message = models.TextField(verbose_name="نص الإشعار", blank=True, null=True)
    notification_sent_at = models.DateTimeField(auto_now_add=True, verbose_name="وقت إرسال الإشعار")
    special_requests = models.TextField(verbose_name="طلبات خاصة", blank=True, null=True)

    def __str__(self):
        return f"{self.passenger_name} - {self.flight_number}"