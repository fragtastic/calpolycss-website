# calpolycss-website
Website for http://calpolycss.com

# Commiting
## Style
- Single commit == single purpose. Don't pack a lot into one.
- Ctrl+Alt+L format in PyCharm. 

## Bootlint
Check for errors with https://github.com/twbs/bootlint#in-the-browser

# Install
## deps
```
apt-get install python python-pip nginx
```

## source
```
mkdir -p /srv/http
chown www-data:www-data /srv/http
su www-data
cd /srv/http
git clone https://github.com/fragtastic/calpolycss-website
```

## venv
```
cd /srv/http/calpolycss-website
virtualenv env
source env/bin/activate
pip install flask gunicorn
deactivate
```

## init
```
ln -s /srv/http/calpolycss-website/calpolycss /etc/init.d/calpolycss
chmod +x /etc/init.d/calpolycss
```

## nginx
```
ln -s /srv/http/calpolycss-website/calpolycss.com.conf /etc/nginx/sites-enabled/calpolycss.com.conf
```

## Start/stop/status
```
/etc/init.d/calpolycss start
/etc/init.d/calpolycss status
/etc/init.d/calpolycss stop
```