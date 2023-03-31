def format_ip(ip: int) -> str:
    str_ip = str(ip)
    if len(str_ip) == 12:
        return f'{str_ip[:3]}.{str_ip[3:6]}.{str_ip[6:9]}.{str_ip[9:12]}'
    else:
        raise Exception