# 💱 Currency Converter

A beginner-friendly Python script that allows users to convert an amount from one currency to another using real-time exchange rates from the [Open ER API](https://open.er-api.com/).

---

## ✨ Features

- 🔄 Converts any amount between two supported currencies
- 🌍 Supports most global currency codes (USD, EUR, UAH, PLN, CZK, etc.)
- ⚠️ Gracefully handles invalid currency codes
- 🔁 Allows repeated conversions without restarting
- 🔌 Uses the free [open.er-api.com](https://open.er-api.com/) API

---

## 🛠️ Tech Stack

- Python 3
- `requests` — for making API requests

---

## ▶️ How to Run

1. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

2. **Run the script**

    ```bash
    python exchange_converter.py
    ```

---

## 💡 Example

```text
Enter amount to convert: 10
From currency (e.g., USD): eur
To currency (e.g., UAH): pln

✅ 10.00 EUR = 42.37 PLN

*****

👨‍💻 Author
Created with ❤️ by Ihor Danylenko
📧 Email: danylenkoigor25@gmail.com
🔗 GitHub: github.com/Ihor3000

*****

📄 License
This project is licensed under the MIT License — feel free to use, modify, and share.
