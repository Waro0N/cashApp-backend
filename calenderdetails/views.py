from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView
)
from cashflow.models import CashFlow
from .serializer import CalenderSerializer
from rest_framework.response import Response
# Create your views here.
class CalenderDetails(ListAPIView):
    queryset = CashFlow.objects.all()
    serializer_class = CalenderSerializer

    def get(self, request, *args, **kargs):
        queryset = CashFlow.objects.all()
        events=[]
        if 'created_by' in self.request.GET:
            created_by = self.request.GET['created_by']
            queryset=queryset.filter(created_by=created_by)

            for i in queryset:
                if i.debit > 0:
                    title = f"Debit: {i.debit}"
                if i.debit ==0:
                    title = f"Credit: {i.credit}"
                event = {
                    "start": i.date.strftime('%Y-%m-%d'),
                    "title" : title
                }
                events.append(event)


        # serializer = self.get_serializer(queryset, many=True)
        # data=serializer.data
        # comp_data={}
        # credit_data={}
        # for i in data:
        #     date = i['date']
        #     debit_item= i['debit']
        #     credit_item = i['credit']
        #     if date in comp_data:
        #         comp_data[date] += debit_item
        #     else:
        #         comp_data[date] = debit_item
        
        #     if debit_item == 0:
        #         if date in credit_data:
        #             credit_data[date] += credit_item
        #         else:
        #             credit_data[date] = credit_item
        # print(comp_data)
        # print(credit_data)
        # results = [{'start': cal_date , 'title': 'Debit: ' + str(total)} for cal_date, total in comp_data.items() ]

        return Response(events)