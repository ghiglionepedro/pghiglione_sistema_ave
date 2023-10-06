# Copyright (C) 2020 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class mascota(models.Model):
    _name = "mascota"
    _description = "Mascota"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "nombre"

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

    partner_id = fields.Many2one(
        "res.partner", string="Dueño", index=True, tracking=True
    )

    consulta_ids = fields.Many2many(
        comodel_name='consulta.medica',
        string='Consultas Médicas',
        compute='_compute_consulta_ids',
        inverse='_inverse_consulta_ids',
        store=True,
    )

    @api.depends('consulta_ids')
    def _compute_consulta_ids(self):
        for mascota in self:
            mascota.consulta_ids = self.env['consulta.medica'].search([
                ('entity_type', '=', 'mascota'),
                ('entity_id', '=', mascota.id),
            ])

    def _inverse_consulta_ids(self):
        for mascota in self:
            for consulta in mascota.consulta_ids:
                consulta.entity_type = 'mascota'
                consulta.entity_id = mascota.id