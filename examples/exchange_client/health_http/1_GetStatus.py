import requests

def main() -> None:
    r = requests.get('https://sentry1.injective.network:4444/api/health/v1/status', verify=False)
    print(r.text)

if __name__ == '__main__':
    main()
