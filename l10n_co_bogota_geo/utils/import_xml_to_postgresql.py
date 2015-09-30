#!/usr/bin/python
# -*- coding: utf-8 -*-
from xml.dom import minidom
import erppeek
import logging
import erppeek
import psycopg2
from optparse import OptionParser
from optparse import OptionParser

logging.basicConfig()
_logger = logging.getLogger('script')



def main():

    usage = "Importar xml a sql\nusage: %prog [options]"
    parser = OptionParser(usage)

    parser.add_option("-D", "--db_name", dest="db_name", help="OpenERP database name")
    parser.add_option("-u", "--db_user",dest="db_user",help="OpenERP database user")
    parser.add_option("-p", "--db_password", dest="db_password", help="OpenERP database password")
    parser.add_option("-s", "--host_openERP", dest="host_openERP", help="OpenERP server host", default="http://localhost")
    parser.add_option("-j", "--port_openERP", dest="port_openERP", help="OpenERP server port", default="8069")

    parser.add_option("-d", "--debug", dest="debug", help="Mostrar mensajes de debug utilize 10", default=0)

    (options, args) = parser.parse_args()
    _logger.setLevel(int(options.debug))

    if not options.db_name:
        parser.error('db_name not given')
    if not options.db_user:
        parser.error('db_user not given')
    if not options.db_password:
        parser.error('db_password not given')

    c = get_connection(options)    #Conectar con erppeek
    con = conectar(options)    #conectar con psycopg2

    ir_model_data_obj = c.model('ir.model.data')
    localidad_obj = c.model('res.country.state.city.district') 
    barrio_obj = c.model('res.country.state.city.neighborhood')
    print localidad_obj.keys()


    doc = minidom.parse("district_bogota.xml")

    def getNodeText(node):

        nodelist = node.childNodes
        result = []
        for node in nodelist:
            if node.nodeType == node.TEXT_NODE:
                result.append(node.data)
        return ''.join(result)

    records = doc.getElementsByTagName("record")
    for record in records:
            id = record.getAttribute("id")
            modulo = id.split('.')[0]
            modelo = record.getAttribute("model")
            id_externo = id.split('.')[1]
            for n in record.childNodes:
                if n.nodeType != n.TEXT_NODE:
                    name = n.getAttribute("name")
                    if name == 'geo_polygon':
                        geo_polygon = getNodeText(n)
                        ir_model_data_id = ir_model_data_obj.search([('name','=',id_externo),('module','=',modulo),('model','=',modelo)])
                        localidad_id = ir_model_data_obj.browse(ir_model_data_id[0]).res_id
                        cur = con.cursor()
                        query = "UPDATE res_country_state_city_district SET geo_polygon = 'SRID=900913;{}' WHERE id = {}".format(geo_polygon, localidad_id)
                        cur.execute(query)
    con.commit()



def get_connection(options):
    server = options.host_openERP + ':' +  options.port_openERP
    database = options.db_name
    user = options.db_user
    password = options.db_password
    insert_employee_id = False
    c = erppeek.Client(server, database, user, password)
    return c


def conectar(opts):
    _logger.debug('Contectando a BD con psycopg2 {0}'.format(opts.db_name));
    con = psycopg2.connect(
        database=opts.db_name,
        user='odoo',   #opts.db_user,
        password='odoo',    #opts.db_password,
        host='localhost',    #opts.host_openERP,
        port=5432
    )
    return con


if __name__ == '__main__':
    main()