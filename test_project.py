import project

from project import (
    Capsule,
    generate_id,
    save_capsules,
    load_capsules
)


def test_capsule_creation():

    capsule = Capsule(
        "Future Me",
        "Learn Python!",
        "2030-01-01",
        "Excited",
        1234
    )

    assert capsule.id == 1234
    assert capsule.title == "Future Me"
    assert capsule.message == "Learn Python!"


def test_generate_id():

    capsules = [
        Capsule(
            "Test",
            "Message",
            "2030-01-01",
            "Happy",
            1234
        )
    ]

    new_id = generate_id(capsules)

    assert new_id != 1234
    assert 1000 <= new_id <= 9999


def test_save_capsules(tmp_path):

    test_file = tmp_path / "test_capsules.json"

    project.FILE_NAME = test_file

    capsule = Capsule(
        "Test Capsule",
        "Hello World",
        "2030-01-01",
        "Happy",
        5555
    )

    save_capsules([capsule])

    assert test_file.exists()


def test_load_capsules(tmp_path):

    test_file = tmp_path / "test_capsules.json"

    project.FILE_NAME = test_file

    capsule = Capsule(
        "Memory",
        "Testing Load",
        "2030-01-01",
        "Calm",
        7777
    )

    save_capsules([capsule])

    capsules = load_capsules()

    assert len(capsules) == 1
    assert capsules[0].id == 7777
    assert capsules[0].title == "Memory"


def test_capsule_features():

    capsule = Capsule(
        "Goals",
        "Become a developer",
        "2030-01-01",
        "Motivated",
        8888
    )

    data = capsule.features()

    assert data["id"] == 8888
    assert data["title"] == "Goals"
    assert data["message"] == "Become a developer"
