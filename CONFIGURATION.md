# シミュレーション設定ファイルのパラメータに関する説明

### ファイル指定関連

| パラメータ | 説明 |
| --- | --- |
| `map_file` | 地図情報を含むXMLファイル（例：建物や道路のレイアウト） |
| `generation_file` | エージェント（人など）の生成ルールを定義したファイル |
| `scenario_file` | シミュレーション実行中に発生させるイベントのスケジュールを定義したファイル |
| `fallback_file` | シミュレーションで使うエージェントの生成、移動ルールなどを定義したファイル |
| `node_appearance_file` | ノード（交差点・建物など）の表示スタイル定義 |
| `link_appearance_file` | リンク（道など）の表示スタイル定義 |
| `polygon_appearance_file` | ポリゴン（建物形状など）の表示スタイル定義 |
| `camera_file` | 3Dビューのカメラ設定 |
| `camera_2d_file` | 2Dビューのカメラ設定 |

---

### 表示・描画設定

| パラメータ | 説明 |
| --- | --- |
| `show_background_map` | 背景地図を表示するかどうか |
| `gsi_tile_name` | 国土地理院などの地図タイル名
"ort"は航空写真のこと |
| `gsi_tile_zoom` | 地図タイルのズームレベル |

---

### シミュレーション制御

| パラメータ | 説明 |
| --- | --- |
| `randseed` | シミュレータの乱数シード |
| `exit_count` | **詳細不明（0にしておけば動く）** |
| `all_agent_speed_zero_break` | 全エージェントの速度が0になったらシミュレーションを終了する |

---

### ログ・履歴関連

| パラメータ | 説明 |
| --- | --- |
| `create_log_dirs` | ログディレクトリを自動作成するかどうか |
| `agent_movement_history_file` | エージェントの移動履歴を保存するCSVファイルパス |
| `individual_pedestrians_log_dir` | 個別のエージェントログ出力ディレクトリ |
| `evacuated_agents_log_file` | 移動完了エージェントのログ出力ファイル |

---

### スクリーンショット・記録関連

| パラメータ | 説明 |
| --- | --- |
| `record_simulation_screen`  | シミュレーション画面を動画として記録するか |
| `screenshot_dir` | スクリーンショット保存先 |
| `clear_screenshot_dir` | シミュレーション開始時にスクリーンショットディレクトリを初期化するか |
| `screenshot_image_type` | スクリーンショットの画像形式（例: png, jpg） |

---

### ビジュアル設定

| パラメータ | 説明 |
| --- | --- |
| `agent_size` | エージェントの表示サイズ |
| `zoom` | 画面表示のズームレベル |
| `show_3D_polygon` | 3Dポリゴンを表示するか |
| `change_agent_color_depending_on_speed` | エージェントの速度に応じて色を変更するか |
| `show_status` | ステータス表示位置（例: Bottom, Topなど） |
| `show_logo` | ロゴ表示の有無 |

---

### 起動・終了挙動

| パラメータ | 説明 |
| --- | --- |
| `exit_with_simulation_finished`  | シミュレーション完了後に自動終了するか |
| `simulation_window_open` | ウィンドウを表示するか（falseで非表示実行） |
| `auto_simulation_start` | 起動時に自動でシミュレーションを開始するか |

---

### Rubyによる拡張設定（スクリプト連携）

| パラメータ | 説明 |
| --- | --- |
| `use_ruby` | Rubyスクリプトを使用するか |
| `ruby_load_path`  | Rubyのロードパス（スクリプトの検索場所） |
| `ruby_simulation_wrapper_class` | Ruby側で使用するクラス名（例：GateOperation） |
| `ruby_init_script` | Rubyスクリプトの実行前に実行されるRubyコード。ゲート通過者数のカウント設定などを行っている |

### `ruby_init_script` の中身について

- `monitor`: 状態をコンソールに出力するか
- `gate_node_tag`: ゲートとして扱うノードのタグ（1つ限定）
- `count_by_entering`: 入場か退場かをカウント対象にするか
- `counting_positions`: カウント対象となるリンク・ノードのタグ一覧
- `delay_time`: 電車ドア開放から乗車完了までの待ち時間（秒）
- `diagram_file`: 運行表CSVファイル（乗車時刻や収容人数を記述）