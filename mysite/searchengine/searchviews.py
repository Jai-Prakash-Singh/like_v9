# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render
from searchengine.models import sites_table
import geoip

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from  searchengine.models import ip_country

from searchengine.models import Document
import urllib 

from django.template import Context, Template
from django.views.decorators.cache import cache_page


def search_form(request):
    #ip = get_client_ip(request)
    ip_to_db(request, "None")

    s_obj = sites_table.objects.filter(status = "A")
    d_obj = Document.objects.filter(status = "A")[0]
    #return render(request, 'searchengine_form.html', {'s_obj' : s_obj})
    return render(request, 'searchengine/searchwithcss.html', {'s_obj' : s_obj, 'd_obj': d_obj})



def search(request):
    ip_to_db(request, request.GET['q']) 
    if 'q' in request.GET and request.GET['q']:
        querrylink = "https://www.google.com/search?output=search&sclient=psy-ab&q=%s" %(request.GET['q'])
        return HttpResponseRedirect(str(querrylink))

    else:
        return HttpResponseRedirect("/searchengine-form/")



def onclickview(request, typ, site): 
    #return HttpResponse(site)
    site = urllib.unquote(site)
    #return HttpResponse(site)
    ip_to_db(request, site)
    error = []

    if str(typ) == "st":
        try:        
            s_obj = sites_table.objects.get(dimainname = site)
            return HttpResponseRedirect(s_obj.dimainlink)
        except:
	    error = True

    elif str(typ) == "vd":
        try:
            d_obj = Document.objects.get(title = str(site))
        
            return HttpResponseRedirect(d_obj.docfile.url)
        except:
            error = True
            
    if error:
        return HttpResponseRedirect("/searchengine-form/")

onclickview = cache_page(onclickview, 60 * 15)

        

    
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]

    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip



def ip_to_db(request, kwd):
    ip = get_client_ip(request)
    cont = geoip.country(ip)
    i = ip_country(ipfield = str(ip), country = cont, keyword = kwd)
    i.save()




from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from searchengine.models import Document
from searchengine.forms import DocumentForm

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('searchengine.searchviews.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response( 'list.html', {'documents': documents, 'form': form}, context_instance=RequestContext(request))
