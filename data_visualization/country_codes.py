from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Returns Pygal code for country consisting from 2 letters"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return name

    return None
