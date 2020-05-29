from main import get_temperature
from unittest import mock, TestCase
import requests

# valores padrão fornecidos pelo readme da atividade

lat = -14.235004
lng = -51.92528
key = "e1ee55658d4a2b28c4841e373c3b3d87"
url = "https://api.darksky.net/forecast/{}/{},{}".format(key, lat, lng)


# uso de patch para localizar a função que será mocada


@mock.patch("main.get_temperature")
class DarkSKyMock(TestCase):

    """ Classe mocada que testa se a função recebeu
        a temperatura em Fahrenheit certa e se transformou
        em Celsius
    """

    def test_get_temperature_by_lat_lng(self, mock_dark_sky):
        result = get_temperature(lat, lng)
        assert result == 16

    def test_verify_temperature_value(self, mock_dark_sky):
        reponse = requests.get(url)
        data = reponse.json()
        temperature = data.get("currently").get("temperature")
        round_temperature = round(temperature)
        assert round_temperature == 62
