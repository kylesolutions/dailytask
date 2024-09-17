import frappe
from frappe.utils import flt

def custom_update_project_percentage(doc):
    project=doc.project
    total_budgeted_qty=0
    toatl_progress_qty=0
    task_list=frappe.db.get_all("Task",{"project":project,"custom_budgeted_qty":[">",0],"custom_progress_qty":[">",0],"status":["not in",["Cancelled"]]},["custom_budgeted_qty","custom_progress_qty"])
    for i in task_list:
        total_budgeted_qty += i["custom_budgeted_qty"]
        toatl_progress_qty += i["custom_progress_qty"]
    percent_complete = flt(flt(toatl_progress_qty) / total_budgeted_qty * 100, 2)
    frappe.db.set_value("Project",project,"percent_complete",percent_complete)
