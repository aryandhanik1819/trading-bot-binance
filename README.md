# 🚀 Binance Futures Testnet Trading Bot (Python)

A lightweight command-line trading bot built in Python that places MARKET and LIMIT orders on the Binance Futures Testnet (USDT-M).  
Designed with clean architecture, input validation, logging, and error handling.

---

## ✨ Features

- ✅ Place MARKET and LIMIT orders
- ✅ Supports BUY and SELL sides
- ✅ Binance Futures Testnet (USDT-M)
- ✅ CLI-based input using argparse
- ✅ Input validation and error handling
- ✅ Structured modular codebase
- ✅ API request/response logging
- ✅ Easily extensible architecture

---

## 📁 Project Structure
trading_bot/
├── bot/
│ ├── client.py # Binance API wrapper
│ ├── orders.py # Order placement logic
│ ├── validators.py # Input validation
│ └── logging_config.py
├── cli.py # CLI entry point
├── requirements.txt
└── README.md
---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/<your-username>/trading-bot-binance.git
cd trading-bot-binance
```
2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```
4. Configure Environment Variables

Create a .env file in project root:
API_KEY=your_binance_testnet_api_key
API_SECRET=your_binance_testnet_secret
BASE_URL=https://testnet.binancefuture.com

▶️ How to Run
✅ Market Order Example
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```
✅ Limit Order Example
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 25000
```
📊 Output Example
Order Request Summary:
symbol: BTCUSDT
side: BUY
type: MARKET
quantity: 0.01

Order Success
Order ID: 12011615063
Status: NEW
Executed Qty: 0.000
Average Price: 0.00

📝 Logging
All API requests, responses, and errors are logged into:
trading.log

This includes:
Order request payloads
Binance API responses
Network / API errors

🛡️ Error Handling
The application gracefully handles:
Invalid CLI inputs
Missing required parameters
Binance API errors
Network failures
Meaningful error messages are printed and logged.

🚀 Future Improvements
Stop-Limit / OCO orders
Order status tracking
Trade history viewer
GUI / Web interface
Risk management rules

👨‍💻 Author
Aryan Dhanik
B.Tech CSE Cyber Security Student
Position monitoring
