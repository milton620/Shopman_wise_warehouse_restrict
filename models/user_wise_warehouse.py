from odoo import  fields, models, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    allowed_warehouse = fields.Many2many('stock.warehouse', string='Allowed warehouse', help='Allowed Warehouse for this user')

    @api.model
    def create(self, vals):
        self.clear_caches()
        return super(ResUsers, self).create(vals)

    def write(self, vals):
        # for clearing out existing values and update with new values
        self.clear_caches()
        return super(ResUsers, self).write(vals)
