__author__ = "Shafikur Rahman"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
MAILER_EMAIL_BACKEND = EMAIL_BACKEND
EMAIL_HOST = "your_mail_server"
EMAIL_HOST_PASSWORD = "your_password"
EMAIL_HOST_USER = "your_email"
EMAIL_PORT = 465
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
