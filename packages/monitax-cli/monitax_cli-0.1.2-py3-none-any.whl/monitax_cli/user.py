from cgi import print_exception
from ctypes import alignment
import typer
import requests
import json
from . import config
from typing import Optional
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel

app = typer.Typer(help="User command interface")
setting=config.Setting()
console=Console()

def getContent(user):
    username=user["username"]    
    phone=user["phone_no"]
    return f"[b]{username}[/b]\n[yellow]{phone}"

@app.command(help="Login into system")
def login(username:str=typer.Option(...,prompt=True),
    password:str=typer.Option(...,prompt=True,hide_input=True)
    ):    
    session=requests.Session()
    headers={'Content-Type': 'application/x-www-form-urlencoded',"Access-Control-Allow-Origin":"*"}
    data={
        "username":username,
        "password":password
    }        
    try:     
        url=f"{setting.baseurl}/auth/access-token"
        with console.status("Wait...",spinner="arrow3") as status:            
            response=session.post(url=url,data=data,headers=headers)
            if response.status_code==200:   
                console.print_json(json.dumps(response.json()))     
                token=response.json()["access_token"]
                setting.setup(token=token,ssl=setting.ssl)        
            else:
                console.print(response.content)                            
    except Exception as ex:
        console.print_exception()
            

@app.command(help="show current user profile ")
def profile():        
    try:
        with console.status("Wait...",spinner="arrow3") as status:
            url=f"{setting.baseurl}/users/me"        
            headers={"Authorization":f"Bearer {setting.token}","Access-Control-Allow-Origin":"*"}
            session=requests.Session()
            response=session.get(url=url,headers=headers)        
            if response.status_code==200:
                console.print_json(json.dumps(response.json()))
            else:
                console.print(response.content)
                               
    except Exception as ex:
        console.print_exception()

@app.command(help="Create new user")
def create(
    username:str=typer.Option(...,"--username","-u",help="A valid email"),
    password:str=typer.Option(...,"--password","-p",prompt=True,hide_input=True,help="Password"),
    nik:str=typer.Option(...,"--nik","-n",help="Nomor Induk Kependudukan"),
    phone:str=typer.Option(...,"--phone","-p",help="Telephone number")
):
    try:
        with console.status("Wait...",spinner="arrow3") as status:
            session=requests.Session()
            url=f"{setting.baseurl}/users/register"
            headers={"Access-Control-Allow-Origin":"*"}
            data={"username":username,"password":password,"nik":nik,"phone_no":phone}
            response=session.post(url=url,json=data,headers=headers)
            if response.status_code==200:
                console.print_json(json.dumps(response.json()))
            else:
                console.print(response.content)                        
    except Exception as ex:
        console.print_exception(str(ex))        

@app.command(help="List user")
def list(card:bool=typer.Option(False,"--card","-c",help="Show user list in card mode alongside json mode")):    
    try:        
        with console.status("Wait...",spinner="arrow3") as status:
            url=f"{setting.baseurl}/users/"        
            headers={"Authorization":f"Bearer {setting.token}",
            "Access-Control-Allow-Origin":"*",
            }
            session=requests.Session()
            response=session.get(url=url,headers=headers)                                
            if response.status_code==200:
                console.print_json(json.dumps(response.json()))
                if card:
                    user_renderables = [Panel(getContent(user), expand=True) for user in response.json()]
                    console.print(Columns(user_renderables,align="center"))                
            else:
                console.print(response.content)       
    except Exception as ex:
        console.print_exception()

if __name__ == "__main__":
    app()