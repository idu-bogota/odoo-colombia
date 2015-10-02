Instalar geospatial
===================

sudo pip install shapely
sudo pip install geojson

sudo apt-get install postgis postgresql-9.3-postgis-2.1

Correr en postresql dentro de la base de datos a usar:

CREATE EXTENSION postgis;
CREATE EXTENSION postgis_topology;

git clone https://github.com/OCA/geospatial.git

Incluirlo en --addons-path



Importar xml a postgresql
=========================

Para importar los poligonos de barrios y localidades a postgresql:

Se corre el Script import_xml_to_postgresql.p con los siguientes parametros:
-D nombre de la base de datos
-u usuario odoo
-p password odoo
-s host odoo
-j puerto odoo
-U usuario postgresql
-P password postgresql
-S host postgresql
-J puerto postgresql

Ejemplo:
python utils/import_xml_to_postgresql.py -D odoo_idu_pqrs -u admin -p admin -s "http://localhost" -j 8069 -U odoo -P odoo -S "localhost" -J 5432

Este Script importara los archivos data/district_bogota.xml y data/neighborhood_bogota.xml.