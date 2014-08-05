# -*- encoding: utf-8 -*-
##############################################################################
#
# OpenERP, Open Source Management Solution
# Copyright (C) Odoo Colombia (Community).
# Authors       Hector Ivan Valencia (TIX)
#               David Arnold (devCO)
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
##############################################################################

{
    'name': 'Legally registered Name on partners.',
    'description': """
* Set the full legally registered Name of the Company.
* Set the full name as by legal requirements of a natural commercial person.
""",
    'category': 'Localization',
    'license': 'AGPL-3',
    'author': 'Hector Ivan Valencia (TIX), David Arnold BA HSG (devCO)',
    'website': '',
    'version': '0.8',
    'depends': [
        'base',
    ],
    'data': [
        'res_partner_razonsocial_view.xml',
    ],
    'demo': [
        #,
    ],
    'test': [
        #,
    ],
    'installable': True,
    'auto_install': False,
}