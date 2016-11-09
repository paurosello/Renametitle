# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "renametitle"
app_title = "Renametitle"
app_publisher = "Pau Rosello"
app_description = "Rename modifies title attribute"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "paurosello@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/renametitle/css/renametitle.css"
# app_include_js = "/assets/renametitle/js/renametitle.js"

# include js, css files in header of web template
# web_include_css = "/assets/renametitle/css/renametitle.css"
# web_include_js = "/assets/renametitle/js/renametitle.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "renametitle.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "renametitle.install.before_install"
# after_install = "renametitle.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "renametitle.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
  	"*": {
  		"after_rename": "renametitle.utils.after_rename",
 	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"renametitle.tasks.all"
# 	],
# 	"daily": [
# 		"renametitle.tasks.daily"
# 	],
# 	"hourly": [
# 		"renametitle.tasks.hourly"
# 	],
# 	"weekly": [
# 		"renametitle.tasks.weekly"
# 	]
# 	"monthly": [
# 		"renametitle.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "renametitle.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "renametitle.event.get_events"
# }

