from django.shortcuts import get_object_or_404, render
from .models import Magnit
from .models import Report

def index(request):
    magnit_list = Magnit.objects.all()
    reports_1 = Report.objects.filter(magnit_id=1)
    reports_2 = Report.objects.filter(magnit_id=2)
    reports_3 = Report.objects.filter(magnit_id=3)
    context = {'magnit_list': magnit_list, 'reports_1': reports_1, 'reports_2': reports_2, 'reports_3': reports_3 }
    return render(request, 'catalog/index.html', context)

def detail(request, mag_id):
    magnit = Magnit.objects.get(id=mag_id)
    report_1 = Report.objects.get(magnit_id=mag_id, quarter=1)
    report_2 = Report.objects.get(magnit_id=mag_id, quarter=2)
    report_3 = Report.objects.get(magnit_id=mag_id, quarter=3)
    report_4 = Report.objects.get(magnit_id=mag_id, quarter=4)
    report_profit_sum = report_1.profit + report_2.profit + report_3.profit + report_4.profit

    context = {'magnit': magnit, 'report_1': report_1, 'report_2': report_2, 'report_3': report_3, 'report_4': report_4, 'report_profit_sum': report_profit_sum }
    return render(request, 'catalog/detail.html', context)
