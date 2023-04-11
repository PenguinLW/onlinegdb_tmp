#in venv
. ~/venv/bin/activate
#pip install -r req.txt
pip freeze > req.txt
chmod u+x *.sh *.py
#git clone -o onlinegdb_tmp https://github.com/PenguinLW/onlinegdb_tmp.git
#git config --global user.email "diana1997525@gmail.com"
#git config --global user.name "PenguinLW"
#git config --global credential.helper cache
git config --global credential.helper "cache --timeout=25200"
#git config credential.helper store
#git config --unset credential.helper
git pull --all
git add .
git commit -m PenguinL
git push --set-upstream onlinegdb_tmp master
#deactivate
