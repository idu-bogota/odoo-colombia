# -*- encoding: utf-8 -*-


from openerp import models, fields
from pygments.lexer import _inherit



class res_city_district(models.Model):
    _name = 'res.country.state.city.district'
    _inherit = 'res.country.state.city.district'

    geom = geo_fields.GeoMultiPolygon('Shape')


class res_city_neighborhood(models.Model):
    _name = 'res.country.state.city.neighborhood'
    _inherit = 'res.country.state.city.neighborhood'

    geom = geo_fields.GeoMultiPolygon('Shape')
