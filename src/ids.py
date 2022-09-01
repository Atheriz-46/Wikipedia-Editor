"""
IDS Structure:

to support: bold, italics, list, H1-H3 

"""


from typing import List
import re
from tkinter import Frame,font
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
        # https://github.com/amandeep511997/Text-Editor/blob/master/main.py
        #convert all the children into frame and then use the subframes to build up the current module.
        
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
        

class MarkdownParser:
    def __init__(self,viewer):
        self.viewer = viewer
        self.result = []
        self.prev_level = -1 
    def parse(self,md):
        self.__init__(self.viewer)
        for line in md.split('\n'):
            self.isList(line+'\n')
        self.root = IDS('',viewer=self.viewer,children=self.result,type_='root')
    
    def getFrame(self,text):
        # frame = tk.Frame(parent, borderwidth=1, relief="sunken")
        # text = tk.Text(master=frame,wrap="word", font=("Liberation Mono", 12), background="white", borderwidth=0, highlightthickness=0)
        # text.pack(in_=frame, side="left", fill="both")
        return self.root.getFrame(text)
        
         
    def getRe(self,type_,*args,**kwargs):
        if type_=='list':
            return re.compile(rf"(\t{{0,{kwargs['level']}}})[\-\*] ([\S\s]*)")
        if type_=='heading':
            return re.compile(rf"(#{{1,6}}) ([\S\s]*)")
        if type_ =='link':
            return re.compile(rf"([\S\s]*)\[([^\n\f\v\r\]]+)\]\(([^\n\f\v\r\t \)]+)\)([\S\s]*)")
        if type_ =='bi':
            return re.compile(rf"([\S\s]*)((\*{{{kwargs['level']}}})(\S.*?[^\s\*])(\*{{{kwargs['level']}}})|(\_{{{kwargs['level']}}})(\S.*?[^\s\_])(\_{{{kwargs['level']}}}))([\S\s]*)")
            
            
    def isList(self,md,params={}):
        regex = self.getRe('list',level= self.prev_level+1)
        match = regex.match(md)
        if match:
            val, self.prev_level = match.group(2), len(match.group(1))
            self.result.append(IDS(val = '   '*self.prev_level + '\u2022 ',viewer=self.viewer,type_ = 'list'))
            self.isHeading(val,params)
        else:
            self.prev_level = -1
            self.isHeading(md,params)

    def isHeading(self,md,params):
        regex = self.getRe('heading')
        match = regex.match(md)
        if match:
            val, depth = match.group(2), len(match.group(1))
            self.isLink(val,{**params,'heading':f'h{depth}'})
                    
        else:
            self.isLink(md,params)
        
    def isLink(self,md,params):
        regex = self.getRe('link')
        match = regex.match(md)
        if match:
            pre, text, link, post = match.group(1), match.group(2), match.group(3),match.group(4)
            self.isStyle(pre,params)
            self.isStyle(text,{**params,'link_to':link})
            self.isLink(post,params)
        else:
            self.isStyle(md,params)
    def isStyle(self,md,params):
        for level,style in [[3,'bi'],[2,'b'],[1,'i']]:
            regex = self.getRe('bi',level = level)
            match = regex.match(md)
            if match:
                if match.group(4):
                    val = match.group(4)
                elif match.group(7):
                    val = match.group(2)
                pre,post = match.group(1), match.group(9)
                self.isText(pre,params)
                style_config = {}
                style_config['slant'] = 'italic' if 'i' in style else 'roman'
                style_config['weight'] = 'bold' if 'b' in style else 'normal'
                
                self.isText(val,{**params,**style_config})
                self.isStyle(post,params)
                break
        else:
            self.isText(md,params)
        
    def isText(self,md,params):
        self.result.append(IDS(md,viewer=self.viewer,**params))

    #TODO: complete line by line parsing
    