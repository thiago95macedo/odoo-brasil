# -*- coding: utf-8 -*-
# © 2009  Gabriel C. Stabel
# © 2009  Renato Lima - Akretion
# © 2016 Danimar Ribeiro, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields

PRODUCT_ORIGIN = [
    ('0', u'0 - Nacional, exceto as indicadas nos códigos 3 a 5'),
    ('1', u'1 - Estrangeira - Importação direta, exceto a indicada no código'
     ' 6'),
    ('2', u'2 - Estrangeira - Adquirida no mercado interno, exceto a indicada'
     u' no código 7'),
    ('3', u'3 - Nacional, mercadoria ou bem com Conteúdo de Importação'
     ' superior a 40% (quarenta por cento)'),
    ('4', u'4 - Nacional, cuja produção tenha sido feita em conformidade com'
     u' os processos produtivos básicos de que tratam o Decreto-Lei nº 288/67,'
     u' e as Leis nºs 8.248/91, 8.387/91, 10.176/01 e 11.484/07'),
    ('5', u'5 - Nacional, mercadoria ou bem com Conteúdo de Importação'
     u' inferior ou igual a 40% (quarenta por cento)'),
    ('6', u'6 - Estrangeira - Importação direta, sem similar nacional,'
     u' constante em lista de Resolução CAMEX'),
    ('7', u'7 - Estrangeira - Adquirida no mercado interno, sem similar'
     u' nacional, constante em lista de Resolução CAMEX'),
    ('8', u'8 - Nacional, mercadoria ou bem com Conteúdo de Importação'
     u' superior a 70%')
]


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    fiscal_type = fields.Selection(
        [('service', u'Serviço'), ('product', 'Produto')], 'Tipo Fiscal',
        required=True, default='product')

    origin = fields.Selection(PRODUCT_ORIGIN, 'Origem', default='0')

    fiscal_classification_id = fields.Many2one(
        'product.fiscal.classification', string="Classificação Fiscal (NCM)")

    service_type_id = fields.Many2one(
        'l10n_br_account.service.type', u'Tipo de Serviço')