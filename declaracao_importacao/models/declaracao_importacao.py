# © 2019 Mackilem Van der Laan, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class DeclaracaoImportacao(models.Model):
    _name = "declaracao.importacao"
    _description = "Declaração da Importação (DI)"

    name = fields.Char(
        string="Número da DI", )
    date_register = fields.Date(string="Data de Registro")
    date_picking = fields.Date(string="Data de Embarque", )
    seller_id = fields.Many2one(
        string="Fornecedor",
        comodel_name="res.partner",
        domain="[('supplier', '!=', False), ('is_company', '!=', False)]",
        ondelete="restrict")
    gross_weight_total = fields.Float(
        string="Peso Bruto Total",)
    net_weight_total = fields.Float(
        string="Peso Liquido Total",)
    freight_currency_id = fields.Many2one(
        string="Moeda Frete",
        comodel_name="res.currency",
        domain="[('active', '!=', False)]",
        ondelete="set null")
    insurance_currency_id = fields.Many2one(
        string="Moeda Seguro",
        comodel_name="res.currency",
        domain="[('active', '!=', False)]",
        ondelete="set null")
    freight_total = fields.Float(string="Valor do Frete", )
    insurance_total = fields.Float(string="Valor do Seguro", )
    amount_total = fields.Float(string="Valor Total", )

    product_line_ids = fields.One2many(
        string="Produtos",
        comodel_name="declaracao.product.line",
        inverse_name="declaracao_id")


class DeclaracaoProductLines(models.Model):
    _name = "declaracao.product.line"

    declaracao_id = fields.Many2one(
        string="DI",
        comodel_name="declaracao.importacao")
    product_id = fields.Many2one(
        string="Produto",
        comodel_name="product.product",
        ondelete="restrict")
    quantity = fields.Float(string="Quantidade")
    price_unit = fields.Float(string="Preço Unit.")
    price_subtotal = fields.Float(string="Subtotal.")
    currency_id = fields.Many2one(
        string="Moeda",
        comodel_name="res.currency",
        domain="[('active', '!=', False)]")
