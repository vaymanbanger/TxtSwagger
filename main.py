from src.txtswagger import extract_name_from_url


def main():
    url = input("Введите URL вашей API: ")
    resource_name = extract_name_from_url(url)
    print(resource_name)
    
if __name__ == "__main__":
    main()