import requests

def get_ip():
    try:
        response = requests.get("https://api64.ipify.org?format=json")
        response.raise_for_status()
        ip = response.json().get("ip", "Unavailable")
        print(f"Your current IP address is: {ip}")
    except requests.RequestException as e:
        print(f"Error fetching IP address: {e}")

if __name__ == "__main__":
    get_ip()
