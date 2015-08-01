from django import forms

class SelectChart(forms.Form):
    dic_chart = {(0,"Select"),(1,"Top 10 Videos by User Count"),(2,"Top 10 cities by User Count"),}
    dic = {(1,"Line Chart"),(2,"Pie Chart"),(3,"Both"),}
    status_chart_type = forms.ChoiceField(choices = dic, widget= forms.RadioSelect(), required = True)
    status_chart = forms.ChoiceField(choices = dic_chart, widget= forms.Select(), required = True)