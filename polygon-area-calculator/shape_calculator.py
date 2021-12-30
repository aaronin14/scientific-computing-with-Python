import math
class Rectangle:
	width = None
	height = None

	def __init__(self,width,height):
		self.width=width
		self.height=height

	def set_width(self,width):
		self.width=width

	def set_height(self,height):
		self.height=height

	def get_area(self):
		return (self.width*self.height)

	def get_perimeter(self):
		return ((self.width+self.height)*2)

	def get_diagonal(self):
		return ((self.width**2 + self.height**2)**0.5)

	def get_picture(self):
		result = ''
		if (self.width > 50) or (self.height > 50):
			result = 'Too big for picture.'
		else:
			for line in range(self.height):
				result += '*'*self.width + '\n'
		return result

	def get_amount_inside(self,shape):
		amount=0
		w_inside=shape.width
		h_inside=shape.height
		#ratio
		w_ratio=math.floor(float(self.width/w_inside))
		h_ratio=math.floor(float(self.height/h_inside))
		if w_ratio >=1 and h_ratio	>=1:
			amount=int(w_ratio*h_ratio)
		return amount



	def __str__(self):
		return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
	def __init__(self,length):
		self.width=length
		self.height=length

	def set_side(self,length):
		self.width=length
		self.height=length
	
	def __str__(self):
		return f'Square(side={self.width})'