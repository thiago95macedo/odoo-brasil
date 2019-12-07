# © 2020 Mackilem Van der Laan, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class DeclaracaoImportacao_wizard(models.TransientModel):
    _name = "declaracao.importacao.wizard"
    _description = "Importação do XML da DI"


    xml = fields.Binary(string="Arquivo XML")


    def action_save_close(self):
        pass
