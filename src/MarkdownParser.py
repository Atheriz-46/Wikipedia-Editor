import re
from IDS import IDS

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