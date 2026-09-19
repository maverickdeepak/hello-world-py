from computer import Computer
from pydantic import ValidationError

def test_valid_computer():
    laptop = Computer(brand="Apple", ram_gb=16, hard_drive_gb=512)
    assert laptop.brand == "Apple"
    assert laptop.ram_gb == 16
    assert laptop.hard_drive_gb == 512

def test_invalid_computer():
    try:
        bad_laptop = Computer(brand="HP", ram_gb=0, hard_drive_gb=512)
    except ValidationError as e:
        assert "ram_gb" in str(e)