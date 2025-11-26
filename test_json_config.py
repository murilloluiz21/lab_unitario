import json

def test_config_json_valido():
    with open("config.json", "r") as f:
        data = json.load(f)

    # Verifica chaves
    assert "version" in data
    assert "enabled" in data
    assert "name" in data

    # Verifica tipos
    assert isinstance(data["version"], int)
    assert isinstance(data["enabled"], bool)
    assert isinstance(data["name"], str)
