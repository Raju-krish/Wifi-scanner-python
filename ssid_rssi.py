


import subprocess

SSID_DETAILS = {}

def fetch_ssid_rssi():
    result = subprocess.run(['nmcli device wifi list'], shell=True, text=True, capture_output=True)
    write_file = open("/tmp/raju.txt", "w")
    write_file.write(result.stdout)
    write_file.close()
    read_file = open("/tmp/raju.txt", "r")
    for line in read_file:
        words = line.strip().split()
        sig_index = 0
        ssid = ''
        i = 1
        while i < 5:
            if 'Infra' == words[i]:
                break
            if i == 1:
                if words[0] == '*':
                    i += 1
                ssid = ssid  + words[i]
            else:
                ssid = ssid + ' ' + words[i]
            i += 1
        for mbit in words:
            sig_index += 1
            if 'Mbit/s' == mbit:
                SSID_DETAILS[ssid] = words[sig_index]
    read_file.close()


