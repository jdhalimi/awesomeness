from awesomeness.http import get_http


def test_get_http():
    response_text = get_http("https://www.google.com")
    assert '<html' in response_text
