# -*- coding: utf-8 -*-
{
	'name':					'Website customization',
	'summary':'''
tx website
	''',
	'description': '''
Ajusta las vistas del website
	''',
	'author':					'caballeroantonio',
	'website':					'http://caballeroantonio.ddns.net',
	
	'category':					'Website',
	'version':					'1.0',
	
	'depends':					['base', 'website'],
	'external_dependencies': {'python': []},
	
	'data': [
		'security/res.groups.xml',
		'security/ir.model.access.csv',
		'views/views.xml',
		
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
