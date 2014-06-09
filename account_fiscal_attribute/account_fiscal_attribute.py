# -*- encoding: utf-8 -*-
##############################################################################
#
# OpenERP, Open Source Management Solution
# Copyright (C) 2004-2009 Tiny SPRL (&amp;lt;http://tiny.be&amp;gt;).
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
# along with this program. If not, see &amp;lt;http://www.gnu.org/licenses/&amp;gt;.
#
##############################################################################

from openerp.osv import orm, fields

class fiscal_domain(orm.Model):
	_name = "fiscal_domain"
	#_rec_name  = "domain"

	_columns = {
		'code' : fields.char('code', size=25, required=True),
		'note' : fields.text('note'),
		'active' : fields.boolean('active'),
		#account_fiscal_attribute_id = fields.many2many
		#account_fiscal_allocation_set_id = fields.many2many
		#tax_id = fields.many2many
	}

class attribute_use(orm.Model):
	_name = "attribute_use"
	#_rec_name  = "attribute"

	_columns = {
		'code' : fields.char('code',size=25, required=True),
		'active' : fields.boolean('active'),
		#account_fiscal_attribute_id = fields.many2many
	}

# class account_fiscal_attribute_partner(osv.osv):
# 	_name = 'account_fiscal_attribute.partner'
# 	_rec_name = 'attribute_partner'

# 	_columns = {

# 	}