#encoding:utf-8
from __future__ import unicode_literals
from django_podio import api
from django_expa import expaApi

def andes_daily_load():
    ex_api = expaApi.ExpaApi("sebastian.ramirezc@aiesec.net")
    accepted_apps = ex_api.get_past_interactions('accepted', 1, 1395, False)
    load_accepted_apps(accepted_apps)
    approved_apps = ex_api.get_past_interactions('approved', 1, 1395, False)
    load_approved_apps(approved_apps)
    approved_igcdp_apps = ex_api.get_past_interactions('approved', 1, 1395, False, program='icx')
    load_approved_icx_eps(approved_igcdp_apps)
    #new_visitors = ex_api.get_past_interactions('registered', 1, 1395, False)

def load_accepted_apps(accepted_apps):
    for app in accepted_apps['items']:
        p_api = api.PodioApi(15586895)
        attributes = {
            120335031:app['person']['first_name'],
            120836240:app['person']['last_name'],
            120836241:app['person']['email'],
            123886690:app['opportunity']['programmes'][0]['short_name'],
            120335070:unicode(app['person']['id']),
            120335071:unicode(app['opportunity']['id']),
            120836243:app['opportunity']['office']['name'],
            124730925:app['opportunity']['title'], #Nombre del proyecto
            }
        p_api.create_item({'fields':attributes})
        print "Se ha agregado a %s al espacio de OGCDP" % app['person']['email']
        #elif app['opportunity']['programmes'][0]['id'] == 2:#FOr GIP
        #    p_api = api.PodioApi(15812927)
        #    attributes = {
        #        122297408:app['person']['first_name'],
        #        122297409:app['person']['last_name'],
        #        122297410:app['person']['email'],
        #        122297411:unicode(app['person']['id']),
        #        122297412:unicode(app['opportunity']['id']),
        #        122297414:app['opportunity']['office']['name']
        #        }
        #    p_api.create_item({'fields':attributes})
        #    print "Se ha agregado a %s al espacio de OGIP" % app['person']['email']

def load_approved_apps(approved_apps):
    for app in approved_apps['items']:
        p_api = api.PodioApi(15998856)
        attributes = {
            123889165:app['person']['first_name'],
            123889166:app['person']['last_name'],
            123889167:app['person']['email'],
            123889168:app['opportunity']['programmes'][0]['short_name'],
            123889169:unicode(app['person']['id']),
            123889170:unicode(app['opportunity']['id']),
            123889171:app['opportunity']['office']['name'],
            124789464:app['opportunity']['title'], #Nombre del proyecto
            }
        p_api.create_item({'fields':attributes})
        print "Se ha agregado a %s al espacio de OGX de EPs aprobados" % app['person']['email']

def email_new_visitors(new_visitors):
    email = mailApi.MailApi('correo_nuevos_inscritos')


def load_approved_icx_eps(applications):
    p_api = api.PodioApi(15886643)
    for app in applications['items']:
        attributes = {
            122922712:app['person']['first_name'],
            122923595:app['person']['last_name'],
            122923598:app['person']['email'],
            122923596:app['opportunity']['programmes'][0]['short_name'], #Programa
            122923597:unicode(app['person']['id']), #Trainee EXPA ID
            122923599:app['opportunity']['title'], #Nombre del proyecto
            122923600:unicode(app['opportunity']['id']), #Nombre del trainee
            122923601:app['person']['home_lc']['name'], #LC origen
            122923604:app['person']['home_lc']['country'], #País origen
            }
        try:
            p_api.create_item({'fields':attributes})

        except api.api.transport.TransportException as te:
            print te
            print app
            try:
                print te['error']
                print te['error_description']
            except ValueError as e:
                print e
                print "El objeto tipo excepcion no sirve como diccionario"

