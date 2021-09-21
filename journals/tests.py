from django.test import TestCase
from .models import Editor,Post,Comment,tags
# Create your tests here.

class EditorTestClass(TestCase):
  #setup method
  def setUp(self):
    self.editor1 = Editor(username = "JohnTheDon" , first_name = "John", last_name = "Clifford", email = 'cliff@gmail.com', profile_pic = 'print.jpg')

  def test_instance(self):
    self.assertTrue(isinstance(self.editor1, Editor))