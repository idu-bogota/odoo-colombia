# -*- encoding: utf-8 -*-
# #############################################################################
#
# OpenERP, Open Source Management Solution
# Copyright (C) Odoo Colombia (Community).
# Author        David Arnold (devCO)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# #############################################################################

from openerp import models, fields, api, _


class ResPartnerRazonsocial(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    state = fields.Selection(
        (('pernat', 'Persona Natural'), ('perjur', 'Persona Juridica')),
        default='perjur', copy=False)
    legal_denomination = fields.Char(compute='_copy_values')
    legal_entity_name = fields.Char(
        required=True,
        states={'pernat': [('invisible', True),('required', False)]}
    )
    firstname = fields.Char(
        required=True,
        states={'perjur': [('invisible', True),('required', False)]}
    )
    middlename = fields.Char(
        required=True,
        states={'perjur': [('invisible', True),('required', False)]}
    )
    first_lastname = fields.Char(
        required=True,
        states={'perjur': [('invisible', True),('required', False)]}
    )
    second_lastname = fields.Char(
        required=True,
        states={'perjur': [('invisible', True,('required', False))]}
    )

    @api.v8
    @api.depends(
        'legal_entity_name',
        'firstname',
        'middlename',
        'first_lastname',
        'second_lastname'
    )
    def _copy_values(self):
        if self.state = 'perjur':
            self.legal_denomination = self.legal_entity_name
        else:
            s1 = self.firstname and self.firstname + ' ' or ''
            s2 = self.middlename and self.middlename + ' ' or ''
            s3 = self.first_lastname and self.first_lastname + ' ' or ''
            s4 = self.second_lastname and self.second_lastname or ''
            self.legal_denomination = s1 + s2 + s3 + s4