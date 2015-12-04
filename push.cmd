@echo off
SET /p comment=Enter commit please: 
git pull
git add -A
git commit -m "%comment%"
git push