# © 2019 Mackilem Van der Laan, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class DeclaracaoImportacao(models.Model):
    _name = "declaracao.importacao"
    _description = "Declaração da Importação (DI)"

    name = fields.Char(
        string="Número da DI", )
    date_registro = fields.Date(
        string="Data Registro", )
    sequence = fields.Integer(
        string="Sequence")
    tag_ids = fields.Many2many(
        string="Marcadores",
        comodel_name="declaracao.tags",
        ondelete="set null",
        help="Explain your field.",)
    declaracao_line_ids = fields.One2many(
        string="Adições",
        comodel_name="declaracao.importacao.line",
        inverse_name="declaracao_id")


class DeclaracaoImportacaoLines(models.Model):
    _name = "declaracao.importacao.line"

    declaracao_id = fields.Many2one(
        string="Declaração",
        comodel_name="declaracao.importacao")
    product_id = fields.Many2one(
        string="Produto",
        comodel_name="product.product",
        ondelete="restrict")
    quantity = fields.Float(string="Quantidade")


class DeclaracaoTags(models.Model):
    _name = "declaracao.tags"
    _description = "Marcadores para DI"

    name = fields.Char(string="Descrição", )
