from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world")



import datetime



#def current_datetime(request):
#    now = datetime.datetime.now()
#    html = "<html><body>It is now %s.</body></html>" % now
#    return HttpResponse(html)



from django.template import Template, Context

#def current_datetime(request):
#    now = datetime.datetime.now()
#    t = Template("<html><body>It is now {{ current_date|date:'F j, Y' }}.</body></html>")
#    html = t.render(Context({'current_date': now}))
#    return HttpResponse(html)

from django.template.loader import get_template

#def current_datetime(request):
#    now = datetime.datetime.now()
#    t = get_template('current_datetime.html')
#    html = t.render(Context({'current_date': now}))
#    return HttpResponse(html)

from django.shortcuts import render

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})


from django.http import Http404

#def hours_ahead(request, offset):
#    try:
#        offset = int(offset)
#    except ValueError:
#        raise Http404()
#    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
#    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
#    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'hours_ahead.html', {'hour_offset': offset, "next_time":dt})
