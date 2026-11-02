from equipments import get_equipment

def test_get_equipment():
    result = get_equipment()

    assert result == "Equipment"