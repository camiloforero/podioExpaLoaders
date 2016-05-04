#encoding:utf-8
from __future__ import unicode_literals
from django_podio import api
from django_expa import expaApi

def mc_daily_load():
    ex_api = expaApi.ExpaApi("sebastian.ramirezc@aiesec.net")
    approved_apps = ex_api.get_past_interactions('approved', 31, 1551, False)
    load_approved_apps(approved_apps)

def load_approved_apps(approved_apps):
    p_api = api.PodioApi(15664510)
    for app in approved_apps['items']:
        attributes = {
            120998811:app['person']['first_name'],
            120998812:app['person']['last_name'],
            120998813:app['person']['email'],
            121302428:app['opportunity']['programmes'][0]['id'],
            121302001:app['person']['home_lc']['name'],
            120998814:unicode(app['person']['id']),
            120998815:unicode(app['opportunity']['id']),
            120998816:app['opportunity']['location'],
            120998817:app['opportunity']['office']['name'],
            120998822:{'start_date':app['opportunity']['earliest_start_date'].split('T')[0]},
            }
        try:
            p_api.create_item({'fields':attributes})
            print 'se ha cargado %s' % (attributes[120998813])
        except api.api.transport.TransportException as te:
            print te
            print app
