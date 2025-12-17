# mojiko-pedestrian-simulation

# Installation 
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
docker build -t ubuntu-py-jdk17 .
```

## Docker コンテナの起動
```bash 
docker run --rm -it \
  -e DISPLAY=$DISPLAY \
  -e WAYLAND_DISPLAY=$WAYLAND_DISPLAY \
  -e XDG_RUNTIME_DIR=/mnt/wslg/runtime-dir \
  -v /mnt/wslg:/mnt/wslg \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  crowdwalk-ubuntu-jdk17
```

## CrowdWalkの実行
確認：
```bash
sh quickstart.sh -h
```
-> CrowdWalk のヘルプが表示されれば正常

GUIを使わないサンプルシナリオの実行：
```bash
sh quickstart.sh sample/stop-sample2/properties.json -c -lError
```

GUIを使ったサンプルシナリオの実行：
（表示が出るまで時間がかかるため注意）
```bash
sh quickstart.sh sample/stop-sample2/properties.json -g2 -lError
```

## Docker コンテナを終了
```bash
exit
```

## 