def middleware(value: str) -> str:
    print("Before execution")
    result = value.strip()
    print("After execution")
    return result


if __name__ == "__main__":
    print(middleware("  hello from the example  "))
