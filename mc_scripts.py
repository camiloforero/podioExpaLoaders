#encoding:utf-8
from __future__ import unicode_literals
from django_podio import api
from django_expa import expaApi
from django_mailTemplates import mailApi

def mc_daily_load():
    ex_api = expaApi.ExpaApi("sebastian.ramirezc@aiesec.net")
    accepted_apps = ex_api.get_past_interactions('accepted', 1, 1551, False)
    ex_api2 = expaApi.ExpaApi("futurecolombia@co.aiesec.org")
    future_colombia_apps = ex_api2.get_past_interactions('applied', 1, 1551, False, program='icx')
    print 'Loading all accepted EPs'
    load_accepted_apps(accepted_apps)
    print 'Loading Future Colombia applicants'
    load_future_colombia_eps(future_colombia_apps)
    return future_colombia_apps

def load_accepted_apps(accepted_apps):
    p_api = api.PodioApi(15664510)
    for app in accepted_apps['items']:
        attributes = {
            120998811:app['person']['first_name'],
            120998812:app['person']['last_name'],
            120998813:app['person']['email'],
            121302428:app['opportunity']['programmes'][0]['id'],
            121482024:app['person']['home_lc']['name'],
            120998814:unicode(app['person']['id']),
            120998815:unicode(app['opportunity']['id']),
            120998817:app['opportunity']['office']['name'],
            120998822:{'start_date':app['opportunity']['earliest_start_date'].split('T')[0]},
            }
        try:
            p_api.create_item({'fields':attributes})
            print 'se ha cargado %s' % (attributes[120998813])
        except api.api.transport.TransportException as te:
            print te
            print app
            try:
                print te['error']
                print te['error_description']
            except ValueError as e:
                print e
                print "El objeto tipo excepcion no sirve como diccionario"

def load_future_colombia_eps(applications):
    p_api = api.PodioApi(15735627)
    for app in applications['items']:
        attributes = {
            121611498:app['person']['first_name'],
            121611497:app['person']['last_name'],
            121611386:app['person']['email'],
            121611501:app['person']['home_lc']['name'],
            121611499:unicode(app['person']['id']),
            121611500:unicode(app['opportunity']['id']),
            121611502:app['opportunity']['office']['name'],
            }
        try:
            p_api.create_item({'fields':attributes})
            print 'se ha cargado %s' % (attributes[121611386])
            email = mailApi.MailApi('expa_future_bienvenida')
            context = {
                'name':app['person']['first_name'],
                'full_name':'%s %s' % (app['person']['first_name'], app['person']['last_name']),
                'opportunity_id':unicode(app['opportunity']['id']),
                }
            email.send_mail('futurecolombia@co.aiesec.org', app['person']['email'], context, sender_name="Future Colombia")
            print 'El correo se ha enviado exitosamente'

        except api.api.transport.TransportException as te:
            print te
            print app
            try:
                print te['error']
                print te['error_description']
            except ValueError as e:
                print e
                print "El objeto tipo excepcion no sirve como diccionario"
