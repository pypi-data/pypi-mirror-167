import requests
from . import fileio


def create_authorized_dg_session():
    session = requests.Session()
    url_for_authentication = "http://www.dailygammon.com/bg/login"
    lines = fileio.read_from_text_file("dg_cred.cfg")
    data = {"login": lines[0], "password": lines[1]}

    _ = http_post_request(session, url=url_for_authentication, data=data)
    return session


def http_post_request(session, url, data=None):
    http_response = session.post(url, data=data)
    http_response.raise_for_status()
    return http_response
