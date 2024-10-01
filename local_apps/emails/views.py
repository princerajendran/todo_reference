from .tasks import single_send_mail, multiple_send_mail
from django.template.loader import render_to_string


def mail_handler(mail_type=None, to=None, subject=None, data=None, template=None, cc=None, bcc=None, reply_to=None):
    print('email view')
    try:
        if to and subject and data and template:
            message = render_to_string(template, context={'data': data, })
            if mail_type == 'single':
                send = single_send_mail.delay(subject=subject, message=message, to_list=to, cc_list=cc, bcc_list=bcc,
                                              reply_to=reply_to)
                return send
            elif mail_type == 'multiple':
                send = multiple_send_mail.delay(subject=subject, message=message, to_list=to, cc_list=cc, bcc_list=bcc,
                                                reply_to=reply_to)
                return send
            else:
                return False
    except Exception as e:
        print(e)
        return False