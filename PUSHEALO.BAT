git add .
git commit -m "Auto-upgrade"
git push heroku master:main
heroku restart
heroku logs --tail