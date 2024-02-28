config_inpt = input("Enter ypur Config : ").lower()
"vless://310caefd-0cdb-4e93-a695-29a800b4e616@op2mtnir.l.wikm.eu.org:2053?security=tls&type=ws&host=ground.wikmgg.top&headerType=&path=%2Fwikm2053&sni=ground.wikmgg.top&fp=chrome&alpn=http%2F1.1#CDN-MTN%F0%9F%9F%A2"
uuid = "uuid"
address = "google.com"
port = "443"
security = "tls"
transmit = "type"
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
        words = transmit.split()
        if "security" in sec2_list[i] :
            security = sec2_list[i].split("=")[1]
        for word in words:
            if word == sec2_list[i].split("=")[1]:
               return True
        # elif words in str_sec2_list :
        #     transmit = sec2_list[i].split("=")[1]
        elif "host" in sec2_list[i] : 
            host = sec2_list[i].split("=")[1]

print(type)
print(uuid)
print(address)
print(port)
print(security)
print(transmit)
print(host)