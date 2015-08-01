from graphos.renderers import gchart
from django.shortcuts import render
from graphos.sources.model import ModelDataSource,SimpleDataSource
from .forms import SelectChart
from .models import WatchedVideo,User,VideoData
from django.db.models import Count
from collections import Counter
    
def delete_records():
    query = User.objects.all()
    query.delete()
    query = WatchedVideo.objects.all()
    query.delete()

def select_chart_form(request):
    form = SelectChart(request.POST)
    
    if form.is_valid():
        chart_type = str(form.cleaned_data['status_chart_type'])
        if (str(form.cleaned_data['status_chart']) == '1'):
            analysis = VideoData.objects.annotate(watches_count = Count('user')).order_by('-watches_count')[:10]
            data_source = ModelDataSource(analysis,fields=['video_name', 'watches_count'])
            column_chart = gchart.ColumnChart(data_source,options={'title': "Top 10 Videos watched by No. Of Users"})
            pie_chart = gchart.PieChart(data_source,options={'title': "Top 10 Videos watched by No. Of Users"})
            context = {
                'chart_type' : chart_type,
                'form' : form,
                "data_source": data_source,
                "column_chart": column_chart,
                "pie_chart": pie_chart,
            }
            return render(request,'chart4.html', context)
        
        if (str(form.cleaned_data['status_chart']) == '2'):
            #return HttpResponseRedirect('/chart2/')
            city_counter = Counter(User.objects.values_list('user_city', flat=True))
            top_ten_cities_and_counts = city_counter.most_common()[:10]
            graph_headher = ('City', 'User')
            top_ten_cities_and_counts.insert(0, graph_headher)
            data_source = SimpleDataSource(top_ten_cities_and_counts)
            column_chart = gchart.ColumnChart(data_source,options={'title': "Number of Users in Top 10 Cities"})
            pie_chart = gchart.PieChart(data_source,options={'title': "Number of Users in Top 10 Cities"})
            context = {
                       'chart_type' : chart_type,
                        'form' : form,
                        "data_source": data_source,
                        "column_chart": column_chart,
                        "pie_chart": pie_chart,
                       }
            return render(request,'chart4.html', context)
        
    context = {               
               'form' : form
               }
    return render(request, 'chart.html', context)