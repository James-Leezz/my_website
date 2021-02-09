uwsgi --http 0.0.0.0:9000 --chdir /root/my_website/mywebsite_v1 --wsgi-file mywebsite_v1/wsgi.py --static-map=/static=static --master --processes 4 --threads 2
##########this is for uwsgi
