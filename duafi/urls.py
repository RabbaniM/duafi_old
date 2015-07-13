from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from duafi import views

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'duafi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.HomeView, name='home'),
    url(r'^pastevents/$', views.PasteventsView, name='pastevents'),
    url(r'^presentevents/$', views.PresenteventsView, name='presentevents'),
    url(r'^futureevents/$', views.FutureeventsView, name='futureevents'),
    url(r'^resources/$', views.ResourcesView, name='resources'),
    url(r'^give/$', views.GiveView, name='give'),
    url(r'^givetoscholarship/$', views.GivetoscholarshipView, name='givetoscholarship'),
    url(r'^givetoduafi/$', views.GivetoduafiView, name='givetoduafi'),
    url(r'^members/$', views.MembersView, name='members'),
    url(r'^becomeamember/$', views.BecomeamemberView, name='becomeamember'),
    url(r'^membershipbenefit/$', views.MembershipbenefitView, name='membershipbenefit'),
    url(r'^currentmembers/$', views.CurrentmembersView, name='currentmembers'),
    url(r'^blog/$', views.BlogView, name='blog'),
    url(r'^aboutus/$', views.AboutusView, name='aboutus'),
    url(r'^ataglance/$', views.AtaglanceView, name='ataglance'),
    url(r'^aoi/$', views.AoiView, name='aoi'),
    url(r'^bod/$', views.BodView, name='bod'),
    url(r'^contact/$', views.ContactView, name='contact'),
    url(r'^thanks/$', views.Thanksview, name='thanks'),
    #url(r'^contact/$', views.email, name='email'),
    #url(r'^thanks/$', views.thanks, name='thanks' ),
    
)
