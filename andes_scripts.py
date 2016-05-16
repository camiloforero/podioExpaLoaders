#encoding:utf-8
from __future__ import unicode_literals
from django_podio import api
from django_expa import expaApi

def andes_daily_load():
    ex_api = expaApi.ExpaApi("sebastian.ramirezc@aiesec.net")
    approved_apps = ex_api.get_past_interactions('approved', 1, 1395, False)
    load_approved_apps(approved_apps)
    #new_visitors = ex_api.get_past_interactions('registered', 1, 1395, False)

def load_approved_apps(approved_apps):
    for app in approved_apps['items']:
        if app['opportunity']['programmes'][0]['id'] == 1:#For GCDP
            p_api = api.PodioApi(15586895)
            attributes = {
                120335031:app['person']['first_name'],
                120836240:app['person']['last_name'],
                120836241:app['person']['email'],
                120335070:unicode(app['person']['id']),
                120335071:unicode(app['opportunity']['id']),
                120836243:app['opportunity']['office']['name']
                }
            #p_api.create_item({'fields':attributes})
            print "Se ha agregado a %s al espacio de OGCDP" % app['person']['email']
        elif app['opportunity']['programmes'][0]['id'] == 2:#FOr GIP
            p_api = api.PodioApi(15812927)
            attributes = {
                122297408:app['person']['first_name'],
                122297409:app['person']['last_name'],
                122297410:app['person']['email'],
                122297411:unicode(app['person']['id']),
                122297412:unicode(app['opportunity']['id']),
                122297414:app['opportunity']['office']['name']
                }
            p_api.create_item({'fields':attributes})
            print "Se ha agregado a %s al espacio de OGIP" % app['person']['email']

def email_new_visitors(new_visitors):
    email = mailApi.MailApi('correo_nuevos_inscritos')
