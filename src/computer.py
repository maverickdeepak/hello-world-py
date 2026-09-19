from pydantic import BaseModel, Field, ValidationError

class Computer(BaseModel):
    brand: str = Field(..., min_length=1, max_length=100)
    ram_gb: int = Field(..., ge=1, le=128)
    hard_drive_gb: int = Field(..., ge=1, le=2048)

if __name__ == "__main__":
    laptop = Computer(brand="Dell", ram_gb=16, hard_drive_gb=512)
    print(laptop.brand)  # Dell
    try:
        bad_laptop = Computer(brand="HP", ram_gb=0, hard_drive_gb=512)
    except ValidationError as e:
        print("Validation error:", e)