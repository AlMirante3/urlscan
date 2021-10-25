import requests
import os
from colorama import Fore
import sys
from datetime import datetime
from bs4 import BeautifulSoup
## \\\\\\ TABELA DE CORES ////// ##
banner = """
 █    ██  ██▀███   ██▓         ██████  ▄████▄   ▄▄▄       ███▄    █ 
 ██  ▓██▒▓██ ▒ ██▒▓██▒       ▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █ 
▓██  ▒██░▓██ ░▄█ ▒▒██░       ░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒
▓▓█  ░██░▒██▀▀█▄  ▒██░         ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒
▒▒█████▓ ░██▓ ▒██▒░██████▒   ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░
░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░ ▒░▓  ░   ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
░░▒░ ░ ░   ░▒ ░ ▒░░ ░ ▒  ░   ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░
 ░░░ ░ ░   ░░   ░   ░ ░      ░  ░  ░  ░          ░   ▒      ░   ░ ░ 
   ░        ░         ░  ░         ░  ░ ░            ░  ░         ░ 
                                      ░                             
                           _______________________________________________________
   _______________________|py 3
  |script to linux  =X    |script by AlMirante
  |   "Hack the Planet"   |ADM Panel Find
  +-----------------------|No Windows Compatibility
                          |_______________________________________________________

"""
def help_window():
	os.system("clear")
	window = """
 Help:
+------------------------------------------------------------+
|	               URLSCAN.PY                            |
|____________________________________________________________|
|   			                                     |
|Using: python3 urlscan.py http://www.exemple.com            | 
|Author: AlMirante - ig @_pedro_mgf                          |
|e-mail: krawklzn@gmail.com                                  |
+------------------------------------------------------------+
	"""
	what = """
 Documentation:
 ------------------------------------------------------------
|Tested version of python: Python 3.7.5 - What is? ---       |
|This script tests, in a few minutes, initially, 293         |
|directories. This script works as a brute force on          |
|directories, with the purpose of cracking administrative    |
|pages on web servers.                                       |
|It is in version 1.0. In version 2.0 I will put a fast      |
|port scanner, in order to help with pentest web;            |
|____________________________________________________________|
	"""
	print(green + window, blue + what)

os.system("clear")
white = Fore.WHITE
red = Fore.RED
blue = Fore.BLUE
yellow = Fore.YELLOW
green = Fore.GREEN
hora =  yellow + "[" + datetime.now().strftime('%H:%M') + "]"
url = sys.argv[1]
	#########################################

word = ['admin.php', 'index.php', 'login.php', 'login.html', 'administrator', 'admin', 'adminpanel', 'cpanel', 'login', 'wp-login.php', 'administrator', 'admins', 'logins', 'admin.asp', 'login.asp', 'adm/', 'admin/', 'admin/account.html', 'admin/login.html', 'admin/login.htm', 'admin/controlpanel.html', 'admin/controlpanel.htm', 'admin/adminLogin.html', 'admin/adminLogin.htm', 'admin.htm', 'admin.html', 'adminitem/', 'adminitems/', 'administrator/', 'administrator/login.%EXT%', 'administrator.%EXT%', 'administration/', 'administration.%EXT%', 'adminLogin/', 'adminlogin.%EXT%', 'admin_area/admin.%EXT%', 'admin_area/', 'admin_area/login.%EXT%', 'manager/', 'superuser/', 'superuser.%EXT%', 'access/', 'access.%EXT%', 'sysadm/', 'sysadm.%EXT%', 'superman/', 'supervisor/', 'panel.%EXT%', 'control/', 'control.%EXT%', 'member/', 'member.%EXT%', 'members/', 'user/', 'user.%EXT%', 'cp/', 'uvpanel/', 'manage/', 'manage.%EXT%', 'management/', 'management.%EXT%', 'signin/', 'signin.%EXT%', 'log-in/', 'log-in.%EXT%', 'log_in/', 'log_in.%EXT%', 'sign_in/', 'sign_in.%EXT%', 'sign-in/', 'sign-in.%EXT%', 'users/', 'users.%EXT%', 'accounts/', 'accounts.%EXT%', 'bb-admin/login.%EXT%', 'bb-admin/admin.%EXT%', 'bb-admin/admin.html', 'administrator/account.%EXT%', 'relogin.htm', 'relogin.html', 'check.%EXT%', 'relogin.%EXT%', 'blog/wp-login.%EXT%', 'user/admin.%EXT%', 'users/admin.%EXT%', 'registration/', 'processlogin.%EXT%', 'checklogin.%EXT%', 'checkuser.%EXT%', 'checkadmin.%EXT%', 'isadmin.%EXT%', 'authenticate.%EXT%', 'authentication.%EXT%', 'auth.%EXT%', 'authuser.%EXT%', 'authadmin.%EXT%', 'cp.%EXT%', 'modelsearch/login.%EXT%', 'moderator.%EXT%', 'moderator/', 'controlpanel/', 'controlpanel.%EXT%', 'admincontrol.%EXT%', 'adminpanel.%EXT%', 'fileadmin/', 'fileadmin.%EXT%', 'sysadmin.%EXT%', 'admin1.%EXT%', 'admin1.html', 'admin1.htm', 'admin2.%EXT%', 'admin2.html', 'yonetim.%EXT%', 'yonetim.html', 'yonetici.%EXT%', 'yonetici.html', 'phpmyadmin/', 'myadmin/', 'ur-admin.%EXT%', 'ur-admin/', 'Server.%EXT%', 'Server/', 'wp-admin/', 'administr8.%EXT%', 'administr8/', 'webadmin/', 'webadmin.%EXT%', 'administratie/', 'admins/', 'admins.%EXT%', 'administrivia/', 'Database_Administration/', 'useradmin/', 'sysadmins/', 'sysadmins/', 'admin1/', 'system-administration/', 'administrators/', 'pgadmin/', 'directadmin/', 'staradmin/', 'ServerAdministrator/', 'SysAdmin/', 'administer/', 'LiveUser_Admin/', 'sys-admin/', 'typo3/', 'panel/', 'cpanel/', 'cpanel_file/', 'platz_login/', 'rcLogin/', 'blogindex/', 'formslogin/', 'autologin/', 'manuallogin/', 'simpleLogin/', 'loginflat/', 'utility_login/', 'showlogin/', 'memlogin/', 'login-redirectn', 'sub-login/', 'wp-login/', 'login1/', 'dir-login/', 'login_db/', 'xlogin/', 'smblogin/', 'customer_login/', 'UserLogin/', 'login-us/', 'acct_login/', 'bigadmin/', 'project-admins/', 'phppgadmin/', 'pureadmin/', 'sql-admin/', 'radmind/', 'openvpnadmin/', 'wizmysqladmin/', 'vadmind/', 'ezsqliteadmin/', 'hpwebjetadmin/', 'newsadmin/', 'adminpro/', 'Lotus_Domino_Admin/', 'bbadmin/', 'vmailadmin/', 'Indy_admin/', 'ccp14admin/', 'irc-macadmin/', 'banneradmin/', 'sshadmin/', 'phpldapadmin/', 'macadmin/', 'administratoraccounts/', 'admin4_account/', 'admin4_colon/', 'radmind-1/', 'Super-Admin/', 'AdminTools/', 'cmsadmin/', 'SysAdmin2/', 'globes_admin/', 'cadmins/', 'phpSQLiteAdmin/', 'navSiteAdmin/', 'server_admin_small/', 'logo_sysadmin/', 'power_user/', 'system_administration/', 'ss_vms_admin_sm/', 'bb-admin/', 'panel-administracion/', 'instadmin/', 'memberadmin/', 'administratorlogin/', 'adm.%EXT%', 'admin_login.%EXT%', 'panel-administracion/login.%EXT%', 'pages/admin/admin-login.%EXT%', 'pages/admin/', 'acceso.%EXT%', 'admincp/login.%EXT%', 'admincp/', 'adminarea/', 'admincontrol/', 'affiliate.%EXT%', 'adm_auth.%EXT%', 'memberadmin.%EXT%', 'administratorlogin.%EXT%', 'modules/admin/', 'administrators.%EXT%', 'siteadmin/', 'siteadmin.%EXT%', 'adminsite/', 'kpanel/', 'vorod/', 'vorod.%EXT%', 'vorud/', 'vorud.%EXT%', 'adminpanel/', 'PSUser/', 'secure/', 'webmaster/', 'webmaster.%EXT%', 'autologin.%EXT%', 'userlogin.%EXT%', 'admin_area.%EXT%', 'cmsadmin.%EXT%', 'security/', 'usr/', 'root/', 'secret/', 'admin/login.%EXT%', 'admin/adminLogin.%EXT%', 'moderator.php', 'moderator.html', 'moderator/login.%EXT%', 'moderator/admin.%EXT%', 'yonetici.%EXT%', '0admin/', '0manager/', 'aadmin/', 'cgi-bin/login%EXT%', 'login1%EXT%', 'login_admin/', 'login_admin%EXT%', 'login_out/', 'login_out%EXT%', 'login_user%EXT%', 'loginerror/', 'loginok/', 'loginsave/', 'loginsuper/', 'loginsuper%EXT%', 'login%EXT%', 'logout/', 'logout%EXT%', 'secrets/', 'super1/', 'super1%EXT%', 'super_index%EXT%', 'super_login%EXT%', 'supermanager%EXT%', 'superman%EXT%', 'superuser%EXT%', 'supervise/', 'supervise/Login%EXT%', 'super%EXT%']

print(yellow + banner)
tam = int(len(word))
print(tam, "links in Wordlist\n=================================================================================")
try:
	print(white + "[?] Testing:", url, "with", tam, "links!\n")
	for final in word:
		hostfinal = url + "/" + final
		connect = requests.get(hostfinal) 
		var = connect.status_code == 200
		if var:
			print(hora, white + "[+]" + green, hostfinal + blue + " // CODE" + green + " --->> 200 <<--- FOUND!!!")
		else:
			print(hora,  white + "[-]" + red, hostfinal + blue + " // CODE =>> " + red + str(connect.status_code))
except KeyboardInterrupt:
	print(red + "\n[-] Stopped")

except:
	help_window()