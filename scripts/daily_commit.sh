#!/bin/bash
cd ~/Desktop/dobby
git add .
CHANGES=$(git status --porcelain)
if [ -n "$CHANGES" ]; then
    git commit -m "$(date '+%Y-%m-%d') 업무 기록 자동 커밋"
    git push
fi
