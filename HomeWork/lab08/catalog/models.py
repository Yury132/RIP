from django.db import models

class Magnit(models.Model):
    address = models.CharField(max_length=50, verbose_name='Адрес')

    # def __str__(self):
    #     return self.pk
    class Meta:
        verbose_name = 'Магнит'
        verbose_name_plural = 'Магниты'

class Report(models.Model):
    magnit_id = models.ForeignKey(Magnit, on_delete=models.CASCADE, verbose_name='ID Магазина')
    quarter = models.IntegerField(default=0, verbose_name='Квартал')
    profit = models.IntegerField(default=0, verbose_name='Чистая Прибыль (тыс.руб.)')
    expense = models.IntegerField(default=0, verbose_name='Расходы (тыс.руб.)')
    products = models.IntegerField(default=0, verbose_name='Кол-во Проданных Товаров (тыс.ед.)')

    # def __str__(self):
    #     return self.quarter
    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'