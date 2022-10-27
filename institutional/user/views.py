from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from .models import AppleTest, BeaIndustry, Cik, Cusip, CikCusip, Form, IndustryValues, MicroTest, NumTest, SicNaics

def table_process(dit):

    headers = list(dit['columns'])

    data = list(dit['data'])


    return {'data':data, 'headers':headers}


def landing(request):

    return render(request, 'landing.html')

def apple(request):

    context = AppleTest.graph()

    return render(request, './html/apple.html', {'context':context})

def micro(request):

    context = MicroTest.graph()

    return render(request, './html/apple.html', {'context':context})

class nums(ListView):

    template_name = './html/nums.html'

    model = NumTest

    def get_context_data(self, **kwargs):

        context = NumTest.table()

        return context


class cik(ListView):

    template_name = './html/cik.html'

    model = Cik

    def get_queryset(self):
        return Cik.objects.filter(investor__icontains='Apple')


class cik_single(ListView):

    template_name = './html/cik_single.html'

    model = CikCusip

    def get_queryset(self, *args, **kwargs):

        pk = self.kwargs['id']

        return CikCusip.objects.filter(cik_id=pk)

    #def get_context_data(self, **kwargs):

        #context = super().get_context_data(**kwargs)

        #pk = self.kwargs['id']

        #context['industry_name'] = BeaIndustry.objects.get(id = pk)

        #return context

class form_entries(ListView):

    template_name = './html/form_entries.html'

    model = Form

    def get_queryset(self, *args, **kwargs):

        pk = self.kwargs['id']

        return Form.objects.filter(cik_id=pk)[:30]


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

class investor(ListView):

    template_name = './html/investor.html'

    model = Cik

    def get_queryset(self, *args, **kwargs):

        return Cik.objects.exclude(investors__isnull=True)


class sic_naics(ListView):

    template_name = './html/sic_naics.html'

    model = SicNaics





