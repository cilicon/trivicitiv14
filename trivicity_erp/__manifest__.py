{
    # App information
    'name': 'Trivicity ERP',
    'version': '14.0.0',
    'license': 'OPL-1',    
    'author': u'Silentinfotech Pvt. Ltd.',
    'website': '',
    # Dependencies
    'depends': ['base', 'sale'],
    
    # Views
    'init_xml': [],
    'data': [
        'view/crm_tag_view.xml',
        'view/res_partner_view.xml',    
             ],
    'demo_xml': [],
    
    # Odoo Store Specific
    'images': [],
    
    'installable': True,
    'auto_install': False,
    'application' : True,
}