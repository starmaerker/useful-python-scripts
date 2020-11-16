import subprocess

# if you have problems with umlauts use decode('utf-8', errors='ignore) or another decoding
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('CP850').split('\n')
wifis = [line.split(':')[1][1:-1] for line in data if "Profil für alle Benutzer" in line]

for wifi in wifis:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('CP850').split('\n')
    results = [line.split(':')[1][1:-1] for line in results if "Schlüsselinhalt" in line]
    try:
        print(f'Name: {wifi}, Passwort: {results[0]}')
    except IndexError:
        print(f'Name: {wifi}, Passwort: ist nicht gespeichert')