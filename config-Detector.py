config_inpt = input("Enter ypur Config : ").lower()
uuid = "uuid"
address = "google.com"
port = "443"
security = "tls"
transmit = "type" # example : ws
host = "subdomain.com"
path = "/admin"
sni = "subdomain.com"
fingerprint = "chrome"
#type detect
type=config_inpt.split(":")[0]
name = config_inpt.split("#")[1]
if type == "vless" :
    uuid = config_inpt.split("@")[0].split("//")[1]
    address = config_inpt.split("@")[1].split(":")[0]
    port = config_inpt.split("@")[1].split(":")[1].split("?")[0]
    sec2 = config_inpt.split("@")[1].split(":")[1].split("?")[1]
    sec2_list = sec2.split("&")
    print(sec2_list)
    count = len(sec2_list)
    for i in range(0,count) :
        str_sec2_list = str(sec2_list[i])
        if "security" in str_sec2_list :
            security = sec2_list[i].split("=")[1]
        # finde transmit
        elif transmit in str_sec2_list :
             transmit = sec2_list[i].split("=")[1]
        elif "host" in str_sec2_list : 
            host = sec2_list[i].split("=")[1]
        elif "path" in str_sec2_list :
            path = sec2_list[i].split("=")[1].split("%2f")[1]
        elif "sni" in str_sec2_list :
            sni = sec2_list[i].split("=")[1]
        elif "fp" in str_sec2_list :
            fingerprint = sec2_list[i].split("=")[1]
        elif "alpn" in str_sec2_list :
            alpn = sec2_list[i].split("=")[1].split("#")[0]


print(type)
print(uuid)
print(address)
print(port)
print(security)
print(transmit)
print(host)
print(path)
print(sni)
print(fingerprint)
print(alpn)
print(name)