import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://open.er-api.com/v6/latest/{base_currency.upper()}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        rate = data["rates"].get(target_currency.upper())
        if rate:
            return rate
        else:
            print("❌ Invalid target currency code.")
            return None
    except Exception as e:
        print("⚠️ Error fetching exchange rates:", e)
        return None

print("💱 Currency Converter")
print("Type 'exit' at any point to quit.\n")

while True:
    amount_input = input("Enter amount to convert: ")
    if amount_input.lower() == "exit":
        break

    try:
        amount = float(amount_input)
    except ValueError:
        print("❌ Please enter a valid number.\n")
        continue

    from_currency = input("From currency (e.g., USD): ").upper()
    if from_currency.lower() == "exit":
        break

    to_currency = input("To currency (e.g., UAH): ").upper()
    if to_currency.lower() == "exit":
        break

    rate = get_exchange_rate(from_currency, to_currency)
    if rate:
        converted = amount * rate
        print(f"✅ {amount:.2f} {from_currency} = {converted:.2f} {to_currency}\n")
