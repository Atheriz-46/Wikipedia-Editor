"""
IDS Structure:

to support: bold, italics, list, H1-H3 

"""


from typing import List


class IDS:
    type_: str
    val: str
    
    def __init__(self,type_: str,val:str):
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
        for type_,val in children:
            child = IDS(type_=type_,val=val)
            self.addChild(child)

    def get_frame(self):
        #convert all the children into frame and then use the subframes to build up the current module.
        pass