#!/bin/sh

export CROWDWALK="/opt/CrowdWalk/crowdwalk"

JAVA='java'
JAVAOPT="-Dgroovy.source.encoding=UTF-8 -Dfile.encoding=UTF-8 --add-opens java.base/sun.nio.ch=ALL-UNNAMED --add-opens java.base/java.io=ALL-UNNAMED"
JAR=$CROWDWALK/build/libs/crowdwalk.jar

$JAVA $JAVAOPT -Djdk.gtk.version=2 -jar $JAR $*
