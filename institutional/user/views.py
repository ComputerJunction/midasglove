from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from .models import AppleTest, BeaIndustry, Cik, Cusip, Form13F, IndustryValues, SicNaics

def table_process(dit):

    headers = list(dit['columns'])

    data = list(dit['data'])


    return {'data':data, 'headers':headers}


def landing(request):

    return render(request, 'landing.html')

class cik(ListView):

    template_name = './html/cik.html'

    model = Cik

    def get_queryset(self):
        return Cik.objects.filter(investor__icontains='Apple')


class cik_single(ListView):

    template_name = './html/cik_single.html'

    model = Cusip

    def get_queryset(self, *args, **kwargs):

        pk = self.kwargs['id']

        return Cusip.objects.filter(cik_id=pk)


class industry(ListView):

    template_name = './html/industry.html'

    model = BeaIndustry


class industry_single(ListView):

    template_name = './html/industry_single.html'

    model = IndustryValues

    def get_queryset(self, *args, **kwargs):

        pk = self.kwargs['id']

        return IndustryValues.objects.filter(industry_id=pk)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        pk = self.kwargs['id']

        context['industry_name'] = BeaIndustry.objects.get(id = pk)

        return context

class ii(ListView):

    template_name = './html/ii.html'

    model = Form13F

    def get_queryset(self, *args, **kwargs):

        return Form13F.objects.filter(cusip_id=1)[:3]


class ii_single(ListView):

    #Limit to 1 for testing

    template_name = './html/ii_single.html'

    model = Form13F


class ii_double(ListView):

    #Limit to 1 for testing

    template_name = './html/ii_double.html'

    #model = Form13F

    def get_queryset(self, *args, **kwargs):

        pk = self.kwargs['cik']

        return Form13F.objects.filter(cik=pk).order_by('id')[:3]


class sic_naics(ListView):

    template_name = './html/sic_naics.html'

    model = SicNaics



def apple(request):

    context = AppleTest.graph()

    return render(request, './html/apple.html', {'context':context})



