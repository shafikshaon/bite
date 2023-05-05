import logging

from notifications.channels.email import EmailChannel

logger = logging.getLogger(__name__)


def _send_email(email_notification_config, context, to):
    email_html_template = email_notification_config.get("email_html_template")
    email_subject = email_notification_config.get("email_subject")

    EmailChannel.send(
        context=context, html_template=email_html_template, subject=email_subject, to=to
    )
