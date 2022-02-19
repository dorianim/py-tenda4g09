from tenda4g09 import Tenda4G09

host = "192.168.0.1"
password = "somepassword"

if __name__ == "__main__":
    tenda = Tenda4G09(host)
    if tenda.login(password):
        ret, data = tenda.status()
        if ret:
            print(data["wl24gName"]) # print 3.4GHz Network name
        
        tenda.reboot()

