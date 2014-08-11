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
    _inherit = 'res.partner'

    @api.one
    @api.depends(
        'legal_entity_name',
        'firstname',
        'middlename',
        'first_lastname',
        'second_lastname'
    )
    def _copy_values(self):
        title = self.title.shortcut and ' ' + self.title.shortcut or ''
        if self.state == 'perjur':
            name = self.legal_entity_name and self.legal_entity_name or ''
            self.legal_denomination = name + title
        elif self.state == 'pernat':
            s1 = self.firstname and self.firstname + ' ' or ''
            s2 = self.middlename and self.middlename + ' ' or ''
            s3 = self.first_lastname and self.first_lastname + ' ' or ''
            s4 = self.second_lastname and self.second_lastname or ''
            self.legal_denomination = s1 + s2 + s3 + s4 + title
        else:
            self.legal_denomination = ''

    state = fields.Selection(
        (
            ('pernat', 'Persona Natural'),
            ('perjur', 'Persona Juridica')
        ),
        copy=False
    )
    legal_denomination = fields.Char(
        string=u'Legal Name',
        readonly=True,
        store=True,
        compute='_copy_values'
    )
    legal_entity_name = fields.Char(
        states={
            'perjur': [('required', True)],
            'pernat': [('invisible', True)],
            False: [('invisible', True)]
        }
    )
    firstname = fields.Char(
        states={
            'pernat': [('required', True)],
            'perjur': [('invisible', True)],
            False: [('invisible', True)]
        }
    )
    middlename = fields.Char(
        states={
            'perjur': [('invisible', True)],
            False: [('invisible', True)]
        }
    )
    first_lastname = fields.Char(
        states={
            'pernat': [('required', True)],
            'perjur': [('invisible', True)],
            False: [('invisible', True)]
        }
    )
    second_lastname = fields.Char(
        states={
            'perjur': [('invisible', True)],
            False: [('invisible', True)]
        }
    )

    # Override from res.partner
    @api.multi
    def onchange_type(self, is_company):
        value = {}
        value['title'] = False
        if is_company:
            value['use_parent_address'] = False
            domain = {'title': [('domain', '=', 'partner')]}
        else:
            domain = {'title': [('domain', '=', 'contact')]}
            value['state'] = False
        return {'value': value, 'domain': domain}
