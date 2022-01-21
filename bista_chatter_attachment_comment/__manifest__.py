# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2021 (http://www.bistasolutions.com)
#
##############################################################################
{
    'name': 'Chatter Attachment Comment',
    "author": "Bista Solutions",
    "website": "https://www.bistasolutions.com",
    "support": "support@bistasolutions.com",
    'version': '15.0.0.1.0',
    'depends': ['base', 'mail'],
    'summary': "Chatter Attachment Comment",
    'description': """
        This is a full-featured chatter attachment system.
        ========================================
        
        It supports:
        ------------
            - Chatter attachment comment add and update functionality
    """,
    'category': 'Attachment',
    'demo': [
    ],
    'data': [
        'views/ir_attachment_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {
        'web.assets_backend': [
            'bista_chatter_attachment_comment/static/src/models/attachment/attachment.js',
            'bista_chatter_attachment_comment/static/src/models/thread/thread.js',
            'bista_chatter_attachment_comment/static/src/widgets/form_renderer/form_renderer.js',
            'bista_chatter_attachment_comment/static/src/components/attachment_card/attachment_card.js',
            'bista_chatter_attachment_comment/static/src/components/attachment_card/attachment_card.scss',
        ],
        'web.qunit_suite_tests': [
        ],
        'web.assets_qweb': [
            'bista_chatter_attachment_comment/static/src/components/attachment_card/attachment_card.xml',
        ],
    },
    'license': 'LGPL-3',
}

