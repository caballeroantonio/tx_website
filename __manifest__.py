# -*- coding: utf-8 -*-
{
	'name':						'Website customization',
	'summary':'''
tx website
	''',
	'description': '''
	Ajusta las vistas del website
	license:	CC BY-NC-ND 4.0
	''',
	'author':					'caballeroantonio',
	'website':					'http://caballeroantonio.ddns.net',
	'category':					'Website',
	'version':					'1.0',
	'depends': [
									'web',
									'website',
	],
	'external_dependencies':	{'python': []},
	'data': [
								'security/res.groups.xml',
								'security/ir.model.access.csv',
								'views/contactus.xml',
								'views/company_name.xml',								
	],
	'demo': [
	],
	'auto_install':				False,
	'price':					169,
	'currency':					'USD',
	'application':				False,
	'installable':				True,
	'license':					'Other proprietary',
	'maintainer':				'caballeroantonio@hotmail.com',
}
