import random
import string


def generate_reservation_code(prefix: str = "UDIG") -> str:
    suffix = "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"{prefix}-{suffix}"
