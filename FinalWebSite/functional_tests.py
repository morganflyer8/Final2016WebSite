# Boiler Plate


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import os

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		if os.name=='nt':
			self.browser = webdriver.Chrome()
		else:
			self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
			self.browser.quit()

	def test_home_page(self):
		self.browser.get('http://localhost:8000/index.html')
		# when we are on the home page, the page title says "The Mandelbrot Set"
		self.assertIn("The Mandelbrot Set",self.browser.title)
		a=self.browser.find_element_by_tag_name('h1')
		a=self.browser.find_element_by_tag_name('img')
		self.assertIn('M.jpg',a.get_attribute('src'))
		
		
		a=self.browser.find_element_by_id('code')
		a.click()
		h=self.browser.find_element_by_tag_name('h1')
		self.assertIn('The Code',self.browser.title)
		m=self.browser.find_element_by_tag_name('img')
		self.assertIn('mbrot.png',m.get_attribute('src'))
		a=self.browser.find_element_by_id ('index')
		a.click()
		
		

if __name__=="__main__":		
	unittest.main(warnings="ignore")
