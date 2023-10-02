# Copyright (C) 2020 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Sistema AVE - Mascotas",
    "version": "15.0.0.0.0",
    "license": "AGPL-3",
    "summary": "Adminsitración de mascotas",
    "author": "Ghiglione Pedro Matias",
    "maintainer": "Ghiglione Pedro Matias",
    'category': 'Sales',
    "website": "https://quimerasoftware.ar",
    "depends": ["base","contacts"],
    "data": [
        "views/menu.xml",
        "views/mascota.xml",
        "security/res_groups.xml",
        "security/ir.model.access.csv",
    ],
    "application": True,
    "development_status": "Beta",
    "maintainers": ["pghiglione"],
}
