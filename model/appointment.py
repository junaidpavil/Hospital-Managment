from odoo import  api, fields, models



class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name = 'ref'


    patient_id=fields.Many2one('hospital.patient',string="Patient")
    ref=fields.Char(string='reference')
    gender=fields.Selection( related='patient_id.gender')
    appointment_time=fields.Datetime(string='Appointment Time',default=fields.Datetime.now)
    booking_date=fields.Date(string='Booking Date',default=fields.Date.context_today)
    prescription=fields.Html(string='prescription')
    priority=fields.Selection([('0','Normal'),('1','Low'),('2','High'),('3','Very High')],string='Priority')
    state=fields.Selection([('draft','Draft'),('in_consultation','In Consultation'),('done','Done'),('cancel','Cancelled')],default='draft',string='Status',required=True)
    doctor_id=fields.Many2one('res.users',string='Doctor',tracking=True)
    pharmacy_line_ids=fields.One2many('appointment.pharmacy.lines','appointment_id',string='Pharmacy Lines')
    hide_sales_price=fields.Boolean(string='Hide Sale Price')


    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref=self.patient_id.ref

    def action_test(self):
        print('Button Clicked !!!!')
        return {
            'effect':{
                'fadeout':'slow',
                'message':'Click Successfully',
                'type':'rainbow_man'
            }
        }

    def action_in_consultation(self):
        for rec in self:
            rec.state='in_consultation'

    def action_done(self):
        for rec in self:
            rec.state="done"

    def action_cancel(self):
        for rec in self:
            rec.state='cancel'

    def action_draft(self):
        for rec in self:
            rec.state='draft'


class AppointmentPharmacyLines(models.Model):
    _name = 'appointment.pharmacy.lines'
    _description = 'Appointment Pharmacy Lines'

    product_id=fields.Many2one('product.product',required=True)
    price_unit=fields.Float(String='Price')
    qty=fields.Integer(string="Quantity",default=1)
    appointment_id=fields.Many2one('hospital.appointment',string='Appointment')