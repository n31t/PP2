import json

with open('/Users/adilovamir/Desktop/PP2/week4/LAB4/jsonn/JSON.json') as file:
    json_data = json.load(file)
    print("""
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
    """)
    imdata = json_data["imdata"]
    for item in imdata:
        phys = item["l1PhysIf"]
        attribs = phys["attributes"]
        dn = attribs["dn"]
        speed = attribs["speed"]
        mtu = attribs["mtu"]
        output = ""
        if (len(dn) == 42):
            output += dn + "                              " + speed + "   " + mtu
        else:
            output += dn + "                               " + speed + "   " + mtu

        print(output)
