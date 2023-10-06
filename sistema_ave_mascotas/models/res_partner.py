# Copyright (C) 2020 Open Source Integrators
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    mascota_ids = fields.One2many("mascota", "partner_id", string="Mascotas")
    mascotas_count = fields.Integer(
        compute=_compute_animal_count(), string="Número de mascotas", store=True
    )

    @api.depends("mascota_ids")
    def _compute_animal_count(self):
        for rec in self:
            rec.animal_count = len(rec.mascota_ids)

    def action_view_mascotas(self):
        xmlid = "sistema_ave_mascotas.action_mascota"
        action = self.env["ir.actions.act_window"]._for_xml_id(xmlid)
        if self.animal_count > 1:
            action["domain"] = [("id", "in", self.mascota_ids.ids)]
        else:
            action["views"] = [(self.env.ref("sistema_ave_mascotas.view_mascota_form").id, "form")]
            action["res_id"] = self.mascota_ids and self.mascota_ids.ids[0] or False
        return action
