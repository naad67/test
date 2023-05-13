from odoo import models, fields


class SurveyQuestion(models.Model):
    _inherit = 'survey.question'

    question_type = fields.Selection([
        ('text_box', 'Multiple Lines Text Box'),
        ('char_box', 'Single Line Text Box'),
        ('numerical_box', 'Numerical Value'),
        ('date', 'Date'),
        ('datetime', 'Datetime'),
        ('simple_choice', 'Multiple choice: only one answer'),
        ('multiple_choice', 'Multiple choice: multiple answers allowed'),
        ('matrix', 'Matrix'),
        ('scale', 'Scale')], string='Question Type',
        compute='_compute_question_type', readonly=False, store=True)