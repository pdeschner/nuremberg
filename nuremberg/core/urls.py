from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^transcripts/', include('nuremberg.transcripts.urls')),
    url(r'^documents/', include('nuremberg.documents.urls')),
    url(r'^search/', include('nuremberg.search.urls')),
    url(r'^', include('nuremberg.content.urls')),
]

handler400 = 'nuremberg.core.views.handler400'
handler403 = 'nuremberg.core.views.handler403'
handler404 = 'nuremberg.core.views.handler404'
handler500 = 'nuremberg.core.views.handler500'