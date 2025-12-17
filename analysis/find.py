import pandas as pd

# CSV読み込み
df = pd.read_csv("log/log_individual_pedestrians.csv")

# グリッドサイズ
grid_size = 10

# グリッド化
df["grid_x"] = (df["current_position_in_model_x"] // grid_size).astype(int)
df["grid_y"] = (df["current_position_in_model_y"] // grid_size).astype(int)

# 有効グリッドの抽出
valid_grids = df.groupby(["grid_x", "grid_y"]).size().reset_index()[["grid_x", "grid_y"]]

# 出力
valid_grids.to_csv("valid_grids.csv", index=False)
print("✅ 有効グリッド一覧を書き出しました: valid_grids.csv")
