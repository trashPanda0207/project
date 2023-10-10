from project import City, area_validator, city_validator
import pytest

@pytest.mark.parametrize("area_names", ["North", "East", "West", "Offshore islands"])
def test_area_validation(area_names):
    assert area_validator(area_names)

@pytest.mark.parametrize("area_names", ["north", "east", "west", "offshore islands"])
def test_area_lower_case(area_names):
    assert area_validator(area_names)

@pytest.mark.parametrize("area_names", ["n", "see", "western", "offshore"])
def test_area_lower_case(area_names):
    with pytest.raises(ValueError):
        assert area_validator(area_names)

@pytest.mark.parametrize("city_names", ["Miaoli County", "Taichung City", "Changhua County", "Nantou County"])
def test_city_validation(city_names):   
    assert city_validator('West', city_names)
    assert city_validator('West', city_names)

@pytest.mark.parametrize("city_names", ["iaoli County", "aichung City", "hanghua County", "antou County"])
def test_city_validation_failed(city_names): 
    with pytest.raises(ValueError):
        city_validator('West', city_names)

