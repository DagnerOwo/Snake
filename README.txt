Requirements to play
install pygame
py -m pip install -U pygame
Necesario instalar git

Comandos terminal
Clonar proyecto:
git clone https://github.com/DagnerOwo/Snake.git
Sincronizar proyecto:
git pull origin master
Añadir cambios al repositorio:
1-git add -A
2-git commit -m "Cualquier texto explicativo de los cambios"
3-git push origin master

Si no puedes sincronizar porque tienes cambios que no quieres añadir:

git fetch origin
git reset --hard origin/master
git clean -f -d