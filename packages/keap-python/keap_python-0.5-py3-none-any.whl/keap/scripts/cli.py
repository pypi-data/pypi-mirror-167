import json
from urllib import parse

import click as click
from click import prompt

from keap import Keap, KeapTokenStorage


@click.group()
def cli():
    """
    Simple CLI for managing Keap API Access
    """
    pass


@cli.command()
@click.option('--client-id', '--id', required=True, hide_input=True, prompt="What is your client id?")
@click.option('--client-secret', '--s', required=True, hide_input=True, prompt="What is your client secret?")
@click.option('--redirect-url', '--s', default='https://theapiguys.com', prompt="What is your redirect?")
@click.option('--client-name', '--n', default='default', prompt="What is your client name?")
@click.option('--use-datetime', '--dt', default=True, prompt="Use Datetime?")
@click.option('--token-file', type=click.Path(), default="./cache/keap_tokens.json",
              prompt="File path to token storage")
@click.option('--output', type=click.File('w'), default="./cache/keap_credentials.json",
              prompt="File path to Keap Credentials")
def generate_client_config(client_id, client_secret, redirect_url, client_name, use_datetime, token_file, output):
    """Generate a valid Keap Configuration file"""
    url_format = 'https://www.googleapis.com/books/v1/volumes/{}'
    creds = {
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_url': redirect_url,
        'client_name': client_name,
        'use_datetime': use_datetime,
        'token_file': token_file,
    }
    if output:
        json.dump(creds, output, indent=4)
    click.echo(f"Secret file generated at {output}")


@cli.command()
@click.option('--credentials-file', '--f', type=click.Path(), default='./cache/keap_credentials.json')
@click.option('--client-name', '--f', default='default')
def get_access_token(credentials_file, client_name):
    """OAuth flow for Keap to obtain an access and refresh token"""
    try:
        with open(credentials_file, "r") as f:
            creds = json.load(f)
    except FileNotFoundError as e:
        click.echo("Please run `keap generate-client-config` then running this command")
        return

    keap = Keap(
        **creds
    )
    if not client_name and creds.get('client_name'):
        client_name = creds.get('client_name')
    if not client_name and creds.get('token_file'):
        storage = KeapTokenStorage(creds.get('token_file'))
        token_names = storage.list_tokens_by_name()
        client_name = prompt("Client Name", default=keap.client_name,
                             type=click.Choice(token_names, case_sensitive=False))
    auth_url = keap.get_authorization_url(client_name)
    click.echo(f"Visit {auth_url}")
    response_url = prompt("Paste the return url here")
    query_string = dict(parse.parse_qsl(parse.urlsplit(response_url).query))
    code = query_string.get('code')
    if code:
        new_token = keap.request_access_token(code)
        if new_token.access_token and new_token.refresh_token:
            token_path = prompt("Path to save token", type=click.Path(), default=f"./cache/keap_tokens.json")
            storage = KeapTokenStorage(token_path)
            storage.save_token(client_name, new_token)


@cli.command()
@click.option('--credentials-file', '--c', type=click.Path(), default='./cache/keap_credentials.json')
@click.option('--token-file', '--t', type=click.Path(), default="./cache/keap_tokens.json")
@click.option('--client-name', '--n')
def refresh_access_token(credentials_file, token_file, client_name):
    """Refresh Keap access token"""
    try:
        with open(credentials_file, "r") as f:
            creds = json.load(f)
    except FileNotFoundError as e:
        click.echo("Please run `keap generate-client-config` then running this command")
        return

    keap = Keap(
        **creds
    )
    storage = KeapTokenStorage(token_file)
    token_names = storage.list_tokens_by_name()
    if not client_name and creds.get('client_name'):
        client_name = creds.get('client_name')
    if not client_name:
        client_name = prompt("Client Name", default=keap.client_name,
                             type=click.Choice(token_names, case_sensitive=False))
    new_token = keap.refresh_access_token(client_name)
    storage.save_token(client_name, new_token)


if __name__ == "__main__":
    cli()
