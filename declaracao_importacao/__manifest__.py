{   # pylint: disable=C8101,C8103
    'name': "Importação DI",

    'summary': "Gerenciamento da Declaração de Importação (DI)",

    'description': "",
    'author': "Trustcode",
    'website': "http://www.trustcode.com.br",
    'category': 'purchase',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'contributors': [
        'Mackilem Van der Laan <mack.vdl@gmail.com>',
    ],
    'depends': ['purchase'],
    'data': [
        'views/declaracao_importacao.xml',
        'security/ir.model.access.csv'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
