#encoding:utf-8
from __future__ import unicode_literals
from django_podio import api
from django_expa import expaApi

def andes_daily_load():
    ex_api = expaApi.ExpaApi("sebastian.ramirezc@aiesec.net")
    approved_apps = ex_api.get_past_interactions('approved', 24, 1395, False)
    load_approved_apps(approved_apps)

def load_approved_apps(approved_apps):
    p_api = api.PodioApi(15586895)
    for app in approved_apps['items']:
        if app['opportunity']['programmes'][0]['id'] == 1:
            attributes = {
                120335031:app['person']['first_name'],
                120836240:app['person']['last_name'],
                120836241:app['person']['email'],
                120335070:unicode(app['person']['id']),
                120335071:unicode(app['opportunity']['id']),
                120836242:app['opportunity']['location'],
                120836243:app['opportunity']['office']['name']
                }
            p_api.create_item({'fields':attributes})
    
