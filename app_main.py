# -*- coding: utf-8 -*-
"""app_main.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TLGgU3ghdCuXIK3nBOy4BDYPQ_o7_-uy
"""

from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
        self.file1 = None
        self.file2 = None

    def file_loader_1_change(self, file, **event_args):
        """This method is called when a new file is loaded into this FileLoader"""
        self.file1 = file

    def file_loader_2_change(self, file, **event_args):
        """This method is called when a new file is loaded into this FileLoader"""
        self.file2 = file

    def button_click(self, **event_args):
        """This method is called when the button is clicked"""
        if self.file1 is not None and self.file2 is not None:
            # Call the compare_docs function asynchronously
            similarity_score, keyword_match, entity_match, name1, phone_number1, skills1,email1 = anvil.server.call('compare_docs', self.file1, self.file2)

        # Check the result
            self.result.text = f"The Similarity score is {similarity_score}"
            self.keyword_match.text = f"{keyword_match}"
            self.entity_match.text = f"{entity_match}"
            self.phone_number.text=f"{phone_number1}"
            self.skill.text=f"{skills1}"
            self.email.text=f"{email1}"
            self.name1.text=f"{name1}"
        else:
            self.result.text = "Error: Unexpected result from server."