import typer
from . import config
from rich.console import Console

app = typer.Typer(help="Configuration command interface")

setting=config.Setting()
console=Console()

@app.command(help="Initialize configuration")
def init(host:str=typer.Option(...,prompt=True),ssl:bool=typer.Option(...,confirmation_prompt=True,prompt=True)):    
    setting.setup(host=host,ssl=ssl)                
    console.print("Initializing done :thumbs_up::thumbs_up:")

@app.command(help="Show current configuration")
def show():    
    with open(setting.__filename__,"r") as f:
        console.print(f.read())

if __name__ == "__main__":
    app()