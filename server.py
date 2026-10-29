from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

# =====================================================
# HOME
# =====================================================

@app.route("/")
def home():

    return jsonify({
        "status": "MONSTER V9 PAPER TRADING",
        "api_key": bool(os.getenv("BITGET_API_KEY")),
        "secret": bool(os.getenv("BITGET_API_SECRET")),
        "passphrase": bool(os.getenv("BITGET_PASSPHRASE"))
    })

# =====================================================
# WEBHOOK
# =====================================================

@app.route("/webhook", methods=["POST"])
def webhook():

    data = request.get_json(force=True)

    action = data.get("action")
    symbol = data.get("symbol")
    price = data.get("price")
    timeframe = data.get("timeframe")

    print("=" * 60, flush=True)

    print(
        f"[{datetime.now()}] "
        f"ACTION={action} "
        f"SYMBOL={symbol} "
        f"PRICE={price} "
        f"TIMEFRAME={timeframe}",
        flush=True
    )

    if action == "LONG":
        print("PAPER: OPEN LONG", flush=True)

    elif action == "SHORT":
        print("PAPER: OPEN SHORT", flush=True)

    elif action == "EXIT_LONG":
        print("PAPER: CLOSE LONG", flush=True)

    elif action == "EXIT_SHORT":
        print("PAPER: CLOSE SHORT", flush=True)

    else:
        print(f"PAPER: UNKNOWN ACTION {action}", flush=True)

    print("=" * 60, flush=True)

    return jsonify({
        "success": True,
        "action": action,
        "symbol": symbol,
        "price": price,
        "timeframe": timeframe,
        "mode": "paper"
    })

# =====================================================
# START
# =====================================================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
