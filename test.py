import BlynkLib

# Initialize Blynk
blynk = BlynkLib.Blynk("TcWuMJZQ6VQSbwliortUqpTqRHt1CZ5a")

# Register Virtual Pins
@blynk.on("connected")
def connected():
    print('Connected')


@blynk.on("V0")
def blynk_handle_vpins(value):
    print(value)

while True:
    blynk.run()