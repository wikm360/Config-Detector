config_inpt = input("Enter ypur Config : ").lower()
"vless://310caefd-0cdb-4e93-a695-29a800b4e616@op2mtnir.l.wikm.eu.org:2053?security=tls&type=ws&host=ground.wikmgg.top&headerType=&path=%2Fwikm2053&sni=ground.wikmgg.top&fp=chrome&alpn=http%2F1.1#CDN-MTN%F0%9F%9F%A2"
uuid = "uuid"
address = "google.com"
port = "443"
security = "tls"
transmit = "type" # example : ws
host = "subdomain.com"
#type detect
type=config_inpt.split(":")[0]
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

print(type)
print(uuid)
print(address)
print(port)
print(security)
print(transmit)
print(host)