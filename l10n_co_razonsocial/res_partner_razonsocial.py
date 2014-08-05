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

    @api.v8
    @api.depends('is_company')
    def _get_fucking_company(self):
        self.is_company

    is_comp = fields.Boolean(compute='_get_fucking_company')

    state = fields.Selection(
        (('person', 'Person'), ('company', 'Company')),
        default='company', readonly=True, invisible=True, copy=False)
        # https://github.com/odoo/odoo/issues/1567
    legal_denomination = fields.Char()
    legal_entity_name = fields.Char(states={'person': [('invisible', True)]})
    firstname = fields.Char(states={'company': [('invisible', True)]})
    middlename = fields.Char(states={'company': [('invisible', True)]})
    first_lastname = fields.Char(states={'company': [('invisible', True)]})
    second_lastname = fields.Char(states={'company': [('invisible', True)]})

    @api.v8
    @api.onchange('is_comp')
    def _set_state(self):
        self.state = self.is_company and ('company', 'Company') or 'person'

    @api.v8
    @api.onchange(
        'legal_entity_name',
        'firstname',
        'middlename',
        'first_lastname',
        'second_lastname'
    )
    def _copy_values(self):
        if self.is_company:
            self.legal_denomination = self.legal_entity_name
        if not self.is_company:
            s1 = self.firstname and self.firstname + ' ' or ''
            s2 = self.middlename and self.middlename + ' ' or ''
            s3 = self.first_lastname and self.first_lastname + ' ' or ''
            s4 = self.second_lastname and self.second_lastname or ''
            self.legal_denomination = s1 + s2 + s3 + s4