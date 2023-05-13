{
    'name': "Survey Update",
    'summary': """
        Qzhub Assets module adding new functionality to existing asset for AstanaREC project""",

    'description': """
        Qzhub Assets module adding new functionality to existing asset for AstanaREC project
    """,

    'author': "TOO QZhub",
    'website': "https://www.qzhub.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Technical Settings',
    'version': '15.0',

    # any module necessary for this one to work correctly
    'depends': [
                'survey',
                ],
    # always loaded
    'data': [
        'views/survey_question.xml',
    ],

}
# -*- coding: utf-8 -*-
