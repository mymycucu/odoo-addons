from odoo import api, fields, models
 
class TrainingCourse(models.Model):
    _name = 'training.course'
    _description = 'Jadwal Kerja'
     
    name = fields.Char(string='Jadwal', required=True)
    description = fields.Text(string='Keterangan')
    user_id = fields.Many2one('res.users', string="PIC")
    company_id = fields.Many2one('res.company', string='Customer', required=True)

    session_line = fields.One2many('training.session', 'course_id', string='Sesi')
    product_ids = fields.Many2many('product.product', 'course_product_rel', 'course_id', 'product_id', 'Layanan')
    gaji = fields.Float(string='Gaji per jam', help='Jumlah Jam')
    priority = fields.Selection([('0', 'Normal'), ('1', 'High')], 'Priority', select=True, default='0')
    active = fields.Boolean(string='Sedang Aktif', default=True)
    state = fields.Selection([
            ('waiting', 'Ready'),
            ('workshop_create_invoices', 'Invoiced'),
            ('cancel', 'Invoice Canceled'),
        ], string='Status', default='waiting', track_visibility='onchange', select=True)
    #aktif?
    #priroritas
    #status

class TrainingSession(models.Model):
    _name = 'training.session'
    _description = 'Sesi Kerja'
      
    course_id = fields.Many2one('training.course', string='Judul Kursus', required=True, ondelete='cascade')
    partner_id = fields.Many2one('res.users', string='Nama Petugas')
    start_date = fields.Date(string='Tanggal')
    duration = fields.Float(string='Durasi (Dalam Jam)', help='Jumlah Jam')
    

# class SaleOrder(models.Model):
  
#     _name = "sale.order"
      
#     order_line = fields.One2many('sale.order.line', 'order_id', string='Order Lines')
 
 
# class SaleOrderLine(models.Model):
  
#     _name = 'sale.order.line'
      
#     order_id = fields.Many2one('sale.order', string='Order Reference', required=True, ondelete='cascade')