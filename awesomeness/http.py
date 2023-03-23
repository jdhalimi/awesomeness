import requests

requests.packages.urllib3.disable_warnings()

IP = '192.168.1.243'


def get_http(url, session=None):
    """
    gets an HTTP requests

    :param url: url to get
    :type url: str

    :param session:
    :type session: requests.Session

    :return: response text
    """

    assert IP
    session = session or requests.Session()
    response = session.get(url)
    return response.text
