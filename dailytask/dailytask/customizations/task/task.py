from dailytask.dailytask.customizations.task.doc_events.utility_functions import custom_update_project_percentage
import frappe

def on_update(doc,events):
    custom_update_project_percentage(doc)