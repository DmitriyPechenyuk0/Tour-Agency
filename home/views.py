import flask, flask_mail
from flask_login import current_user
from  main.flask_mail_config import mail
from jinja2 import exceptions


def render_home():
    try:
        user = current_user

        if flask.request.method == 'POST':
            try:
                body_message = f'Клієнт {flask.request.form["name"]} залишив/ла відгук:\n{flask.request.form["description"]}:\n\n Email клієнта: {flask.request.form["email"]}'
                message = flask_mail.Message(
                    subject=f'Клієнт залишив/ла відгук',
                    body=body_message,
                    recipients=['dmitriypechenyuk0@gmail.com'],
                    sender='touragent.practice@gmail.com'
                )
                mail.send(message=message)
            except Exception as exeption:
                print(exeption)
    except exceptions.UndefinedError:
        flask.redirect('/registration')

    # if current_user != None or current_user != '' or current_user != 
    return flask.render_template(template_name_or_list='home.html', user = user)
    


