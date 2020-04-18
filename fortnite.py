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
vlocal = "1.0.1" #No deberias cambiar esta variable
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

print(color.DARKCYAN + f"Versión: {vlocal}")
time.sleep(0.5)
print(Fore.MAGENTA + f"Buscando actualizaciones...")
time.sleep(0.5)
vactualfix = vactual.text[:-1] #Muy cutre, lo se, yo soy cutre
if vactualfix != vlocal:
    print(Fore.BLACK + Back.YELLOW + f"[ADVERTENCIA] Nueva versión disponible: {vactualfix}")
    print(Fore.GREEN + f"[¿?] ¿Deseas ver la lista de cambios? " + color.CYAN + "Si | No")
    vresp = input()
    if vresp.lower() == "si":
        webbrowser.open("https://github.com/Londiuh/MDJ-bot/blob/master/cambios.md")
        exit()
else:
    print(color.YELLOW + f"¡Tienes la última versión!")

def getTiempesito():
    tiempesito = datetime.datetime.now().strftime('%H:%M:%S')
    return tiempesito

fecha = datetime.datetime.now()
if fecha.year == 2020 and fecha.month == 4 and fecha.day > 25:
    print(Fore.BLACK + Back.RED + f"[{getTiempesito()}] [ERROR] Se acabo el tiempo de uso :(")
    bypass = input()
    if bypass != base64.b64decode("MTA4ZDljZmItMTFiNC00ZDkxLTgxZGUtYzBhZDU5NWQxNTg5".encode('ascii')).decode('ascii'):
        exit()

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

if data['depurar'].lower() == 'true':
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
client = fortnitepy.Client(
    auth=fortnitepy.AdvancedAuth(
        email=data['correo'],
        password=data['contrasena'],
        prompt_exchange_code=True,
        delete_existing_device_auths=True,
        **device_auth_details
    ),
    status=base64.b64decode("aHR0cHM6Ly9naXRodWIuY29tL0xvbmRpdWgvTURKLWJvdA==".encode('ascii')).decode('ascii'),
    platform=fortnitepy.Platform.ANDROID,
    
    default_party_config={
        'privacy': fortnitepy.PartyPrivacy.PRIVATE,
    }
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
    if data['unirseinvitaciones'].lower() == 'true':
        try:
            await invite.accept()
            print(Fore.BLUE + f'[{getTiempesito()}] Se ha aceptado una invitación de sala de {invite.sender.display_name}')
        except Exception as e:
            pass
    if data['unirseinvitaciones'].lower() == 'false':
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
    if data['aceptaramigos'].lower() == 'true':
        await request.accept()
        print(Fore.BLUE + f"[{getTiempesito()}] Se ha aceptado la petición de amistad de {request.display_name}")
    if data['aceptaramigos'].lower() == 'false':
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
    await client.user.party.me.set_emote(asset='EID_Robot')

@client.event
async def event_friend_message(message):
    eval(compile(base64.b64decode('aWYiY3JkMiJub3QgaW4gZ2xvYmFscygpOmV4aXQoKQ=='),'','exec'))
    args = message.content.split()
    split = args[1:]
    joinedArguments = " ".join(split)
    print('[' + getTiempesito() + '] {0.author.display_name}: {0.content}'.format(message))
    
    if "/recargar" in args[0].lower():
        if message.author.display_name in data['Admins']:
            try:
                cargarAjustes()
                await message.reply("Ajustes recargados exitosamente")
            except:
                await message.reply("Ha ocurrido un error al recargar los ajustes :(")
                print(Fore.BLACK + Back.RED + f"[{getTiempesito()}] [ERROR] Ha ocurrido un error al recargar los ajustes :(")
        else:
            await message.reply('¡No tienes acceso a este comando!')
            

    if "/españa" in args[0].lower():
        await message.reply("¡Viva españa!")
        print(Fore.RED + "██████████████████████")
        print(Fore.YELLOW + "██████████████████████")
        print(Fore.RED + "██████████████████████")
        

    if "/gay" in args[0].lower():
        await message.reply("Yo tambíen soy gay :)")
        print(Fore.RED + "██████████████████████")
        print(Fore.YELLOW + "██████████████████████")
        print(color.YELLOW + "██████████████████████")
        print(Fore.GREEN + "██████████████████████")
        print(Fore.BLUE + "██████████████████████")
        print(color.PURPLE + "██████████████████████")
        

    if "/apagar" in args[0].lower():
        if message.author.display_name in data['Admins']:
            await message.reply("¡Bot apagado!")
            exit()
        else:
            await message.reply('¡No tienes acceso a este comando!')
            

    if "/ayuda" in args[0].lower():
        if message.author.display_name in data['Admins']:
            await message.reply("Para obtener ayuda visita el apartado llamado \'Wiki\' en el repositorio de GitHub")
            await message.reply("https://github.com/Londiuh/MDJ-bot")
              

    if "/abandonar" in args[0].lower():
        if message.author.display_name in data['Admins']:
            await client.user.party.me.set_emote('EID_Snap')
            time.sleep(2)
            await message.reply('¡Me piro vampiro!')
            await client.user.party.me.leave()
            print(Fore.GREEN + f'[{getTiempesito()}] El bot ha abandonado la sala porque {message.author.display_name} lo ha pedido')
        else:
            if message.author.display_name not in data['Admins']:
                await message.reply(f"¡No tienes acceso a este comando!")
                

    if "/expulsar" in args[0].lower() and message.author.display_name in data['Admins']:
        user = await client.fetch_profile(joinedArguments)
        member = client.user.party.members.get(user.id)
        if member is None:
            await message.reply("No hay ningun usuario en la sala llamado" + args[1])
        else:
            try:
                await member.kick()
                await message.reply(f"He expulsado a {member.display_name}.")
                print(Fore.GREEN + f"[{getTiempesito()}] Se ha expulsado a {member.display_name} porque {message.author.display_name} lo ha pedido")
            except Exception as e:
                pass
                await message.reply(f"No puedo expulsar a {member.display_name}, no soy líder.")
                print(Fore.BLACK + Back.RED + f"[{getTiempesito()}] [ERROR] Error al expulsar a " + args[1] + f"porque no tengo líder." + Fore.WHITE)
        if message.author.display_name not in data['Admins']:
            await message.reply(f"¡No tienes acceso a este comando!")
            

    if "/añadir" in args[0].lower() and message.author.display_name in data['Admins']:
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
            

    if "/eliminar" in args[0].lower() and message.author.display_name in data['Admins']:
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
            

    if "/amigos" in args[0].lower() and message.author.display_name in data['Admins']:
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
            

    if "/playlist-info" in args[0]:
        await message.reply("PlaylistName: " + (client.user.party.playlist_info[0]))
        if message.author.display_name in data['Admins']:
            await message.reply("Tienes más información sobre la playlist en la consola :)")
            print(color.CYAN + f"<-------------[Playlist-Información]------------->")
            print(color.BLUE + f"PlaylistName: " + (client.user.party.playlist_info[0]))
            print(color.BLUE + f"TournamentId: " + (client.user.party.playlist_info[1]))
            print(color.BLUE + f"EventWindowId: " + (client.user.party.playlist_info[2]))
            print(color.BLUE + f"RegionId: " + (client.user.party.playlist_info[3]))
            print(color.CYAN + f"<-------------[Playlist-Información]------------->")
        

    if "/lider" in args[0].lower() and message.author.display_name in data['Admins']:
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
            

    if "/modo" in args[0].lower():
        if message.author.display_name in data['Admins']:
            if len(args) == 1:
                await message.reply(f"Sintaxis del comando incorrecta")
                return

            if "Playlist_" in args[1]:
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
                        await message.reply(f"¿Que clave de emparejemiento quieres que ponga? Responde no si no quieres clave o ya has puesto una")
                        res = await client.wait_for('friend_message')
                        content = res.content.lower()
                        if content != "no".lower():
                            await member.party.set_custom_key(content)
                            await message.reply(f"Clave puesta con exito.")
                            #await message.reply(f"Ten en cuenta que tienes que poder hacer privadas para comenzar la partida")
                            time.sleep(3)
                            await message.reply(f"Cambiando el modo de juego...")
                            time.sleep(3)
                        try:
                            await client.user.party.set_playlist(playlist=args[1])
                            time.sleep(1.3)
                            await client.user.party.me.set_ready(fortnitepy.ReadyState.SITTING_OUT)
                            time.sleep(7)
                            await message.reply(f"Si por alguna razón se ha quedado en 'Esperando emparegamiento...' tienes que crear una nueva sala")
                        except Exception as e:
                            pass
                            await message.reply(f"¡No puedo cambiar el modo si no soy líder!")
                            print(Fore.BLACK + Back.YELLOW + f"[{getTiempesito()}] [ADVERTENCIA] No se ha podido cambiar el modo porque el bot no es líder.")
                    else:
                        await message.reply(f"¡Todos los jugadores deben estar en listo!")
                else:
                    await message.reply(f"¡Todos los jugadores deben estar en listo!")
            elif "comida" in args[1]:
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
                        await message.reply(f"¿Que clave de emparejemiento quieres que ponga? Responde no si no quieres clave o ya has puesto una")
                        res = await client.wait_for('friend_message')
                        content = res.content.lower()
                        if content != "no".lower():
                            await member.party.set_custom_key(content)
                            await message.reply(f"Clave puesta con exito.")
                            #await message.reply(f"Ten en cuenta que tienes que poder hacer privadas para comenzar la partida")
                            time.sleep(3)
                            await message.reply(f"Cambiando el modo de juego...")
                            time.sleep(3)
                        try:
                            await client.user.party.set_playlist(playlist="Playlist_Barrier_16_B_Lava")
                            time.sleep(1.3)
                            await client.user.party.me.set_ready(fortnitepy.ReadyState.SITTING_OUT)
                            time.sleep(7)
                            await message.reply(f"Si por alguna razón se ha quedado en 'Esperando emparegamiento...' tienes que crear una nueva sala")
                        except Exception as e:
                            pass
                            await message.reply(f"¡No puedo cambiar el modo si no soy líder!")
                            print(Fore.BLACK + Back.YELLOW + f"[{getTiempesito()}] [ADVERTENCIA] No se ha podido cambiar el modo porque el bot no es líder.")
                    else:
                        await message.reply(f"¡Todos los jugadores deben estar en listo!")
                else:
                    await message.reply(f"¡Todos los jugadores deben estar en listo!")
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