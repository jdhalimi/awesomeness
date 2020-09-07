import requests

requests.packages.urllib3.disable_warnings()


def get_http(url, session=None):
    """
    gets an HTTP requests

    :param url: url to get
    :type url: str

    :param session:
    :type session: requests.Session

    :return: response text
    """

    session = session or requests.Session()
    response = session.get(url)
    return response.text
