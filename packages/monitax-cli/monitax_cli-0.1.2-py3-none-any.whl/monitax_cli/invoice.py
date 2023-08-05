import typer
import random
import requests
import string
import pendulum
import json
from . import config
from rich.console import Console

app = typer.Typer(help="Invoice command interface")
setting=config.Setting()
console=Console()
characters = list(string.ascii_letters + string.digits)

def generate_invoice_num(length: int):
    random.shuffle(characters)
    invoice_num = []
    for i in range(length):
        invoice_num.append(random.choice(characters))
    random.shuffle(invoice_num)
    return "".join(invoice_num)

@app.command(help="Send random invoice to backend server. For testing purpose only")
def send(
    username:str=typer.Option(...,"--username","-u",help="A registered username"),
    devicename:str=typer.Option(...,"--devicename","-d",help="A device which has been assigned to registered user"),
    api_key:str=typer.Option(...,"--api-key","-k",help="A key to authorize API calling")
    ):
    
    total_value = random.randint(100, 999) * 100.0
    invdate = pendulum.now().to_iso8601_string()  # .replace('+07:00','Z')    
    invoice = {
        "invoice_num": "INV-" + generate_invoice_num(8),
        "invoice_date": invdate,
        "device_name": devicename,
        "username": username,
        "tax_value": round(total_value * 11.0 / 111.0, 2),
        "total_value": total_value,
    }
    try:        
        with console.status("Wait...",spinner="arrow3") as status:                
            headers={"Access-Control-Allow-Origin":"*","x-api-key": api_key}
            session = requests.Session()
            url=f"{setting.baseurl}/invoices"
            response = session.post(
                url= url, json=invoice, headers=headers
            )
            if(response.status_code==200):
                console.print_json(json.dumps(response.json()))
            else:
                console.print(response.content)                
    except Exception as ex:
        console.print_exception()


if __name__ == "__main__":
    app()