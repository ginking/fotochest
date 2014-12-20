### 3.1.1 - Released 11-22-2014

Like all upgrades we suggest doing a full database and data (media) backup before proceeding with
an update.  Once you've backed those two things up, continue on.

#### Checkout

```
git fetch
git checkout 3.1.1
```

#### Upgrade Packages

Using your virtualenv (if you set one up):

```
pip install -r requirements.txt
```

#### Collect static

```
python manage.py colectstatic
```


#### Restart Gunicorn

```
sudo supervisorctl
restart YOUR_FOTOCHEST_PROGRAM
```