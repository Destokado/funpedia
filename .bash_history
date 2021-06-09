#1619643306
webservice
#1619643343
webservice -start
#1619643352
webservice start
#1619643415
mkdir public_html
#1619643419
dir
#1619643435
echo '<html><head></head><body>Hello!<?php ?></body></html>' > public_html/index.php
#1619643444
webservice start
#1619643562
webservice stop
#1619644183
sh -v destokado.wcdo.eqiad1.wikimedia.cloud
#1619644197
sh -v destokado@wcdo.eqiad1.wikimedia.cloud
#1619648965
exit
#1623240022
mkdir -p %HOME/www/python/src
#1623240044
webservice --backend=kubernetes python3.9 shell
#1623240071
webservice --backend=kubernetes python3.7 shell
python3 -m venv $home/www/python/venv
ls
cd %home
ls
cd destokado
cd funpedia
rmdir %HOME
rm -r %HOME
ls
mkdir -p $HOME/www/python/src
webservice --backed=kubernetes python3.7 shell
webservice --backend=kubernetes python3.5 shell
webservice --backend=kubernetes python3.7 shell
ls
cd www
ls
cd python
ls
cd src
ls
ls
cd ..
cd
ls
rmdir -r www
rm -r www
ls
cd ..
ls
cd destokado
cd funpedia
ls
cd ..
cd contropedia
ls
logs
open logs
cd ..
cd funpedia
ls
webservice --backend=kubernetes python3.7 shell
python3 -m venv $HOME/www/python/activate
pip install --upgrade pip
pip install
cd www/python
ls
rm -r activate
ls
cd
ls
python3 -m venv $HOME/www/python/venv
source $HOME/www/python/venv/bin/activate
pip install --upgrade pip
cat > $HOME/www/python/src/requirements.txt << EOF
flask
EOF

pip install -r $HOME/www/python/src/requirements.txt
cat > $HOME/www/python/src/requirements.txt << EOF
flask
EOF

EOF
exit
#1623242194
ls
#1623242200
git init
#1623242208
git add public_html
#1623242219
git commit -m 'Initial check-in'
#1623242249
git config --global --edit
#1623242305
ls
#1623242320
mkdir ~/www
#1623242328
mkdir ~/www/static/
#1623242334
cd www/static
#1623242336
ls
#1623242375
ln -s ~/.git funpedia.git
#1623242403
cd funpedia.git
#1623242410
git update-server-info
#1623242432
ln -s hooks/post-update.sample hooks/post-commit
#1623242432
ln -s hooks/post-update.sample hooks/post-rewrite
#1623242432
ln -s hooks/post-update.sample hooks/post-update
#1623242433
chmod a+x hooks/post-update.sample
#1623243282
ls
#1623243290
cd
#1623243294
ls
#1623243309
git clone https://github.com/Destokado/funpedia.git
#1623243324
ls
#1623244220
cd funpedia
#1623244224
git pull
#1623244338
ls
#1623244372
cat readme.md
#1623244376
cat README.md
#1623244397
git pull
#1623244402
cat README.md
#1623244697
ls
#1623244698
cd
#1623244700
ls
#1623244708
cd
#1623244710
ls
#1623244714
cd ..
#1623244715
ls
#1623244727
cd funpedia
#1623244728
ls
#1623245705
ls
#1623245713
git add -all
#1623245852
yes
#1623245903
git add -all
#1623245913
git add --all
#1623245942
git push
#1623245963
git push
#1623246048
git commit
#1623246150
git push
#1623246415
mkdir -p $HOME/www/python/src
#1623246417
ls
#1623246441
webservice --backend=kubernetes python3.7 shell
#1623247020
edit $HOME/www/python/src/app.py 
source $HOME/www/python/venv/bin/activate
cat >> $HOME/www/python/src/requirements.txt << EOF
pyyaml
EOF

pip install -r $HOME/www/python/src/requirements.txt
exit
source $HOME/www/python/venv/bin/activate
cat >> $HOME/www/python/src/requirements.txt << EOF
mwoauth
EOF

pip install -r $HOME/www/python/src/requirements.txt
exit
#1623247368
ls
#1623247435
vim $HOME/www/python/src/app.py
#1623247633
webservice --backend=kubernetes --canonical python3.7 restart
#1623248254
webservice --backend=kubernetes --canonical python3.7 restart
#1623248314
webservice --backend=kubernetes python3.7 shell
#1623248433
touch $HOME/www/python/src/config.yaml
#1623248454
chmod u=rw,go= $HOME/www/python/src/config.yaml
#1623248461
cat > $HOME/www/python/src/config.yaml << EOF
GREETING: Goodnight moon!
EOF

#1623248481
webservice restart
#1623248511
webservice --backend=kubernetes python3.7 shell
#1623248972
mkdir $HOME/www/python/src/templates
#1623248980
edit $HOME/www/python/src/templates/index.html
#1623249926
webservice restart
#1623250017
git add --all
#1623250060
git commit -m "My first flask app"
#1623250121
git push origin master
#1623250128
git push
#1623250148
git push
