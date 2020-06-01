import main


class DarkSkyApi:

    """
    Classe que irá simular a API com o retorno no formato json
    """

    @staticmethod
    def json():
        lat = -14.235004
        lng = -51.92528
        if lat and lng:
            return {"currently": {"temperature": 62}}


def test_get_temperature_by_lat_lng(monkeypatch):
    lat = -14.235004
    lng = -51.92528
    expected = 16

    # função que faz a chamada para a api

    def mock_request(*args):
        return DarkSkyApi()

    # Gera um request GET para a função mock_quest

    monkeypatch.setattr("requests.get", mock_request)
    assert main.get_temperature(lat, lng) == expected
