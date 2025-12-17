FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# Java / Python / git / JavaFX
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    git \
    curl \
    tzdata \
    python3 \
    python3-pip \
    python3-venv \
    openjdk-17-jdk \
    openjfx \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Java env
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="${JAVA_HOME}/bin:${PATH}"

# 文字化け対策（Gradle/Groovy/Java）
ENV JAVA_OPTS="-Dgroovy.source.encoding=UTF-8 -Dfile.encoding=UTF-8"
ENV GRADLE_OPTS="-Dfile.encoding=UTF-8"
ENV GROOVY_OPTS="-Dgroovy.source.encoding=UTF-8"

# ---- CrowdWalk を取得 ----
WORKDIR /opt

# 更新しやすいようにブランチ/タグを指定可能にする
ARG CROWDWALK_REF=master

RUN git clone --depth 1 --branch "${CROWDWALK_REF}" https://github.com/crest-cassia/CrowdWalk.git

# ---- ビルド（質問の ./gradlew に相当）----
WORKDIR /opt/CrowdWalk/crowdwalk

# gradlew を確実に実行可能に
RUN chmod +x ./gradlew

# 依存取得＆ビルド（必要に応じて tasks/build に置き換え可）
RUN ./gradlew --no-daemon

CMD ["bash"]
