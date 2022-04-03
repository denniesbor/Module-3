from django.test import TestCase
from datetime import datetime

class Search:
    def __init__(self,content,searched=None):
        self.content = content
        self.searched = searched or datetime.now()
