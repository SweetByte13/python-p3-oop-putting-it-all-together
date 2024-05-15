#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand=brand
        self._brand=brand
        self.size = size
        self._size= size
        
    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        if brand is (str):
            self._brand = brand
            
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if size is (int):
            self._size = size
        else:
            print("size must be an integer")
            
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        
    def cobble(self, condition='Needs Repair'):
        if condition == 'New':
            self.condition = 'New' 
        else:
            self.condition = 'New'
            print("Your shoe is as good as new!")