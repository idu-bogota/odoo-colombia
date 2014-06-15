# -*- encoding: utf-8 -*-
###############################################################################
#                                                                             #
# Copyright (C) 2014                                                          #
# David Arnold (El Aleman SAS), Hector Ivan Valencia, Juan Pablo Arias        #
#                                                                             #
# This program is free software: you can redistribute it and/or modify        #
# it under the terms of the GNU Affero General Public License as published by #
# the Free Software Foundation, either version 3 of the License, or           #
# (at your option) any later version.                                         #
#                                                                             #
# This program is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of              #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
# GNU Affero General Public License for more details.                         #
#                                                                             #
# You should have received a copy of the GNU Affero General Public License    #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
###############################################################################

from openerp.osv import orm, fields

# Define an extencible city model.


class res_city(orm.Model):
    _name = 'res.country.state.city'
    _description = 'Ciudad'
    # TODO: make sure, that ste and country are consistent, if state is filled.
    _columns = {
        'name': fields.char('Ciudad', size=64, required=True),
        'state_id': fields.many2one('res.country.state', 'Departamento'),
        # 'zip': fields.char('ZIP', size=5),
        # 'phone_prefix': fields.char('Telephone Prefix', size=16),
        'codigo_dane': fields.char('Codigo DANE', size=5),
        'country_id': fields.many2one('res.country', 'Country'),
        # 'cadaster_code': fields.char('Cadaster Code', size=16),
        # 'web_site': fields.char('Web Site', size=64),
    }

    def onchange_res_city_state(self, cr, uid, ids, state_id, context=None):
        if state_id:
            country_id = self.pool['res.country.state'].browse(cr, uid, state_id, context).country_id.id
            return {'value': {'country_id': country_id}}
        return {}


class res_partner(orm.Model):
    _inherit = 'res.partner'

    _columns = {

        'city': fields.many2one(
            'res.country.state.city', 'Ciudad',)
    }

    # change several fields based on the city-field.
    # @api.onchange('city')
    def onchange_city(self, cr, uid, ids, city_id, context=None):
        if city_id:
            state_id = self.pool['res.country.state.city'].browse(cr, uid, city_id, context).state_id.id
            return {'value': {'state_id': state_id}}
        return {}
