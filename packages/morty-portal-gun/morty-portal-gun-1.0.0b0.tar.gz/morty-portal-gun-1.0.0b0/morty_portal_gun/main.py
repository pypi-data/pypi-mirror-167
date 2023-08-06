import typer
import os

app = typer.Typer()
file_path = os.path.dirname(os.path.abspath(__file__))

@app.callback()
def callback():
    """
    Awesome Portal Gun
    """


@app.command()
def shoot():
    """
    Shoot the portal gun
    """
    typer.echo("Shooting portal gun")


@app.command()
def load():
    """
    Load the portal gun
    """
    typer.echo("Loading portal gun")

@app.command()
def add(name:str):
    """
    Add File Name
    """
    write(name)

@app.command()
def list():
    a = read()
    typer.echo(a)
    
def write(file:str):    
    f = open(os.path.join(file_path,"db.txt"), "w")
    f.write(file)
    f.close()

def read():
    f = open(os.path.join(file_path,"db.txt"), "r")
    return f.read()