# its for /etc/apache2/httpd.conf

MaxRequestsPerChild 1
LoadModule python_module /usr/lib/apache2/modules/mod_python.so


<Location "/searchengine">
    SetHandler python-program
    PythonHandler django.core.handlers.modpython
    PythonPath "['/home/user/searchsite/mysite/', '/usr/local/lib/python2.7/dist-packages/django'] + sys.path"

    SetEnv DJANGO_SETTINGS_MODULE mysite.settings
    PythonDebug Off
    PythonAutoReload Off
</Location>

<Location "/static/">
    SetHandler None
</Location>

Alias /media/ /home/user/searchsite/mysite/media/
Alias /static/ /home/user/searchsite/mysite/static/

<Directory /home/user/searchsite/mysite/static/>
Order deny,allow
Allow from all
</Directory>

<Directory /home/user/searchsite/mysite/media/>
Order deny,allow
Allow from all
</Directory>

#WSGIScriptAlias / /home/user/searchsite/staticvirt/test_project/test_project/wsgi.py

<Directory /home/user/searchsite/mysite/mysite/>
<Files wsgi.py>
Order allow,deny
Allow from all
</Files>
</Directory>



rectory /home/user/searchsite/mysite/media/>
Order deny,allow
Allow from all
</Directory>

#WSGIScriptAlias / /home/user/searchsite/staticvirt/test_project/test_project/wsgi.py

<Directory /home/user/searchsite/mysite/mysite/>
<Files wsgi.py>
Order allow,deny
Allow from all
</Files>
</Directory>

