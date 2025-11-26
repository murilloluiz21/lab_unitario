import yaml

def test_yaml_workflow_valido():
    with open(".github/workflows/python-tests.yml", "r") as file:
        data = yaml.safe_load(file)

    # Verifica chaves básicas
    assert "name" in data
    assert "jobs" in data

    # Garante que tem um job chamado "test"
    assert "test" in data["jobs"]

    job = data["jobs"]["test"]

    assert job["runs-on"] == "ubuntu-latest"
    assert "steps" in job
    assert isinstance(job["steps"], list)
