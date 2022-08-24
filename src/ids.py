"""
IDS Structure:

to support: bold, italics, list, H1-H3 

"""


from typing import List


class IDS:
    
    val: str
    
    def __init__(self, val:str, type_: str = 'root',bi = 'None',):
        self.child : List[IDS]
        self.type_ = type_
        
    def addChild(self, child):
        assert isinstance(child,IDS), "Illegal child type"
        self.child.append(child)
        #check the type of the child to be legal for the current type
    
    def parse(self, md: str):
        #extract type of child
        #pass to child
        
        children = None
        for type_,val,child_str in children:
            child = IDS(type_=type_,val=val)
            self.addChild(child)
            child.parse(md = child_str)

    def __str__(self):
        return f"type:{self.type_}, val:{self.val}" + '('+''.join(str(child) for child in self.child)+')'

    def get_frame(self):
        #convert all the children into frame and then use the subframes to build up the current module.
        pass