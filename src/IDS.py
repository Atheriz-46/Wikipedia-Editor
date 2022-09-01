from typing import List
from tkinter import font
import tkinter as tk
from constants import heading_size


class IDS:
    """Internal Data Structure to act as a Bridge between md file and Tkinter object"""

    def __init__(self, val: str, viewer, type_: str = "leaf", children=[], **kwargs):
        """Initialises the IDS

        Args:
            val (str): the text values associated with the node
            viewer (Viewer): Viewer Object
            type_ (str, optional): type of Node [root,leaf,list]. Defaults to 'leaf'.
            children (list, optional): List of children, only if type_='root'. Defaults to [].
        """
        self.val = val
        self.child: List[IDS] = []
        if children:
            self.child += children
        self.type_ = type_  # ['root','list','non-list']
        self.params = kwargs
        self.viewer = viewer

    def __str__(self):
        """Converts to string

        Returns:
            string: Custom string representation of subtree rooted at self
        """
        return (
            f"type:{self.type_}, val:{self.val}, params:{str(self.params)}"
            + "\n("
            + "".join(str(child) for child in self.child)
            + ")"
        )

    def getFrame(self, text=None, enum=-1):
        """Converts the subtree rooted at self to corresponding tk.Text object

        Args:
            text (tk.Text, optional): The tk.Text object to render the subtree. Defaults to None.
            enum (int, optional): to maintain the tag attribute currospinding to the current node. Defaults to -1.

        Returns:
            (tk.text, optional): the final tk.text object
        """

        if self.type_ == "root":
            for idx, child in enumerate(self.child):
                child.getFrame(text, idx)
            return text

        if self.type_ == "list":
            tag = f"tag_{enum}"
            text.insert(tk.END, self.val, tag)
            curr_font = font.Font(text, text.cget("font"))
            font_config = {}
            font_config["size"] = heading_size["h0"]
            curr_font.configure(**font_config)
            tag_config = {"font": curr_font}
            text.tag_configure(tag, **tag_config)
        else:

            tag = f"tag_{enum}"
            text.insert(tk.END, self.val, tag)
            curr_font = font.Font(text, text.cget("font"))
            font_config = {
                k: v for k, v in self.params.items() if k in ["slant", "weight"]
            }
            font_config["size"] = heading_size[self.params.get("heading", "h0")]
            curr_font.configure(**font_config)

            tag_config = {"font": curr_font}
            if "link_to" in self.params:
                tag_config = {**tag_config, "foreground": "blue", "underline": 1}
                text.tag_bind(
                    tag,
                    "<1>",
                    lambda event, link=self.params["link_to"]: self.click(link),
                )
            text.tag_configure(tag, **tag_config)

    def click(self, link):
        """Callback function to handle links

        Args:
            link (str): The name of the destination article
        """
        print(f"goto {link}")
        self.viewer.link(link)
