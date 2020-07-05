echo off
cls
color E
echo -----------------------------------------------------------------------
echo Si no hay permisos de escritura, las librerias se instalaran en AppData
echo -----------------------------------------------------------------------
:Parpadeo un poco cutre, con PINGs lol
ping -n 2 127.0.0.1>nul
color C
ping -n 2 127.0.0.1>nul
color E
cls
color 07
py -3 -m pip install --user --force-reinstall --requirement librerias.txt
cmd /k
