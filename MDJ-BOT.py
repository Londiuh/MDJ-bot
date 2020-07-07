#!/usr/bin/env python3

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m' 
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

try:
    import fortnitepy
    from fortnitepy.errors import *
    import asyncio
    import time
    import datetime
    import json
    import aiohttp
    import base64
    import time
    import logging
    import functools
    import sys
    import os
    import requests
    import webbrowser
    from colorama import init
    init(autoreset=True)
    from colorama import Fore, Back, Style
except ModuleNotFoundError as e:
    print(color.RED + f"[ERROR CRITICO] Problema al importar 1 o más librerias ({e})")
    exit()

config = None
auth = None
vlocal = json.load(open("version.json"))

print(f'  ')
print(color.RED + f'\t\t\t███╗   ███╗██████╗      ██╗      ██████╗  █████╗ ████████╗')
print(color.RED + f'\t\t\t████╗ ████║██╔══██╗     ██║      ██╔══██╗██╔══██╗╚══██╔══╝')
print(color.RED + f'\t\t\t██╔████╔██║██║  ██║     ██║█████╗██████╦╝██║  ██║   ██║   ')
print(color.RED + f'\t\t\t██║╚██╔╝██║██║  ██║██╗  ██║╚════╝██╔══██╗██║  ██║   ██║   ')
print(color.RED + f'\t\t\t██║ ╚═╝ ██║██████╔╝╚█████╔╝      ██████╦╝╚█████╔╝   ██║   ')
print(color.RED + f'\t\t\t╚═╝     ╚═╝╚═════╝  ╚════╝       ╚═════╝  ╚════╝    ╚═╝   ')
eval(compile(base64.b64decode('Y3JkMT1UcnVlDQpwcmludChjb2xvci5EQVJLQ1lBTitmIiBcdFx0XHRcdCIrYmFzZTY0LmI2NGRlY29kZSgiVlc1aElHTnZjMkVnYUdWamFHRWdjRzl5SUVWc1RHOXVaR2wxYUE9PSIuZW5jb2RlKCdhc2NpaScpKS5kZWNvZGUoJ2FzY2lpJykp'),'','exec'))
print(f'  ') 
print(color.DARKCYAN + f"Versión: {vlocal['major']}.{vlocal['minor']}.{vlocal['patch']}")

#Funciones y mierdas
def es_numero(str_num: str, convertir: bool) -> bool:
    try:
        num = float(str_num)
        if convertir:
            return True, num
        return True
    except:
        return False

def getTiempesito() -> str:
    tiempesito = datetime.datetime.now().strftime('%H:%M:%S')
    return tiempesito

def pAdvertencia(msg: str) -> None:
    print(Fore.BLACK + Back.YELLOW + f"[{getTiempesito()}] [ADVERTENCIA] " + msg + Style.RESET_ALL)

def pError(msg: str) -> None:
    print(Fore.BLACK + Back.RED + f"[{getTiempesito()}] [ERROR] " + msg + Style.RESET_ALL)

try:
    requests.get("http://216.58.192.142")
except Exception as e:
    pError(f"No dispones de acceso a internet ({e})")
    exit()

def buscarUpdate() -> bool:
    print(Fore.MAGENTA + f"[{getTiempesito()}] Buscando actualizaciones...")
    veRepo = json.loads(requests.get("https://raw.githubusercontent.com/Londiuh/MDJ-bot/master/version.json").text)
    if veRepo["major"] > vlocal["major"] or veRepo["minor"] > vlocal["minor"] or veRepo["patch"] > vlocal["patch"]:
        pAdvertencia(f"Hay una actualización disponible: {veRepo['major']}.{veRepo['minor']}.{veRepo['patch']}")
        if veRepo["msg"]:
            pAdvertencia(f"Mensaje importante sobre la actualización: {veRepo['msg_contenido']}")
        return True, f"{veRepo['major']}.{veRepo['minor']}.{veRepo['patch']}"
    else:
        print(color.YELLOW + f"[{getTiempesito()}] ¡Tienes la última versión! ({vlocal['major']}.{vlocal['minor']}.{vlocal['patch']})")
        return False

if buscarUpdate():
    print(Fore.GREEN + f"[¿?] ¿Deseas ver la lista de cambios? " + color.CYAN + "Si | No")
    vresp = input()
    if vresp.lower() == "si":
        webbrowser.open("https://github.com/Londiuh/MDJ-bot/blob/master/cambios.md")
        exit()

def cargarAjustes():
    try:
        with open("ajustes.json", encoding="utf-8") as f:
            print(color.YELLOW + f"[{getTiempesito()}] Cargando 'ajustes.json'...")
            time.sleep(1)
            global config
            config = json.load(f)
            print(color.GREEN + f"[{getTiempesito()}] ¡Ajustes cargados con éxito!")
    except Exception as e:
        pError(f"Ha ocurrido un problema al cargar 'ajustes.json' ({e})")
        exit()

cargarAjustes()

if config["depurar"]:
    print(color.YELLOW + f"[{getTiempesito()}] La depuración está activada.")
    if config["depurar_respuestas"]:
        logger = logging.getLogger("fortnitepy.xmpp")
        logger.setLevel(level=logging.DEBUG)
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
        logger.addHandler(handler)
        print(color.YELLOW + f"[{getTiempesito()}] La depuración de respuestas HTTP está activada.")

if config["depurar_respuestas"] and not config["depurar"]:
    pAdvertencia("'depurar_respuestas' esta activado pero 'depurar' no")

time.sleep(0.1)  
print(color.BLUE + f"\n---------------------------------------------------------------------")
listo = False

if config['plataforma'].lower() in ["win", "windows"]:
    plataforma = fortnitepy.Platform.WINDOWS
elif config['plataforma'].lower() in ["mac", "macintosh"]:
    plataforma = fortnitepy.Platform.MAC
elif config['plataforma'].lower() in ["psn", "playstation"]:
    plataforma = fortnitepy.Platform.PLAYSTATION
elif config['plataforma'].lower() in ["xb", "xbox"]:
    plataforma = fortnitepy.Platform.XBOX
elif config['plataforma'].lower() in ["ns", "switch"]:
    plataforma = fortnitepy.Platform.SWITCH
elif config['plataforma'].lower() == "ios":
    plataforma = fortnitepy.Platform.IOS
elif config['plataforma'].lower() in ["and", "android"]:
    plataforma = fortnitepy.Platform.ANDROID
else:
    plataforma = fortnitepy.Platform.SWITCH
    pAdvertencia("{config['plataforma']} no es una plataforma válida")
    pAdvertencia("Se ha puesto la plataforma en SWITCH")

#Autentificación
def get_detalles_autentificacion():
    if os.path.isfile("auths.json"):
        with open('auths.json', 'r') as fp:
            return json.load(fp)
    else:
        with open('auths.json', 'w+') as fp:
            fp.write('{}')
            
    return {}

def store_detalles_autentificacion(email, details):
    existing = get_detalles_autentificacion()
    existing[email] = details

    with open('auths.json', 'w') as fp:
        json.dump(existing, fp, sort_keys=False, indent=4)

device_auth_details = get_detalles_autentificacion().get(config["correo"], {})

client = fortnitepy.Client(
    auth=fortnitepy.AdvancedAuth(
        email=config["correo"],
        password=config["contraseña"],
        prompt_authorization_code=True,
        delete_existing_device_auths=False,
        **device_auth_details
    ),
    status=config["estado"],
    platform=plataforma,
    avatar=fortnitepy.Avatar(asset=config["kairos_avatar_id"], background_colors=config["kairos_avatar_fondo"])
)

#Eventos y comandos
@client.event
async def event_device_auth_generate(details: dict, email: str) -> None:
    store_detalles_autentificacion(email, details)


@client.event
async def event_ready():
    print(color.BLUE + f"[{getTiempesito()}] ¡El bot se incició exitosamente!")
    print(color.BLUE + "\n---------------------------------------------------------------------") 
    member = client.party.me
    await member.edit_and_keep(
        functools.partial(fortnitepy.ClientPartyMember.set_outfit, asset=config["skin_id"]),
        functools.partial(fortnitepy.ClientPartyMember.set_backpack, asset=config["mochila_id"]),
        functools.partial(fortnitepy.ClientPartyMember.set_banner, icon=config["escudo"], color=config["escudo_color"], season_level=config["nivel_pase"])
    )

@client.event
async def event_restart():
    print(Fore.GREEN + f"[{getTiempesito()}] ¡El bot se ha reiniciado correctamente!")

@client.event
async def event_party_invite(invite):
    if config['unirseinvitaciones']:
        try:
            await invite.accept()
            print(Fore.BLUE + f'[{getTiempesito()}] Se ha aceptado una invitación de sala de {invite.sender.display_name}')
        except Exception as e:
            pass
    else:
        if invite.sender.display_name in config["admins"]:
            await invite.accept()
            print(Fore.BLUE + f'[{getTiempesito()}] Se ha aceptado una invitación de sala de {invite.sender.display_name}')
        else:
            print(Fore.BLACK + Back.YELLOW + f'[{getTiempesito()}] Se ha rechazado una invitación de sala de {invite.sender.display_name} (Motivo: unirseinvitaciones esta desactivado y no es admin)')
            await invite.sender.send(f"Este bot no puede aceptar tu invitación de partida ahora mismo porque no eres admin.")
            await invite.sender.send(f"Si conoces a la persona que esta controlando a este bot puedes pedirle que active la habilidad de aceptar invitaciones o te haga admin.")
            await invite.sender.send(base64.b64decode("VGFtYmnDqW4gcHVlZGVzIGNvbnNlZ3VpciB0dSBwcm9waW8gYm90IGVuOiBodHRwczovL2dpdGh1Yi5jb20vTG9uZGl1aC9NREotYm90".encode('ascii')).decode('ascii'))

@client.event
async def event_friend_request(request):
    if config['aceptaramigos']:
        await request.accept()
        print(Fore.BLUE + f"[{getTiempesito()}] Se ha aceptado la petición de amistad de {request.display_name}")
    else:
        if request.display_name in config["admins"]:
            await request.accept()
            print(Fore.BLUE + f"[{getTiempesito()}] Se ha aceptado la petición de amistad de {request.display_name}")  
        else:
            print(Fore.BLACK + Back.YELLOW + f"[{getTiempesito()}] Se ha rechazado la petición de amistad de {request.display_name} (Motivo: aceptaramigos esta desactivado y no es admin)")

@client.event
async def event_party_member_join(member):
    eval(compile(base64.b64decode('Z2xvYmFsIGNyZDINCmNyZDIgPSBUcnVl'),'','exec'))
    await client.party.send(base64.b64decode("RXN0ZSBib3QgaGEgc2lkbyBjcmVhZG8gcG9yIEVsTG9uZGl1aC4gUHVlZGVzIGVjb250cmFybG8gZW4gZWwgcmVwb3NpdGlvcmlvIG9maWNpYWw6IGh0dHBzOi8vZ2l0aHViLmNvbS9Mb25kaXVoL01ESi1ib3Q=".encode('ascii')).decode('ascii'))
    eval(compile(base64.b64decode('aWYiY3JkMiJub3QgaW4gZ2xvYmFscygpOmV4aXQoKQ=='),'','exec'))
    if client.user.display_name != member.display_name:
        print(Fore.BLUE + f"[{getTiempesito()}] {member.display_name} se ha unido a la sala.")
    # TODO: emojis
    if config["emote"]:
        time.sleep(1)
        await client.party.me.set_emote(asset=config["emote_id"], run_for=config["emote_duración"])

@client.event
async def event_friend_message(message):
    eval(compile(base64.b64decode('aWYiY3JkMiJub3QgaW4gZ2xvYmFscygpOmV4aXQoKQ=='),'','exec'))
    args = message.content.split()
    split = args[1:]
    joinedArguments = " ".join(split)
    print(f"[{getTiempesito()}] " + "{0.author.display_name}: {0.content}".format(message))
    pre = config["prefijo"]
    
    # TODO: nuevo sistema comandos (fortnitepy.ext.commands)
    #Tener que reescribir todo el sitema de comandos me da mucha pereza
    # TODO: comandos no admin, piedra papel tijera...
    # TODO: /skin, /mochila, /emote... para gente que no sabe las IDs
    # TODO: poder configurar que comandos son admin
    if message.author.display_name in config["admins"] or config["todos_admins"]:
        '''
        if pre + "region" in args[0]:
            if len(args) == 2:
                await client.party.set_playlist(region=args[1])

        elif pre + "userid" in args[0]:
            usuario = await client.fetch_profile(joinedArguments)
            miembro = client.party.members.get(usuario.id)
            if miembro == None:
                await message.reply("Error: Ese usuario no existe o no esta en tu sala")
            else:
                await message.reply(f"ID: {miembro}")
                print(miembro)
        '''
        if pre + "nolisto" in args[0] or pre + "participar" in args[0]:
            await client.party.me.set_ready(fortnitepy.ReadyState.NOT_READY)
            await message.reply("Estado de sala cambiado a: no listo")
            print(Fore.GREEN + f"[{getTiempesito()}] Estado de sala cambiado a: no listo") 

        elif pre + "listo" in args[0]:
            await client.party.me.set_ready(fortnitepy.ReadyState.READY)
            await message.reply("Estado de sala cambiado a: listo")
            print(Fore.GREEN + f"[{getTiempesito()}] Estado de sala cambiado a: listo") 

        elif pre + "noparticipar" in args[0]:
            await client.party.me.set_ready(fortnitepy.ReadyState.SITTING_OUT)
            await message.reply("Estado de sala cambiado a: no participando")
            print(Fore.GREEN + f"[{getTiempesito()}] Estado de sala cambiado a: no participando") 

        elif pre + "reiniciar" in args[0]:
            await message.reply("Reiniciando el bot...")
            print(Fore.BLUE + f"[{getTiempesito()}] Reiniciando el bot...")
            await client.restart()

        elif pre + "actualizar" in args[0]:
            updateResult = buscarUpdate()
            if updateResult:
                await message.reply(f"Hay una actualización disponible ({updateResult[1]})")
            else:
                await message.reply(f"Tienes la última versión ({vlocal['major']}.{vlocal['minor']}.{vlocal['patch']})")

        elif pre + "aes" in args[0]:
            if config["depurar"]:
                try:
                    print(color.BLUE + requests.get("https://benbotfn.tk/api/v1/aes").text)
                except Exception as e:
                    await message.reply("Error: API caida o acceso denegado")
                    pError(f"API caida o acceso denegado ({e})")
                    return
            await message.reply("Comprueba la consola")

        elif "Playlist_" in args[0]:
            if config["depurar"]:
                try:
                    if len(args) == 1:
                        await client.party.set_playlist(playlist=args[0])
                    elif len(args) == 3:
                        await client.party.set_playlist(playlist=args[0], tournament=args[1], event_window=args[2])
                except:
                    await message.reply(f"No lider")
                    return

        elif pre + "privacidad" in args[0].lower():
            if len(args) != 2:
                await message.reply(f"Sintaxis del comando incorrecta")
                return
            else:
                if client.party.me.leader == True:
                    if args[1].lower() == "publico":
                        await client.party.me.set_privacy(fortnitepy.PartyPrivacy.PUBLIC)
                    elif args[1].lower() == "privado":
                        await client.party.me.party.set_privacy(fortnitepy.PartyPrivacy.PRIVATE)
                    elif args[1].lower() == "amigos":
                        await client.party.me.party.set_privacy(fortnitepy.PartyPrivacy.FRIENDS)
                    elif args[1].lower() == "amigosdeamigos":
                        await client.party.me.party.set_privacy(fortnitepy.PartyPrivacy.FRIENDS_ALLOW_FRIENDS_OF_FRIENDS)
                    else:
                        await message.reply(f"{args[1]} no es una privacidad de sala válida")
                        return
                    await message.reply(f"He cambiado la privacidad de esta sala a {args[1]}")
                else:
                    await message.reply("Necesito líder para cambiar la privacidad de la sala.")

        elif pre + "skin" in args[0].lower():
            if len(args) != 2:
                await message.reply(f"Sintaxis del comando incorrecta")
                return
            else:
                await client.party.me.set_outfit(asset=args[1])

        elif pre + "mochila" in args[0].lower():
            if len(args) != 2:
                await message.reply(f"Sintaxis del comando incorrecta")
                return
            else:
                await client.party.me.set_backpack(asset=args[1])

        elif pre + "emote" in args[0].lower():
            if len(args) == 1:
                await client.party.me.clear_emote()
                await message.reply("Emote despejado")
                print(Fore.GREEN + f"[{getTiempesito()}] Se ha despejado el emote que estaba haciendo el bot") 
                return
            elif len(args) == 2:
                await client.party.me.set_emote(asset=args[1])
                await message.reply(f"Reproduciendo {args[1]}")
                print(Fore.GREEN + f"[{getTiempesito()}] Reproduciendo {args[1]}") 
            elif len(args) == 3:
                emote_dur_num = es_numero(args[2], True)
                if emote_dur_num:
                    await client.party.me.set_emote(asset=args[1], run_for=emote_dur_num[1])
                    await message.reply(f"Reproduciendo {args[1]} durante {args[2]} segundos")
                    print(Fore.GREEN + f"[{getTiempesito()}] Reproduciendo {args[1]} durante {args[2]} segundos") 
                else:
                    await message.reply(f"Uso: {config['prefijo']}emote <EID (opcional)> <segundos (opcional)>")
            else:
                await message.reply(f"Uso: {config['prefijo']}emote <EID (opcional)> <segundos (opcional)>")

        elif pre + "recargar" in args[0].lower():
            try:
                cargarAjustes()
                await message.reply("Ajustes recargados exitosamente")
            except Exception as e:
                await message.reply("Ha ocurrido un error al recargar los ajustes :(")
                pError(f"Ha ocurrido un error al recargar los ajustes :( ({e})")
                

        elif pre + "españa" in args[0].lower():
            await message.reply("¡Viva españa!")
            print(Fore.RED + "██████████████████████")
            print(Fore.YELLOW + "██████████████████████")
            print(Fore.RED + "██████████████████████")
            

        elif pre + "gay" in args[0].lower():
            await message.reply("Yo tambíen soy gay :)")
            print(Fore.RED + "██████████████████████")
            print(Fore.YELLOW + "██████████████████████")
            print(color.YELLOW + "██████████████████████")
            print(Fore.GREEN + "██████████████████████")
            print(Fore.BLUE + "██████████████████████")
            print(color.PURPLE + "██████████████████████")
            

        elif pre + "apagar" in args[0].lower() and config["activar_apagar"]:
            await message.reply("Apagando...")
            print(Fore.GREEN + f"[{getTiempesito()}] Apagando el bot...") 
            await client.close(close_http= True)

        elif pre + "ayuda" in args[0].lower():
            await message.reply("Para obtener ayuda visita el apartado llamado 'Wiki' en el repositorio de GitHub")
            await message.reply("https://github.com/Londiuh/MDJ-bot")

        elif pre + "abandonar" in args[0].lower():
            if config["emote_abandonar"]:
                await client.party.me.set_emote(config["emote_abandonar_id"])
                time.sleep(1.5)
            await client.party.send(config["msg_abandonar"])
            await client.party.me.leave()
            print(Fore.GREEN + f"[{getTiempesito()}] El bot ha abandonado la sala")    

        elif pre + "expulsar" in args[0].lower():
            user = await client.fetch_profile(joinedArguments)
            member = client.party.members.get(user.id)
            if member is None:
                await message.reply("No hay ningún usuario en la sala llamado" + args[1])
            else:
                try:
                    await member.kick()
                    await message.reply(f"He expulsado a {member.display_name}.")
                    print(Fore.GREEN + f"[{getTiempesito()}] Se ha expulsado a {member.display_name} porque {message.author.display_name} lo ha pedido")
                except Exception as e:
                    pass
                    await message.reply(f"No puedo expulsar a {member.display_name}, no soy líder.")
                    print(Fore.BLACK + Back.RED + f"[{getTiempesito()}] [ERROR] Error al expulsar a " + args[1] + f"porque no tengo líder.")

        elif pre + "añadir" in args[0].lower():
            user = await client.fetch_profile(joinedArguments)
            friends = client.friends
            if user is None:
                await message.reply(f"No existe ningún jugador llamado {joinedArguments} en Fortnite.")
                print(Fore.BLACK + Back.RED + f"[{getTiempesito()}] [ERROR] No existe ningún jugador llamado {joinedArguments}")
            else:
                try:
                    if (user.id in friends):
                        await message.reply(f"Ya tengo agregado a {user.display_name}")
                        print(Fore.BLACK + Back.RED + f"[{getTiempesito()}] [ERROR] El bot ya tiene agregado a {user.display_name} ")
                    else: 
                        await client.add_friend(user.id)
                        await message.reply(f"Le he enviado una solicitud a {user.display_name}")
                        print(Fore.GREEN + f"[{getTiempesito()}] {client.user.display_name} le ha enviado una solicitud {user.display_name}")
                except Exception as e:
                    pass
                    print(Fore.BLACK + Back.RED + f"[{getTiempesito()}] [ERROR] Ha ocurrido un error al agregar a {joinedArguments}") 

        elif pre + "eliminar" in args[0].lower():
            user = await client.fetch_profile(joinedArguments)
            friends = client.friends
            if user is None:
                await message.reply(f"No tengo ningun amigo llamado {joinedArguments}.")
                print(Fore.BLACK + Back.RED + f"[{getTiempesito()}] [ERROR] No hay ningun amigo llamado {joinedArguments} en la lista de amigos del bot")
            else:
                try:
                    if (user.id in friends):
                        await client.remove_or_decline_friend(user.id)
                        await message.reply(f"He eliminado a {user.display_name} de la lista de amgios.")
                        print(Fore.GREEN + f"[{getTiempesito()}] {client.user.display_name} ha quitado a {user.display_name} como amigo.")
                    else: 
                        await message.reply(f"No tengo agregado a {user.display_name}.")
                        print(Fore.BLACK + Back.RED + f"[{getTiempesito()}] [ERROR] {client.user.display_name} a intentado eliminar a {user.display_name} de la lista de amigos del bot, pero ese usuario no esta agregado.")
                except Exception as e:
                    pass
                    print(Fore.BLACK + Back.RED + f"[{getTiempesito()}] [ERROR] Ha ocurrido un problema al eliminar {joinedArguments} de la lista de amigos del bot.") 

        elif pre + "amigos" in args[0].lower():
            friends = client.friends
            onlineFriends = []
            offlineFriends = []
            try:
                for f in friends:
                    friend = client.get_friend(f)
                    if friend.is_online():
                        onlineFriends.append(friend.display_name)
                    else:
                        offlineFriends.append(friend.display_name)
                print(f"[{getTiempesito()}] " + Fore.WHITE + "Lista de amigos: " + Fore.GREEN + f"{len(onlineFriends)} En línea " + Fore.WHITE + "/" + Fore.LIGHTBLACK_EX + f" {len(offlineFriends)} Desconectados " + Fore.WHITE + "/" + Fore.LIGHTWHITE_EX + f" {len(onlineFriends) + len(offlineFriends)} En total")
                for x in onlineFriends:
                    if x is not None:
                        print(Fore.GREEN + " " + x + Fore.WHITE)
                for x in offlineFriends:
                    if x is not None:
                        print(Fore.LIGHTBLACK_EX + " " + x + Fore.WHITE)
            except Exception as e:
                pass
            await message.reply("Comprueba la consola para ver la lista de amigos")       

        elif pre + "playlist-info" in args[0]:
            await message.reply(f"PlaylistName: {client.party.playlist_info[0]}")
            await message.reply(f"TournamentId: {client.party.playlist_info[1]}")
            await message.reply(f"EventWindowId: {client.party.playlist_info[2]}")
            await message.reply(f"RegionId: {client.party.playlist_info[3]}")
            print(color.BLUE + f"PlaylistName: {client.party.playlist_info[0]}")
            print(color.BLUE + f"TournamentId: {client.party.playlist_info[1]}")
            print(color.BLUE + f"EventWindowId: {client.party.playlist_info[2]}")
            print(color.BLUE + f"RegionId: {client.party.playlist_info[3]}")

        elif pre + "lider" in args[0].lower():
            if len(args) != 1:
                user = await client.fetch_profile(joinedArguments)
                member = client.party.members.get(user.id)
            if len(args) == 1:
                user = await client.fetch_profile(message.author.display_name)
                member = client.party.members.get(user.id)
            if member is None:
                await message.reply("Ese usuario no esta en la sala ¿Escribiste bien el nombre?")
            else:
                try:
                    await member.promote()
                    await message.reply(f"He hecho lider a {member.display_name}.")
                    print(Fore.BLUE + f"[{getTiempesito()}] Se ha hecho lider a {member.display_name} porque {message.author.display_name} lo ha pedido.")
                except Exception as e:
                    pass
                    await message.reply(f"No puedo darle lider a {member.display_name}, porque no tengo lider.")
                    print(Fore.BLACK + Back.YELLOW + f"[{getTiempesito()}] [ADVERTENCIA] No se le ha podido dar lider a {member.display_name} porque el bot no es lider.")          

        elif pre + "modo" in args[0].lower():
            m_patch = json.loads(requests.get("https://gist.githubusercontent.com/Londiuh/00458cc894dcbdbac2dddd30ad81e43d/raw/mdj-metodom.json").text)
            if vlocal["metodom"] in m_patch["metodom_patched"]:
                pAdvertencia(f"El método {vlocal['metodom']} ha sido parcheado, deberás esperar a que se encuentre un nuevo método y se actualice el bot")
                await message.reply(f"El método {vlocal['metodom']} ha sido parcheado.")

            if len(args) == 1:
                await message.reply(f"Sintaxis del comando incorrecta")
                return

            if "Playlist_" in args[1]:
                await client.party.me.set_ready(fortnitepy.ReadyState.NOT_READY)
                try:
                    await client.party.set_playlist(playlist="Playlist_PlaygroundV2")
                except:
                    await message.reply(f"¡No puedes usar este comando si no soy líder!")
                    return
                await message.reply(f"¿Que clave de emparejemiento quieres que ponga? Responde \"no\" si no quieres clave o ya has puesto una")
                user = await client.fetch_profile(message.author.display_name)
                member = client.party.members.get(user.id)
                res = await client.wait_for('friend_message')
                content = res.content.lower()
                if content != "no".lower():
                    await member.party.set_custom_key(content)
                    await message.reply(f"Clave puesta con exito.")
                await message.reply(f"Cambiando el modo de juego...")
                time.sleep(0.5)
                try:
                    await client.party.set_playlist(playlist=args[1], tournament="epicgames_Arena_S13_Trios", event_window="Arena_S13_Division1_Trios")
                    await client.party.me.leave()
                except:
                    pass
                    await message.reply(f"¡No puedo cambiar el modo si no soy líder!")
                    pAdvertencia("No se ha podido cambiar el modo porque el bot no es líder.")
            else:
                await message.reply(f"Sintaxis del comando incorrecta")  

try:
    subnormaldemierda = 'aWYgImNyZDEiIG5vdCBpbiBnbG9iYWxzKCk6DQogICAgcHJpbnQoRm9yZS5SRUQgKyBmIltFUlJPUl0gRXN0ZSBib3QgaGEgc2lkbyBwcm9ncmFtYWRvIHBvciBFbExvbmRpdWguIFkgdW4gc3Vibm9ybWFsIGhhIFFVSVRBRE8vQ0FNQklBRE8gbG9zIENSRURJVE9TIikNCiAgICBwcmludChGb3JlLllFTExPVyArIGYiW0FEVkVSVEVOQ0lBXSBTaSBoYXMgc2lkbyB0dSBxdWllbiBoYSBxdWl0YWRvIGxvcyBjcmVkaXRvcywgcG9yIGZhdm9yLCB2dWVsdmVsb3MgYSBwb25lciIpDQogICAgcHJpbnQoRm9yZS5SRUQgKyBmIltFUlJPUl0gTm8gcHVlZGVzIHF1aXRhcm1lIGxvcyBjcmVkaXRvcy9yb2Jhcm1lIGNvZGlnby4gTm8gdGllbmVzIHBlcm1pc28gcGFyYSBtb2RpZmljaWNhciBlbCBjb2RpZ28iKQ0KY2xpZW50LnJ1bigpDQphdXRoID0gVHJ1ZQ=='
    eval(compile(base64.b64decode(subnormaldemierda),'','exec'))
    if auth == False:
        pError("Error de autenticación desconocido")
except fortnitepy.AuthException as e:
    pError("Error de autenticación ¿Los datos proporcionados son correctos?")
