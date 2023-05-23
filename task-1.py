import base64
steps = ["plan", "code", "test", "delivery", "deploy", "monitor"]

for step in steps:
    #encode = step.encode("UTF-8")
    #encoded = base64.b64encode(encode)
    #print(encoded)

    encoded = base64.b64encode(step.encode('UTF-8')).decode('UTF-8')
    print(encoded)