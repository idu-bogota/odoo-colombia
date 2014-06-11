# -*- encoding: utf-8 -*-
###############################################################################
#                                                                             #
# Copyright (C) 2014                                                          #
# David Arnold (El Aleman SAS), Hector Ivan Valencia, Juan Pablo Arias        #
#                                                                             #
#This program is free software: you can redistribute it and/or modify         #
#it under the terms of the GNU Affero General Public License as published by  #
#the Free Software Foundation, either version 3 of the License, or            #
#(at your option) any later version.                                          #
#                                                                             #
#This program is distributed in the hope that it will be useful,              #
#but WITHOUT ANY WARRANTY; without even the implied warranty of               #
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
#GNU Affero General Public License for more details.                          #
#                                                                             #
#You should have received a copy of the GNU Affero General Public License     #
#along with this program.  If not, see <http://www.gnu.org/licenses/>.        #
###############################################################################

{
    'name': 'Account Fiscal Attribute',
    'description': 'Account fiscat attribute for partner and product',
    'category': 'Account/Fiscal',
    'license': 'AGPL-3',
    'author': 'Juan Pablo Arias',
    'website': '',
    'version': '0.1',
    'depends': [
        'base',
        'account',
    ],
    'data': [
        #'views/res_partner_view.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
}