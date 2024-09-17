import frappe
from frappe import _

def validate_cmplete_method(doc):
    if doc.percent_complete_method != "Manual":
        frappe.throw(_("Project Complete Method Must be Manual"))