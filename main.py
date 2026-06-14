import requests

print("\n--- CRYPTO TRACKER ---\n")

coin = input("Enter coin: ").lower()

try:
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    res = requests.get(url)
    data = res.json()

    if coin in data:
        print("Price:", data[coin]["usd"], "USD")
    else:
        print("Invalid coin")

except:
    print("Error")