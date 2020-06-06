import pyglet
from game_of_life import GameOfLife

class Window(pyglet.window.Window):
	def __init__(self):
		super().__init__(600,600)
		
		self.gameOfLife = GameOfLife(self.get_size()[0], self.get_size()[1],20)
		pyglet.clock.schedule_interval(self.update, 1.0/24.0)
	def on_draw(self):
		self.clear()
		self.gameOfLife.draw()
		self.gameOfLife.run_rules()
	def update(self,dt):
		self.gameOfLife.run_rules()


if __name__=='__main__':
	window=Window()
	pyglet.app.run()
