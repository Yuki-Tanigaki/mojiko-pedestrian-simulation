# mojiko-pedestrian-simulation

# Dockerを使って仮想環境内で利用する方法
## WSL で systemd を有効化
Ubuntu（WSL）で：
```bash 
sudo tee /etc/wsl.conf >/dev/null <<'EOF'
[boot]
systemd=true
EOF
```
WSLを再起動する

## WSL(Ubuntu) に Docker Engine を入れて起動
```bash 
sudo apt update
sudo apt install -y docker.io
sudo systemctl enable --now docker

sudo usermod -aG docker $USER
newgrp docker
```
動作確認：
```bash 
which docker
docker info | grep -i "Operating System"
```
-> WSL 用 Dockerが表示されれば正常
> /usr/bin/docker  
> Operating System: Ubuntu 24.04 LTS

## Docker イメージの作成
```bash 
docker build -t crowdwalk:local .
```

## Docker コンテナの起動
```bash 
docker run --rm -it \
  -e DISPLAY=$DISPLAY \
  -e WAYLAND_DISPLAY=$WAYLAND_DISPLAY \
  -e XDG_RUNTIME_DIR=/mnt/wslg/runtime-dir \
  -v /mnt/wslg:/mnt/wslg \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v "$(pwd)/launcher:/work/launcher" \
  crowdwalk:local
```

## CrowdWalkの実行
確認：
```bash
sh launcher/launcher.sh -h
```
-> CrowdWalk のヘルプが表示されれば正常

GUIを使わないサンプルシナリオの実行：
```bash
sh launcher/launcher.sh launcher/properties.json -c -lError
```

GUIを使ったサンプルシナリオの実行：
（表示が出るまで時間がかかるため注意）
```bash
sh launcher/launcher.sh launcher/properties.json -g2 -lError
```

## Docker コンテナを終了
```bash
exit
```

# launcher内のファイル説明
【変更不要】
- base_configs: 具体的なシミュレーションのサンプルデータ置き場
- diagram.csv: 門司港駅の電車の発着ファイル
- GuiSimulationLauncher.ini: GUI起動時のシミュレーション表示範囲
- launcher.sh: シミュレーション起動用シェルスクリプト

【シミュレーション内容の】
- configs: 人流データや信号制御情報を置く場所
- GateOperation.rb: シミュレーション内の歩行者のルート制御時に利用されるrubyスクリプト（通行止め and 方向指示）
- properties.json: シミュレーション設定ファイル


# チュートリアルの実行
```bash
docker run --rm -it \
  -e DISPLAY=$DISPLAY \
  -e WAYLAND_DISPLAY=$WAYLAND_DISPLAY \
  -e XDG_RUNTIME_DIR=/mnt/wslg/runtime-dir \
  -v /mnt/wslg:/mnt/wslg \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v ./launcher:/launcher \
  ubuntu-py-jdk17
```