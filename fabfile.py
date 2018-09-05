from fabric.api import env,run
from fabric.operations import  sudo

GIT_REPO = 'https://github.com/ZhaoLizz/WebServer.git'
env.user = 'root'
env.password = 'tianchao1'
env.hosts = '120.77.182.38'
env.port = 22

def deplot():
    source_folder = '/home/zhaolizhi/sites/zhaolizhi.xyz/WebServer'
    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder))
    sudo('systemctl restart zhaolizhi.xyz')
    sudo('service nginx reload')