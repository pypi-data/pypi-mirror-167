import typer
import os
import subprocess
import json

cli = typer.Typer()

@cli.command()
def pull():
    typer.echo("Pulling from github")
    path = f"/home/{os.getlogin()}"
    repo = "https://github.com/AbdelrhmanNile/skynix.git"
    os.system(f"cd {path} && git clone {repo}")
    typer.echo("Done pulling")
    typer.echo("Installing requirements")
    os.system(f"cd {path}/skynix && pip3 install pipenv && pipenv install")
    os.system(f"cd {path}/skynix && pipenv --venv > {path}/skynix/venv.txt")
    with open(f"{path}/skynix/venv.txt", "r") as f:
        venv = f.read()
    params = {"python": f"{venv.strip()}/bin/python",
                  "nlpcloud_tokens": ["","","",""],
                  "forefront_token": "",
                  "forefront_gptj_url": "",
                  "forefront_codegen_url": ""}
    with open(f"{path}/skynix/config.json", "w", encoding="utf-8") as f:
        json.dump(params, f, indent=4)
    typer.echo("Done installing requirements")
    

@cli.command()
def run():
    config = json.load(open(f"/home/{os.getlogin()}/skynix/config.json"))
    python = config["python"]
    os.system(f'cd /home/{os.getlogin()}/skynix && pipenv shell | python -u "/home/{os.getlogin()}/skynix/main.py"')

@cli.command()
def config():
    os.system(f"nano /home/{os.getlogin()}/skynix/config.json")

if __name__ == "__main__":
    cli()