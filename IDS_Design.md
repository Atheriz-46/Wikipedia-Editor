# Problems:
- Nested lists ?

# Functions to be supported
* bold
* italics
* headings
* links = [Link](path/file_name in our context) 
    - support both local and global links (can be done by checking for the presence of "https://")
* bulleted lists.

# Dynamics of different categories
* Bold and italics
    * needs to have no space between star and the following text
    * can be inside headings
    * can be inside lists (not the opposite)
    - b+i is *** so can be treated as a category of its own
    - can be applied to the whole link * []() * or inside the link text body.(Not to be parsed inside the link destination) (and as a combination of both as well)


* Headings 
    -  b,i:
       -  B-I inside heading works
       -  Heading inside B_I does not
    -  headings :  does not support other headings inside one heading
    -  needs a space after the indicator
    -  Extra continous hashs will result in all hashes to be parsed as hashes inplace of metacharacters.
    -  Links: 
       -  supports links in the heading
       -  Does **Not** support heading inside link text.
   - supports heading inside bullet'
- Links
  - supports to be inside lists, not list inside them.
  

# IDS design
## The IDS node class:
This will be the basic building block of our IDS. The structure needs to be such that there is easy translation from md to ids and ids to the tkinter frame. Since only one direction of the transformation is required, this makes the choice of structure, linear or nested, for the IDS, important. Since we need to finally get a tkinter object, we choose the nested structure as that most closely resembles the tkinter flow.

So we will define every node to have:
- type
- value
- children
  
### Types
we define the following types:
- document
-  plain
- heading - h1-h6
- link
- bold
- italics
- bold+italics 

### Notes
- text
- bi
  - texts
- Links
  - bi
- Headings
  - Links
  - bi
- list
  - list
  - heading 
  - Link
  - bi
    - bi
      - bi  
        - bi

### Types#2
We will store the following in metadata:
    bold,italics, bi, Headings(size), link_to,