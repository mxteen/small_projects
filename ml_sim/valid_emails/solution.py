import re
from typing import List

valid_email_regex = re.compile(
    r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")


def valid_emails(strings: List[str]) -> List[str]:
    """Take list of potential emails and returns only valid ones"""

    def is_valid_email(email: str) -> bool:
        return bool(valid_email_regex.fullmatch(email))

    emails = list(filter(is_valid_email, strings))

    return emails
