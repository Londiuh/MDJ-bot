class color: #Tabla de colores (aunque tambíen uso colorama)
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m' 
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

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
except ModuleNotFoundError:
    print(color.RED + f'[ERROR CRITICO] ¿Has instalado todas las librerías? Es que eres tontísimo".')
    exit()

auth = None
vlocal = "1.2.0" #No deberias cambiar esta variable
vactual = requests.get("https://raw.githubusercontent.com/Londiuh/MDJ-bot/master/version.txt")  

print(f'  ')
print(color.PURPLE + f'\t\t\t███╗░░░███╗██████╗░░░░░░██╗░░░░░░██████╗░░█████╗░████████╗')
print(color.PURPLE + f'\t\t\t████╗░████║██╔══██╗░░░░░██║░░░░░░██╔══██╗██╔══██╗╚══██╔══╝')
print(color.PURPLE + f'\t\t\t██╔████╔██║██║░░██║░░░░░██║█████╗██████╦╝██║░░██║░░░██║░░░')
print(color.PURPLE + f'\t\t\t██║╚██╔╝██║██║░░██║██╗░░██║╚════╝██╔══██╗██║░░██║░░░██║░░░')
print(color.PURPLE + f'\t\t\t██║░╚═╝░██║██████╔╝╚█████╔╝░░░░░░██████╦╝╚█████╔╝░░░██║░░░')
print(color.PURPLE + f'\t\t\t╚═╝░░░░░╚═╝╚═════╝░░╚════╝░░░░░░░╚═════╝░░╚════╝░░░░╚═╝░░░')
eval(compile(base64.b64decode('Y3JkMT1UcnVlDQpwcmludChjb2xvci5EQVJLQ1lBTitmIiBcdFx0XHRcdCIrYmFzZTY0LmI2NGRlY29kZSgiVlc1aElHTnZjMkVnYUdWamFHRWdjRzl5SUVWc1RHOXVaR2wxYUE9PSIuZW5jb2RlKCdhc2NpaScpKS5kZWNvZGUoJ2FzY2lpJykp'),'','exec'))
print(f'  ') 

def getTiempesito():
    tiempesito = datetime.datetime.now().strftime('%H:%M:%S')
    return tiempesito
print(color.DARKCYAN + f"Versión: {vlocal}")
time.sleep(0.5)
print(Fore.MAGENTA + f"[{getTiempesito()}] Buscando actualizaciones...")
time.sleep(0.5)
vactualfix = vactual.text[:-1] #Muy cutre, lo se, yo soy cutre
if vactualfix != vlocal:
    print(Fore.BLACK + Back.YELLOW + f"[{getTiempesito()}] [ADVERTENCIA] Nueva versión disponible: {vactualfix}")
    print(Fore.GREEN + f"[¿?] ¿Deseas ver la lista de cambios? " + color.CYAN + "Si | No")
    vresp = input()
    if vresp.lower() == "si":
        webbrowser.open("https://github.com/Londiuh/MDJ-bot/blob/master/cambios.md")
        exit()
else:
    print(color.YELLOW + f"¡Tienes la última versión!")

def cargarAjustes():
    try:
        with open('ajustes.json') as f:
            print(color.YELLOW + f'[{getTiempesito()}] Cargando \'ajustes.json\'...')
            time.sleep(5)
            global data
            data = json.load(f)
            print(color.GREEN + f'[{getTiempesito()}] ¡Ajustes cargados con éxito!')
    except:
        print(Fore.BLACK + Back.RED + f"[ERROR] No se ha encontrado 'ajustes.json' en el directorio. ¿Que coño has hecho?")
        exit()
cargarAjustes()

if data['depurar']:
    print(color.YELLOW + f'[{getTiempesito()}] La depuración esta activada.')
    logger = logging.getLogger('fortnitepy.xmpp')
    logger.setLevel(level=logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

time.sleep(0.1)  
print(color.BLUE + f'\n---------------------------------------------------------------------')
listo = False

def get_detalles_autentificacion():
    if os.path.isfile('device_auths.json'):
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

device_auth_details = get_detalles_autentificacion().get(data['correo'], {})
if data['sala_privacidad'].lower() == "publico":
    privasidad = fortnitepy.PartyPrivacy.PUBLIC
elif data['sala_privacidad'].lower() == "privado":
    privasidad = fortnitepy.PartyPrivacy.PRIVATE
elif data['sala_privacidad'].lower() == "amigos":
    privasidad = fortnitepy.PartyPrivacy.FRIENDS
elif data['sala_privacidad'].lower() == "amigosdeamigos":
    privasidad = fortnitepy.PartyPrivacy.FRIENDS_ALLOW_FRIENDS_OF_FRIENDS
else:
    privasidad = fortnitepy.PartyPrivacy.PUBLIC
    print(Fore.BLACK + Back.YELLOW + f"[{getTiempesito()}] [ADVERTENCIA] {data['sala_privacidad']} no es una privacidad de sala válida.")
    print(Fore.BLACK + Back.YELLOW + f"[{getTiempesito()}] [ADVERTENCIA] Se ha puesto la privacidad en PÚBLICO")
if data['plataforma'].lower() in ["win", "windows"]:
    plataforma = fortnitepy.Platform.WINDOWS
elif data['plataforma'].lower() in ["mac", "macintosh"]:
    plataforma = fortnitepy.Platform.MAC
elif data['plataforma'].lower() in ["psn", "playstation"]:
    plataforma = fortnitepy.Platform.PLAYSTATION
elif data['plataforma'].lower() in ["xb", "xbox"]:
    plataforma = fortnitepy.Platform.XBOX
elif data['plataforma'].lower() in ["ns", "switch"]:
    plataforma = fortnitepy.Platform.SWITCH
elif data['plataforma'].lower() == "ios":
    plataforma = fortnitepy.Platform.IOS
elif data['plataforma'].lower() in ["and", "android"]:
    plataforma = fortnitepy.Platform.ANDROID
else:
    plataforma = fortnitepy.Platform.SWITCH
    print(Fore.BLACK + Back.YELLOW + f"[{getTiempesito()}] [ADVERTENCIA] {data['plataforma']} no es una plataforma válida.")
    print(Fore.BLACK + Back.YELLOW + f"[{getTiempesito()}] [ADVERTENCIA] Se ha puesto la plataforma en SWITCH")
print(plataforma)
client = fortnitepy.Client(
    auth=fortnitepy.AdvancedAuth(
        email=data['correo'],
        password=data['contrasena'],
        prompt_exchange_code=True,
        delete_existing_device_auths=True,
        **device_auth_details
    ),
    status=data['estado'],
    platform=plataforma,
    default_party_config={'privacy': privasidad},
    default_party_member_config=[
        functools.partial(fortnitepy.ClientPartyMember.set_outfit, asset=data['skin_id']),
        functools.partial(fortnitepy.ClientPartyMember.set_backpack, data['mochila_id']),
        functools.partial(fortnitepy.ClientPartyMember.set_banner, icon=data['escudo'], color=data['escudo_color'], season_level=data['nivel_pase']),
    ]
)

@client.event
async def event_device_auth_generate(details: dict, email: str) -> None:
    store_detalles_autentificacion(email, details)


@client.event
async def event_ready():
    print(color.BLUE + f'[{getTiempesito()}] ¡El bot se incició exitosamente!')
    print(color.BLUE + f'\n---------------------------------------------------------------------') 

@client.event
async def event_party_invite(invite):
    if data['unirseinvitaciones']:
        try:
            await invite.accept()
            print(Fore.BLUE + f'[{getTiempesito()}] Se ha aceptado una invitación de sala de {invite.sender.display_name}')
        except Exception as e:
            pass
    else:
        if invite.sender.display_name in data['Admins']:
            await invite.accept()
            print(Fore.BLUE + f'[{getTiempesito()}] Se ha aceptado una invitación de sala de {invite.sender.display_name}')
        else:
            print(Fore.BLACK + Back.YELLOW + f'[{getTiempesito()}] Se ha rechazado una invitación de sala de {invite.sender.display_name} (Motivo: unirseinvitaciones esta desactivado y no es admin)')
            await invite.sender.send(f"Este bot no puede aceptar tu invitación de partida ahora mismo porque no eres admin.")
            await invite.sender.send(f"Si conoces a la persona que esta controlando a este bot puedes pedirle que active la habilidad de aceptar invitaciones o te haga admin.")
            await invite.sender.send(base64.b64decode("VGFtYmnDqW4gcHVlZGVzIGNvbnNlZ3VpciB0dSBwcm9waW8gYm90IGVuOiBodHRwczovL2dpdGh1Yi5jb20vTG9uZGl1aC9NREotYm90".encode('ascii')).decode('ascii'))

@client.event
async def event_friend_request(request):
    if data['aceptaramigos']:
        await request.accept()
        print(Fore.BLUE + f"[{getTiempesito()}] Se ha aceptado la petición de amistad de {request.display_name}")
    else:
        if request.display_name in data['Admins']:
            await request.accept()
            print(Fore.BLUE + f"[{getTiempesito()}] Se ha aceptado la petición de amistad de {request.display_name}")  
        else:
            print(Fore.BLACK + Back.YELLOW + f"[{getTiempesito()}] Se ha rechazado la petición de amistad de {request.display_name} (Motivo: aceptaramigos esta desactivado y no es admin)")

@client.event
async def event_party_member_join(member):
    eval(compile(base64.b64decode('Z2xvYmFsIGNyZDINCmNyZDIgPSBUcnVl'),'','exec'))
    await client.user.party.send(base64.b64decode("RXN0ZSBib3QgaGEgc2lkbyBjcmVhZG8gcG9yIEVsTG9uZGl1aC4gUHVlZGVzIGVjb250cmFybG8gZW4gZWwgcmVwb3NpdGlvcmlvIG9maWNpYWw6IGh0dHBzOi8vZ2l0aHViLmNvbS9Mb25kaXVoL01ESi1ib3Q=".encode('ascii')).decode('ascii'))
    eval(compile(base64.b64decode('aWYiY3JkMiJub3QgaW4gZ2xvYmFscygpOmV4aXQoKQ=='),'','exec'))
    if client.user.display_name != member.display_name:
        print(Fore.BLUE + f"[{getTiempesito()}] {member.display_name} se ha unido a la sala.")
    time.sleep(1)
    await client.user.party.me.set_emote(asset=data['emote_id'])

@client.event
async def event_friend_message(message):
    eval(compile(base64.b64decode('aWYiY3JkMiJub3QgaW4gZ2xvYmFscygpOmV4aXQoKQ=='),'','exec'))
    args = message.content.split()
    split = args[1:]
    joinedArguments = " ".join(split)
    print('[' + getTiempesito() + '] {0.author.display_name}: {0.content}'.format(message))
    pre = data['prefijo'] #Para acortar
    
    if pre + "privacidad" in args[0].lower():
        if message.author.display_name in data['Admins']:
            if len(args) != 2:
                await message.reply(f"Sintaxis del comando incorrecta")
                return
            else:
                if client.user.party.me.leader == True:
                    if args[1].lower() == "publico":
                        await client.user.party.set_privacy(fortnitepy.PartyPrivacy.PUBLIC)
                    elif args[1].lower() == "privado":
                        await client.user.party.set_privacy(fortnitepy.PartyPrivacy.PRIVATE)
                    elif args[1].lower() == "amigos":
                        await client.user.party.set_privacy(fortnitepy.PartyPrivacy.FRIENDS)
                    elif args[1].lower() == "amigosdeamigos":
                        await client.user.party.set_privacy(fortnitepy.PartyPrivacy.FRIENDS_ALLOW_FRIENDS_OF_FRIENDS)
                    else:
                        await message.reply("{args[1]} no es una privacidad de sala válida")
                        return
                    await message.reply("He cambiado la privacidad de esta sala a {args[1]}")
                else:
                    await message.reply("Necesito líder para cambiar la privacidad de la sala.")
        else:
            await message.reply('¡No tienes acceso a este comando!')

    if pre + "skin" in args[0].lower():
        if message.author.display_name in data['Admins']:
            if len(args) != 2:
                await message.reply(f"Sintaxis del comando incorrecta")
                return
            else:
                await client.user.party.me.set_outfit(asset=args[1])
        else:
            await message.reply('¡No tienes acceso a este comando!')

    if pre + "mochila" in args[0].lower():
        if message.author.display_name in data['Admins']:
            if len(args) != 2:
                await message.reply(f"Sintaxis del comando incorrecta")
                return
            else:
                await client.user.party.me.set_backpack(asset=args[1])
        else:
            await message.reply('¡No tienes acceso a este comando!')

    if pre + "emote" in args[0].lower():
        if message.author.display_name in data['Admins']:
            if len(args) != 2:
                await message.reply(f"Sintaxis del comando incorrecta")
                return
            else:
                await client.user.party.me.set_emote(asset=args[1])
        else:
            await message.reply('¡No tienes acceso a este comando!')

    if pre + "recargar" in args[0].lower():
        if message.author.display_name in data['Admins']:
            try:
                cargarAjustes()
                await message.reply("Ajustes recargados exitosamente")
            except:
                await message.reply("Ha ocurrido un error al recargar los ajustes :(")
                print(Fore.BLACK + Back.RED + f"[{getTiempesito()}] [ERROR] Ha ocurrido un error al recargar los ajustes :(")
        else:
            await message.reply('¡No tienes acceso a este comando!')
            

    if pre + "españa" in args[0].lower():
        await message.reply("¡Viva españa!")
        print(Fore.RED + "██████████████████████")
        print(Fore.YELLOW + "██████████████████████")
        print(Fore.RED + "██████████████████████")
        

    if pre + "gay" in args[0].lower():
        await message.reply("Yo tambíen soy gay :)")
        print(Fore.RED + "██████████████████████")
        print(Fore.YELLOW + "██████████████████████")
        print(color.YELLOW + "██████████████████████")
        print(Fore.GREEN + "██████████████████████")
        print(Fore.BLUE + "██████████████████████")
        print(color.PURPLE + "██████████████████████")
        

    if pre + "apagar" in args[0].lower():
        if message.author.display_name in data['Admins']:
            await message.reply("¡Bot apagado!")
            exit()
        else:
            await message.reply('¡No tienes acceso a este comando!')
            

    if pre + "ayuda" in args[0].lower():
        if message.author.display_name in data['Admins']:
            await message.reply("Para obtener ayuda visita el apartado llamado \"Wiki\" en el repositorio de GitHub")
            await message.reply("https://github.com/Londiuh/MDJ-bot")
              

    if pre + "abandonar" in args[0].lower():
        if message.author.display_name in data['Admins']:
            await client.user.party.me.set_emote('EID_Snap')
            time.sleep(2)
            await message.reply('¡Me piro vampiro!')
            await client.user.party.me.leave()
            print(Fore.GREEN + f'[{getTiempesito()}] El bot ha abandonado la sala porque {message.author.display_name} lo ha pedido')
        else:
            if message.author.display_name not in data['Admins']:
                await message.reply(f"¡No tienes acceso a este comando!")
                

    if pre + "expulsar" in args[0].lower() and message.author.display_name in data['Admins']:
        user = await client.fetch_profile(joinedArguments)
        member = client.user.party.members.get(user.id)
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
        if message.author.display_name not in data['Admins']:
            await message.reply(f"¡No tienes acceso a este comando!")
            

    if pre + "añadir" in args[0].lower() and message.author.display_name in data['Admins']:
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
        if message.author.display_name not in data['Admins']:
            await message.reply(f"¡No tienes acceso a este comando!")
            

    if pre + "eliminar" in args[0].lower() and message.author.display_name in data['Admins']:
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
        if message.author.display_name not in data['Admins']:
            await message.reply(f"¡No tienes acceso a este comando!")
            

    if pre + "amigos" in args[0].lower() and message.author.display_name in data['Admins']:
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
        if message.author.display_name not in data['Admins']:
            await message.reply(f"¡No tienes acceso a este comando!")
            

    if pre + "playlist-info" in args[0]:
        await message.reply("PlaylistName: " + (client.user.party.playlist_info[0]))
        if message.author.display_name in data['Admins']:
            await message.reply("Tienes más información sobre la playlist en la consola :)")
            print(color.CYAN + f"<-------------[Playlist-Información]------------->")
            print(color.BLUE + f"PlaylistName: " + (client.user.party.playlist_info[0]))
            print(color.BLUE + f"TournamentId: " + (client.user.party.playlist_info[1]))
            print(color.BLUE + f"EventWindowId: " + (client.user.party.playlist_info[2]))
            print(color.BLUE + f"RegionId: " + (client.user.party.playlist_info[3]))
            print(color.CYAN + f"<-------------[Playlist-Información]------------->")
        

    if pre + "lider" in args[0].lower() and message.author.display_name in data['Admins']:
        if len(args) != 1:
            user = await client.fetch_profile(joinedArguments)
            member = client.user.party.members.get(user.id)
        if len(args) == 1:
            user = await client.fetch_profile(message.author.display_name)
            member = client.user.party.members.get(user.id)
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
        if message.author.display_name not in data['Admins']:
            await message.reply(f"¡No tienes acceso a este comando!")
            

    if pre + "modo" in args[0].lower():
        if message.author.display_name in data['Admins']:
            if len(args) == 1:
                await message.reply(f"Sintaxis del comando incorrecta")
                return

            if "Playlist_" in args[1]:
                await client.user.party.me.set_ready(fortnitepy.ReadyState.NOT_READY)
                try:
                    await client.user.party.set_playlist(playlist="Playlist_PlaygroundV2")
                except:
                    await message.reply(f"¡No puedes usar este comando si no soy líder!")
                    return
                user = await client.fetch_profile(message.author.display_name)
                member = client.user.party.members.get(user.id)
                if member.is_ready():
                    await message.reply(f"¿Estan todos los demás jugadores de la sala en listo? Si o no")
                    res = await client.wait_for('friend_message')
                    content = res.content.lower()
                    if content == "si".lower():
                        await message.reply(f"¿Que clave de emparejemiento quieres que ponga? Responde \"no\" si no quieres clave o ya has puesto una")
                        res = await client.wait_for('friend_message')
                        content = res.content.lower()
                        if content != "no".lower():
                            await member.party.set_custom_key(content)
                            await message.reply(f"Clave puesta con exito.")
                        time.sleep(3)
                        await message.reply(f"Cambiando el modo de juego...")
                        time.sleep(3)
                        try:
                            await client.user.party.set_playlist(playlist=args[1])
                            time.sleep(1.3)
                            await client.user.party.me.set_ready(fortnitepy.ReadyState.SITTING_OUT)
                            time.sleep(7)
                            await message.reply(f"Si se ha quedado 'Esperando emparejamiento' usa \"{pre}modo reintentar\"")
                        except Exception as e:
                            pass
                            await message.reply(f"¡No puedo cambiar el modo si no soy líder!")
                            print(Fore.BLACK + Back.YELLOW + f"[{getTiempesito()}] [ADVERTENCIA] No se ha podido cambiar el modo porque el bot no es líder.")
                    else:
                        await message.reply(f"¡Todos los jugadores deben estar en listo!")
                else:
                    await message.reply(f"¡Todos los jugadores deben estar en listo!")
            elif "reintentar" in args[1]:
                await message.reply("Reintentando...")
                await client.user.party.me.set_ready(fortnitepy.ReadyState.NOT_READY)
                time.sleep(0.5)
                await client.user.party.me.set_ready(fortnitepy.ReadyState.SITTING_OUT)

            elif "gilipollas" in args[1].lower():
                await message.reply(f"Activando modo gilipollas...")
                time.sleep(1)
                await message.reply(f"Error al activar el modo gilipollas. Comprueba la consola para ver el error")
                print(Fore.BLACK + Back.RED + f'             ,----------------,              ,---------,')
                print(Fore.BLACK + Back.RED + f'        ,-----------------------,          ,"        ,"|')
                print(Fore.BLACK + Back.RED + f'      ,"                      ,"|        ,"        ,"  |')
                print(Fore.BLACK + Back.RED + f'     +-----------------------+  |      ,"        ,"    |')
                print(Fore.BLACK + Back.RED + f'     |  .-----------------.  |  |     +---------+      |')
                print(Fore.BLACK + Back.RED + f'     |  |                 |  |  |     | -==----\'|      |')
                print(Fore.BLACK + Back.RED + f'     |  |\'gilipollas.py\'  |  |  |     |         |      |')
                print(Fore.BLACK + Back.RED + f'     |  |   not found     |  |  |/----|`---=    |      |')
                print(Fore.BLACK + Back.RED + f'     |  |  C:\\>_          |  |  |   ,/|==== ooo |      ;')
                print(Fore.BLACK + Back.RED + f'     |  |                 |  |  |  // |(((( [33]|    ,"')
                print(Fore.BLACK + Back.RED + f'     |  `-----------------\'  |," .;\'| |((((     |  ,"')
                print(Fore.BLACK + Back.RED + f'     +-----------------------+  ;;  | |         |,"  ')
                print(Fore.BLACK + Back.RED + f'        /_)______________(_/  //\'   | +---------+')
                print(Fore.BLACK + Back.RED + f'   ___________________________/___  `,')
                print(Fore.BLACK + Back.RED + f'  /  oooooooooooooooo  .o.  oooo /,   \\,"-----------')
                print(Fore.BLACK + Back.RED + ' / ==ooooooooooooooo==.o.  ooo= //   ,`\\--{}B     ,"')
                print(Fore.BLACK + Back.RED + f'/_==__==========__==_ooo__ooo=_/\'   /___________,"')
                print(Fore.BLACK + Back.RED + f'`-----------------------------\'')
            else:
                await message.reply(f"Sintaxis del comando incorrecta")
        else:
            await message.reply(f"¡No tienes acceso a este comando!")
            

try:
    subnormaldemierda = 'aWYgImNyZDEiIG5vdCBpbiBnbG9iYWxzKCk6DQogICAgcHJpbnQoRm9yZS5SRUQgKyBmIltFUlJPUl0gRXN0ZSBib3QgaGEgc2lkbyBwcm9ncmFtYWRvIHBvciBFbExvbmRpdWguIFkgdW4gc3Vibm9ybWFsIGhhIFFVSVRBRE8vQ0FNQklBRE8gbG9zIENSRURJVE9TIikNCiAgICBwcmludChGb3JlLllFTExPVyArIGYiW0FEVkVSVEVOQ0lBXSBTaSBoYXMgc2lkbyB0dSBxdWllbiBoYSBxdWl0YWRvIGxvcyBjcmVkaXRvcywgcG9yIGZhdm9yLCB2dWVsdmVsb3MgYSBwb25lciIpDQogICAgcHJpbnQoRm9yZS5SRUQgKyBmIltFUlJPUl0gTm8gcHVlZGVzIHF1aXRhcm1lIGxvcyBjcmVkaXRvcy9yb2Jhcm1lIGNvZGlnby4gTm8gdGllbmVzIHBlcm1pc28gcGFyYSBtb2RpZmljaWNhciBlbCBjb2RpZ28iKQ0KY2xpZW50LnJ1bigpDQphdXRoID0gVHJ1ZQ=='
    eval(compile(base64.b64decode(subnormaldemierda),'','exec'))
    if auth == False:
        print(Fore.BLACK + Back.RED + f"[{getTiempesito()}] [ERROR] Error de autenticación desconocido. Si este error sigue ocurriendo reportalo")
except fortnitepy.AuthException as e:
    print(Fore.BLACK + Back.RED + f"[{getTiempesito()}] [ERROR] Error de autenticación ¿Pusiste el correo y la contraseña bien? ¿Pusiste el exchange code bien?")
#Si robas codigo estas cometiendo un acto ilegal. El codigo esta visible para que aprendas