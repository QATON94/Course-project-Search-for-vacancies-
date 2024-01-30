from api.connector import HeadHunterAPI


def test_get_response():
    api_hh = HeadHunterAPI('python')
    data = api_hh.get_response()
    assert len(data) == 10
