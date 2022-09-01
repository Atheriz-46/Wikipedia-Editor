"""
IDS Structure:

to support: bold, italics, list, H1-H3 

"""


from typing import List
from tkinter import font
import tkinter as tk
from constants import heading_size
class IDS:
    
    val: str
    
    def __init__(self, val:str,viewer, type_: str = 'leaf',children = [],**kwargs):
        #TODO: add a way to inherit properties like bi and heading_size from the parent node
        self.val = val
        self.child : List[IDS] = []
        if children: self.child+=children
        self.type_ = type_ #['root','list','non-list']
        self.params = kwargs
        self.viewer = viewer

    def __str__(self):
        return f"type:{self.type_}, val:{self.val}, params:{str(self.params)}" + '\n('+''.join(str(child) for child in self.child)+')'

    def getFrame(self,text=None,enum = -1):        
        if self.type_=='root':
            for idx,child in enumerate(self.child):
                child.getFrame(text,idx)
            return text
        
        if self.type_=='list':
            tag = f'tag_{enum}'
            text.insert(tk.END,self.val,tag)
        else:
            
            tag = f'tag_{enum}'
            text.insert(tk.END,self.val,tag)
            curr_font = font.Font(text,text.cget("font"))
            font_config = {k:v for k,v in self.params.items() if k in ['slant','weight']}
            font_config['size'] = heading_size[self.params.get('heading','h0')] 
            curr_font.configure(**font_config)     
                           
            tag_config = {'font':curr_font}
            if "link_to" in self.params: 
                tag_config = {**tag_config,'foreground':"blue",'underline':1}
                text.tag_bind(tag,'<1>',lambda event,link=self.params['link_to']: self.click(link)) 
            text.tag_configure(tag, **tag_config)
   
    def click(self,link):
        print(f"goto {link}")
        self.viewer.link(link)
