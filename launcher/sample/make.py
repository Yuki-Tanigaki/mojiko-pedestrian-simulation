import json
from datetime import datetime, timedelta

# 信号リスト
signals = [
    "J1", "J2",
    "G1-1", "G1-2", "G1-3",
    "G2-1", "G2-2",
    "G3-1", "G3-2",
    "G4"
]

# 時間設定
start_time = datetime.strptime("19:00:00", "%H:%M:%S")
end_time = datetime.strptime("23:00:00", "%H:%M:%S")
open_interval = 3   # 閉じたあと、次に開けるまでの間隔（分）
close_interval = 2  # 開いたあと、次に閉じるまでの間隔（分）

# イベントリスト
raw_events = []

# Initiate イベントを追加
raw_events.append({
    "atTime": start_time,
    "type": "Initiate",
    "placeTag": None
})

# 各信号は start_time に開いている → close_interval後に閉じ、open_interval後に再オープン → 繰り返し
for signal in signals:
    t = start_time

    # 最初に開いている状態なので、明示的に OpenGate を追加してもよい（任意）
    raw_events.append({
        "atTime": t,
        "type": "OpenGate",
        "placeTag": signal
    })

    t += timedelta(minutes=close_interval)

    while t <= end_time:
        # 閉じるイベント
        raw_events.append({
            "atTime": t,
            "type": "CloseGate",
            "placeTag": signal
        })
        # J1のときはAlertも追加
        if signal == "J1":
            raw_events.append({
                "atTime": t,
                "type": "Alert",
                "placeTag": "FL_J1",
                "message": "J1_open",
                "onoff": "false"
            })
            raw_events.append({
                "atTime": t,
                "type": "Alert",
                "placeTag": "FL_J1",
                "message": "J1_closed"
            })
        # J2のときはAlertも追加
        if signal == "J2":
            raw_events.append({
                "atTime": t,
                "type": "Alert",
                "placeTag": "FL_J2",
                "message": "J2_open",
                "onoff": "false"
            })
            raw_events.append({
                "atTime": t,
                "type": "Alert",
                "placeTag": "FL_J2",
                "message": "J2_closed"
            })
        
        t += timedelta(minutes=open_interval)
        if t > end_time:
            break

        # 開けるイベント
        raw_events.append({
            "atTime": t,
            "type": "OpenGate",
            "placeTag": signal
        })
        # J1のときはAlertも追加
        if signal == "J1":
            raw_events.append({
                "atTime": t,
                "type": "Alert",
                "placeTag": "FL_J1",
                "message": "J1_closed",
                "onoff": "false"
            })
            raw_events.append({
                "atTime": t,
                "type": "Alert",
                "placeTag": "FL_J1",
                "message": "J1_open"
            })
        # J2のときはAlertも追加
        if signal == "J2":
            raw_events.append({
                "atTime": t,
                "type": "Alert",
                "placeTag": "FL_J2",
                "message": "J2_closed",
                "onoff": "false"
            })
            raw_events.append({
                "atTime": t,
                "type": "Alert",
                "placeTag": "FL_J2",
                "message": "J2_open"
            })
        t += timedelta(minutes=close_interval)

# 時間で整列
raw_events.sort(key=lambda e: e["atTime"])

# 時刻を文字列に変換、placeTag=None は省略
events = []
for e in raw_events:
    event = {
        "atTime": e["atTime"].strftime("%H:%M:%S"),
        "type": e["type"]
    }
    if e["placeTag"] is not None:
        event["placeTag"] = e["placeTag"]
    events.append(event)

# JSON出力
with open("generated_signals.json", "w", encoding="utf-8") as f:
    json.dump(events, f, ensure_ascii=False, indent=2)

print("generated_signals.json を出力しました。")
