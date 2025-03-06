import os

if os.getenv('ENVIRONMENT') == 'local':
    from dotenv import load_dotenv

    load_dotenv()


def get_env(key: str, default=None, required_type: type = str):
    val = os.getenv(key, default)

    if val is None:
        return default
    elif type(val) == required_type:
        return val

    if required_type == bool:
        return val.lower() in ('true', '1', 'yes', 'on')
    elif required_type == list:
        return val.split(',')

    try:
        return required_type(val)
    except ValueError:
        return default
