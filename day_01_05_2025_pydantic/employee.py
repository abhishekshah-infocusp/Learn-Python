from typing import Annotated, Self
from pydantic import BaseModel, Field, field_validator, model_validator, validate_call, EmailStr, PositiveFloat # type: ignore
from datetime import date
import time
# from .Department import Department
from day_01_05_2025_pydantic.department import Department

class Employee(BaseModel):
    employee_id : int = Field(default_factory=int, frozen = True) # Frozen makes the field immutable
    name: str = Field(min_length=1, max_length=100, description="Name of the employee", frozen = True)
    email: str = Field(pattern= r".+@infocusp\.com$", frozen = True)
    date_of_birth : date = Field(alias = "dob", repr = False, frozen = True)
    salary: float = Field(gt=0, lt=10000000, repr= False)
    department: Department = Field(frozen = False) # Department can be changable
    other_benifits: bool

    # Custom Validator
    @field_validator("date_of_birth")
    @classmethod
    def check_valid_dob(cls, dob: date) -> date:
        date_difference_years = (date.today() - dob).days / 365.25
        # print(date_difference_years)
        if date_difference_years < 18:
            raise ValueError("Employee must be at least 18 years old.")
        return dob

    @model_validator(mode = "after")
    def check_it_benifits(self) -> Self:
        if self.department != Department.IT and self.other_benifits:
            raise ValueError("Only IT employees are allowed for other benifits.")
        return self

    @validate_call
    def send_invoice(
        self,
        items_purchased: list[str],
        amount_owed: PositiveFloat,
    ) -> str:
        email_str = f"""
        Dear {self.name},

        Thank you for choosing InfocusP Innovations!
        You owe ${amount_owed:,.2f} for the following items:

        {items_purchased}
        """
        print(f"Sending email to {self.email}...")
        time.sleep(2)
        return email_str
