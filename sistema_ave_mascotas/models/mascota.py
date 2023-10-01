# Copyright (C) 2020 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class mascota(models.Model):
    _name = "mascota"
    _description = "Mascota"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "name"

    especie = fields.Char()
    raza = fields.Char()
    nombre = fields.Char()
    sexo = fields.Char()
    edad = fields.Char()
    pelaje = fields.Char()
    imagen = fields.Binary(
        attachment=True, help="Imagen de mascota"
    )
    active = fields.Boolean(default=True)