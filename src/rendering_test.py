import pyglet
import pyglet.gl as gl
import random 
import json

gl.glEnable(gl.GL_BLEND)
gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)

pyglet.resource.path = ['../res']
pyglet.resource.reindex()

with pyglet.resource.file('images.json') as f:
	waifus = json.load(f)
with pyglet.resource.file('hues.json') as f:
	hues = json.load(f)
hues = hues['pastel']

currHue = {}
currWaifu = {}

window = pyglet.window.Window(
	width = 1280, height = 720, resizable=True, visible=True, 
	style=pyglet.window.Window.WINDOW_STYLE_BORDERLESS)



def get_render(currHue,currWaifu,hues,waifus):
	nextHue = currHue
	nextWaifu = currWaifu
	while(currHue == nextHue or currWaifu == nextWaifu):
		nextHue = random.choice(hues)
		nextWaifu = waifus[random.choice(list(waifus))]
	return(nextHue,nextWaifu)

def get_color(currHue):
	color = currHue['color']
	return (int(color[2:4],16)/0xff,int(color[4:6],16)/0xff,int(color[6:8],16)/0xff,1)

def get_image_path(currWaifu):
	return (currWaifu['package'] + "/" + currWaifu['file_type'] + "/" + currWaifu['file_name'] + ".png")

def animate_transition
@window.event
def on_draw():
	global currHue
	global currWaifu
	currHue, currWaifu = get_render(currHue,currWaifu,hues,waifus)
	gl.glClearColor(*get_color(currHue))
	image = pyglet.resource.image(get_image_path(currWaifu))
	sprite = pyglet.sprite.Sprite(img=image,x=0,y=0)
	window.clear()
	sprite.draw()

pyglet.app.run()