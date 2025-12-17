import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSV読み込み
df = pd.read_csv("log/log_individual_pedestrians.csv")

# パラメータ設定
grid_size = 10  # 10m × 10m

# 座標をグリッドに変換
df["grid_x"] = (df["current_position_in_model_x"] // grid_size).astype(int)
df["grid_y"] = (df["current_position_in_model_y"] // grid_size).astype(int)

# 有効グリッドの一覧を抽出（全期間通して一度でも通過があったグリッド）
valid_grids = df.groupby(["grid_x", "grid_y"]).size().reset_index()[["grid_x", "grid_y"]]
valid_grids_set = set([tuple(x) for x in valid_grids.to_numpy()])

# Gini係数を計算する関数
def gini(array):
    if len(array) == 0:
        return np.nan
    array = np.sort(np.array(array))
    n = len(array)
    mean = np.mean(array)
    if mean == 0:
        return 0
    diff_sum = np.sum(np.abs(array[:, None] - array))
    return diff_sum / (2 * n**2 * mean)

# 時刻ごとのGini係数リスト
gini_per_time = []

# 各時刻について計算
for time, group in df.groupby("current_time"):
    # この時刻のグリッドカウント
    grid_counts = group.groupby(["grid_x", "grid_y"]).size()

    # 有効グリッドすべてに対してカウント（通っていないグリッドは0）
    full_counts = []
    for gx, gy in valid_grids_set:
        count = grid_counts.get((gx, gy), 0)
        full_counts.append(count)

    g = gini(full_counts)
    gini_per_time.append(g)

# 全時刻の平均Gini
average_gini = np.nanmean(gini_per_time)

print(f"Average Gini Coefficient over all time steps (valid grids only): {average_gini:.4f}")

# ここから可視化
# 各時刻・グリッドの人数をカウント
grouped = df.groupby(["current_time", "grid_x", "grid_y"]).size().reset_index(name="count")

# グリッドごとの平均人数を計算
mean_density = grouped.groupby(["grid_x", "grid_y"])["count"].mean().reset_index()

# ピボットしてヒートマップ描画用に整形
pivot = mean_density.pivot(index="grid_y", columns="grid_x", values="count")

# 可視化
plt.figure(figsize=(8, 6))
plt.imshow(pivot.fillna(0), origin="lower", cmap="hot")
plt.colorbar(label="Average Pedestrian Count")
plt.title("Average Pedestrian Density Over Time")
plt.xlabel("Grid X")
plt.ylabel("Grid Y")
plt.savefig("density.png")
