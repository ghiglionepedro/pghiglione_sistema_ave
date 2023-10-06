# Copyright (C) 2020 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class consultas(models.Model):
    _name = "consultas"
    _description = "Consultas clínicas"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "nombre"

    fecha_consulta = fields.Date(string='Fecha de Consulta', required=True)
    tipo_consulta = fields.Char()
    descripcion = fields.Text(string='Descripción')
    imagenes = fields.Many2many('ir.attachment', 'consulta_medica_attachment_rel', 'consulta_medica_id', 'attachment_id', string='Imágenes', widget="many2many_binary")

    entity_type = fields.Selection(
        [('mascota', 'Mascota'), ('res.partner', 'Dueño')],
        string='Entidad Relacionada',
        required=True,
        default='mascota',
    )
    entity_id = fields.Many2one(
        comodel_name='mascota_o_dueño',
        string='Entidad',
    )

    tipo_consulta = fields.Selection([('vacunacion', 'Vacunación'), ('analisis', 'Análisis clinicos'), ('desparacitacion', 'Desparacitación'), ('cirugia', 'Cirugia'), ('visita', 'Visita')], string='Tipo de Consulta', required=True)
    
    mascota_id = fields.Many2one('mascota', string='Mascota')