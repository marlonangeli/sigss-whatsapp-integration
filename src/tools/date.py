from datetime import datetime

def get_date():
    date = f'{str(datetime.now().replace())[:10]}'
    date = datetime.strptime(date, "%Y-%m-%d")
    return str(date.strftime("%d/%m/%Y"))
    