# -*- encoding: utf-8 -*-
from openerp import models, fields
from openerp.addons.base_geoengine import geo_model
from openerp.addons.base_geoengine import fields as geo_fields


class res_city_district(geo_model.GeoModel):
    _name = 'res.country.state.city.district'
    _inherit = 'res.country.state.city.district'

    geo_polygon = geo_fields.GeoMultiPolygon('Shape')


class res_city_neighborhood(geo_model.GeoModel):
    _name = 'res.country.state.city.neighborhood'
    _inherit = 'res.country.state.city.neighborhood'

    geo_polygon = geo_fields.GeoMultiPolygon('Shape')
