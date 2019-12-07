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
    currency_id = fields.Many2one(
        string="Moeda",
        comodel_name="res.currency",
        domain="[('active', '!=', False)]",
        ondelete="set null")
    currency_fee = fields.Float(string="Câmbio")
    freight_currency_id = fields.Many2one(
        string="Moeda Frete",
        comodel_name="res.currency",
        domain="[('active', '!=', False)]",
        ondelete="set null")
    freight_currency_fee = fields.Float(string="Câmbio Frete")
    insurance_currency_id = fields.Many2one(
        string="Moeda Seguro",
        comodel_name="res.currency",
        domain="[('active', '!=', False)]",
        ondelete="set null")
    insurance_currency_fee = fields.Float(string="Câmbio Seguro")
    freight_total = fields.Float(
        string="Valor do Frete")
    insurance_total = fields.Float(
        string="Valor do Seguro")
    amount_subtotal = fields.Float(
        string="Subtotal",
        readonly="1",
        compute="_compute_subtotal")
    amount_total = fields.Float(
        string="Valor Total",
        readonly="1",
        compute="_compute_total")

    @api.multi
    @api.depends("product_line_ids")
    def _compute_subtotal(self):
        for s in self:
            subtotal = sum(s.product_line_ids.mapped('price_subtotal'))
            s.amount_subtotal = subtotal

    @api.multi
    @api.depends("amount_subtotal", "insurance_total", "freight_total")
    def _compute_total(self):
        for s in self:
            i = s.currency_fee
            if i == 0:
                continue
            freight = s.freight_total * (s.freight_currency_fee / i)
            insurance = s.insurance_total * (s.insurance_currency_fee / i)
            s.amount_total = s.amount_subtotal + freight + insurance

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
    name = fields.Char(string="Descrição")
    quantity = fields.Float(string="Quantidade")
    price_unit = fields.Float(string="Preço Unit.")
    price_subtotal = fields.Float(
        string="Subtotal",
        compute="_compute_subtotal")
    currency_id = fields.Many2one(
        string="Moeda",
        comodel_name="res.currency",
        domain="[('active', '!=', False)]")
    cost = fields.Float(
        string="Custo",
        compute="_compute_custo")

    @api.onchange("product_id")
    def _onchange_product_id(self):
        self.name = self.product_id.name

    @api.multi
    @api.depends("declaracao_id.freight_total", "declaracao_id.insurance_total", "price_subtotal")
    def _compute_custo(self):
        for s in self:
            i = s.price_subtotal / s.declaracao_id.amount_subtotal
            if i == 0:
                continue
            pt = (s.declaracao_id.freight_total * i)
            it = (s.declaracao_id.insurance_total * i)
            s.cost = pt + it

    @api.multi
    @api.depends("quantity", "price_unit")
    def _compute_subtotal(self):
        for s in self:
            s.price_subtotal = s.quantity * s.price_unit
