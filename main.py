# main fayl yaratildi




from datetime import date


class User:
    ADULT_AGE = 18

    def __init__(self, first_name: str, last_name: str, birth_year: int):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self) -> int:
        return date.today().year - self.birth_year

    def is_adult(self) -> bool:
        return self.age >= self.ADULT_AGE

    @staticmethod
    def _ask_text(prompt: str) -> str:
        while True:
            value = input(prompt).strip()
            if value.isalpha():
                return value.capitalize()
            print("Faqat harflardan iborat bo'lsin, qaytadan kiriting.")

    @staticmethod
    def _ask_year(prompt: str) -> int:
        current_year = date.today().year
        while True:
            value = input(prompt).strip()
            if value.isdigit() and 1900 <= int(value) <= current_year:
                return int(value)
            print(f"1900 va {current_year} oralig'idagi yil kiriting.")

    @classmethod
    def from_input(cls) -> "User":
        first_name = cls._ask_text("Ismingiz: ")
        last_name = cls._ask_text("Familiyangiz: ")
        birth_year = cls._ask_year("Tug'ilgan yilingiz: ")
        return cls(first_name, last_name, birth_year)

    def __str__(self) -> str:
        status = "voyaga yetgan" if self.is_adult() else "voyaga yetmagan"
        return f"{self.full_name}, {self.age} yosh — {status}"


if __name__ == "__main__":
    user = User.from_input()
    print(user)