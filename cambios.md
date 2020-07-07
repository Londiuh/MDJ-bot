###### Aviso: Las versiones de MDJ-BOT ya no se encuentran en "releases" ahora debes clonar el repositorio
[Clonar repositiorio](https://github.com/Londiuh/MDJ-bot/archive/master.zip)

## v1.5.0 - 07/07/2020
- Ahora con el comando `Playlist_` pudes cambiar `tournamentID` y `eventWindowID`
- Ahora el fondo del avatar (kairos) es un degradado morado, por defecto
- Ahora `/playlist-info` muestra todas las IDs del modo en el chat

## v1.4.0 - 05/07/2020
- Errores arreglados
- Optimizaciones
- Nuevo y mejor metodo para buscar actualizaciones del bot
- Ahora `bid_557_sharksuitfemale` es la mochila por defecto
- Nuevos comandos: `/reiniciar`, `/actualizar`, `/listo`, `/nolisto (alias: /participar)` y `/noparticipar` (lee los cambios para más info)
- Ahora el bot detecta si el metodo para unirse a modos no disponibles esta parcheado
- Se ha removido la opción `sala_privacidad` ya que dejó de funcionar
- Se ha añadido la opción `todos_admins` la cual si esta activada ignorara la lista de admins y dara acceso completo a todos los usuarios
- Se ha añadido la opción `activar_apagar` la cual activa/desactiva el comando `/apagar` (util si `todos_admins` esta activado y no quieres que la gente apage el bot)
- Ahora el comando `/privacidad` muestra los argumentos correctamente
- Se ha removido `/modo gilipollas`
- La variable que contenia la configuración a sido renombrada a `config` (antes era `data`)
- Ahora las advertencias y errores se muestran usando las funciones `pError(msg)` y `pAdvertencia(msg)` (Para no tener que poner siempre los colores, hora y prefijo)
- Ahora al inciar el bot se comprueba si tienes acceso a internet
- Ahora algunos errores muestran información más detallada sobre la excepcion que ha occurido
- Se ha arreglado un error que impedia leer correctamente las autentificaciones guardadas
- Ahora puedes comprobar si hay nuevas actualizaciones mientras el bot esta en marcha con `/actualizar`
- Ahora puedes cambiar el avatar (kairos) del bot (el que se muestra en la lista de amigos) `kairos_avatar_id` y `kairos_avatar_fondo`
- Se ha cambiado el emote por defecto que hace el bot al unirse, ahora es el emote de Kit (muy gracioso la verdad)
- Ahora se puede configurar la duración del emote que hace el bot al unirse con la opción `emote_duracion` (segundos)
- Ahora el titulo es rojo y más limpio
- Ahora al utilizar `/emote` sin dar ningún EID como argumento parara el emote que el bot este bailando
- Ahora todos comandos informan en la consola
- Ahora `LIBRERIAS.bat` reinstala todas las librerias (aunque ya esten instaladas y actualizadas)
- Se han añadido las opciones `emote` y `emote_abandonar` las cuales te permiten activar/desactivar el emote que hace el bot al abandonar/unirse
- Ahora puedes cambiar el emote que hace el bot al usar `/abandonar` con la opción `emote_abandonar_id`
- Ahora el emote de abandonar por defecto es `eid_fireworks_wkx2w`
- Ahora `/apagar` apaga el bot de manera "adequada" ya que antes solo hacia un `exit()`
- Se ha añadido la opción `msg_abandonar` la cual te permite cambiar el mensaje que dice al abandonar con `/abandonar`
- Ahora el mensaje de abandono se envia al chat de sala (antes solo se enviava al jugador que ejecuto el comando)
- `Admins[...]` renombrado a `admins[...]`
- Ahora `ajustes.json` soporta caracteres unicode (utf-8)
- El ajuste `contrasena` ha sido renombrado a `contraseña`
- Se ha añadido el comando `/reiniciar` el cual te permite reiniciar el bot (no confundir con `/recragar`)
- Nueva sintaxis para el comando `/emote <EID (opcional)> <segundos (opcional)>` (si no se especifican segundos el bot bailara el emote infinitamente)
- Con los nuevos comandos: `/listo`, `/nolisto (alias: /participar)` y `/noparticipar` puedes cambiar el estado de sala de tu bot

## v1.3.0 - 21/06/2020
- Errores arreglados
- Mejoras y optimizaciones
- Correcciones ortográficas
- Nuevo método para unirse a modos, que funciona después del parche
- Nuevo ajuste `depurar_respuestas` (requiere que `depurar` este activo)
- Ahora puedes instalar las librerías abriendo `LIBRERIAS.bat`
- Nuevos comandos de depuración `/aes y Playlist_`
- Se ha arreglado el error que rompió completamente el bot después de una actualización de una librería
- Ahora, por defecto, la skin del bot es Aqua Man (antes era una skin extraña)
- Ahora se usa el código de autorización, lee la wiki. (Antes se usaba el código de intercambio)
- Se ha removido `/modo reintentar`, ya que con el nuevo método no es necesario

## v1.2.0 - 26/04/2020
- Mejoras
- Errores arreglados
- Correcciones ortograficas
- Nuevos comandos `/privacidad, /skin, /mochila, /emote`
- Nuevos ajustes (ahora puedes configurar muchas más cosas)
- He quitado el limite de tiempo (me descuide y no lo quite de la versión final)
- He quitado `/modo comida` (me olvide de quitarlo en la versión final, no funcionava)
- Archivo renombrado a **MDJ-BOT.py**
- Ahora puedes usar `/modo reintentar` si se quedo en **esperando emparejamiento...**
- Al usar `/modo <ID>` después de haver jugado un modo, el bot volvera a estar participando

## v1.0.1 - 18/04/2020
- Errores arreglados

## v1.0.0 - 17/04/2020
- Primera versión :smile:
