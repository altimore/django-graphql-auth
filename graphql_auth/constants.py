from django.utils.translation import ugettext as _


class Messages:
    INVALID_PASSWORD = [
        {"message": _("Invalid password."), "code": "invalid_password",}
    ]
    UNAUTHENTICATED = [
        {"message": _("Unauthenticated."), "code": "unauthenticated",}
    ]
    INVALID_TOKEN = [{"message": _("Invalid token."), "code": "invalid_token",}]
    EXPIRATED_TOKEN = [
        {"message": _("Expirated token."), "code": "expirated_token",}
    ]
    ALREADY_VERIFIED = [
        {"message": _("Account already verified."), "code": "already_verified",}
    ]
    EMAIL_FAIL = [{"message": _("Failed to send email."), "code": "email_fail"}]
    INVALID_CREDENTIALS = [
        {
            "message": _("Please, enter valid credentials."),
            "code": "invalid_credentials",
        }
    ]
    NOT_VERIFIED = [
        {"message": _("Please verify your account."), "code": "not_verified",}
    ]
    NOT_VERIFIED_PASSWORD_RESET = [
        {
            "message": _(
                "Please verify your account before requesting the password reset."
            ),
            "code": "not_verified",
        }
    ]
