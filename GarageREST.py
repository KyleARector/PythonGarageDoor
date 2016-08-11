import time
import web
import RPi.GPIO as GPIO

relay_pin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay_pin, GPIO.OUT)
GPIO.setwarnings(False)

urls = (
    '/', 'index',
    '/relay', 'trigger_relay'
)

class GarageServer(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))

class index:
    def GET(self):
        render = web.template.render('templates')
        return render.index()

class trigger_relay:
    def GET(self):
        output = "{'test': 'hello'}"
        GPIO.output(relay_pin, True)
	time.sleep(1)
	GPIO.output(relay_pin, False)
        return output

if __name__ == "__main__":
    app = GarageServer(urls, globals())
    app.run(port=80)
