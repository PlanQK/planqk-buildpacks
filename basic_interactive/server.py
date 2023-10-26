import os

def main():
    print("It shall run")

    name = os.environ.get("NAME")
    if name:
        print(f"Hello, {name}!")
    else:
        print("Name wurde nicht übergeben")

if __name__ == "__main__":
    main()
