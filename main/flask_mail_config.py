import flask_mail
from .settings import project



project.config["MAIL_SERVER"] = "smtp.gmail.com"
project.config["MAIL_PORT"] = 587
project.config["MAIL_USE_TLS"] = True
project.config["MAIL_USERNAME"] = "touragent.practice@gmail.com"
project.config["MAIL_PASSWORD"] = "ijam ahhn swhb qnzs"

mail = flask_mail.Mail(project)
