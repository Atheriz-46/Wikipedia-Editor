import re
from IDS import IDS


class MarkdownParser:
    """Parser for md to IDS."""

    def __init__(self, viewer):
        """Initializes the MarkdownParser

        Args:
            viewer (Viewer): provides the corresponding viewer object
        """
        self.viewer = viewer
        self.result = []
        self.prev_level = -1

    def parse(self, md):
        """Parses the given markdown string and sets the

        Args:
            md (_type_): _description_
        """
        self.__init__(self.viewer)
        for line in md.split("\n"):
            self.isList(line + "\n")
        self.root = IDS("", viewer=self.viewer, children=self.result, type_="root")

    def getFrame(self, text):
        """Returns the rendered tk.Text object corresponding to the md parsed.

        Args:
            text (tk.Text): tk.Text object to dump all the formatted text into

        Returns:
            tk.Text: Rendered tk.Text object, ready to be packed
        """
        return self.root.getFrame(text)

    def getRe(self, type_, *args, **kwargs):
        """Returns the corresponding regex object

        Args:
            type_ (str): denotes the regex type wanted

        Returns:
            re.pattern : returns the regex pattern object
        """
        if type_ == "list":
            return re.compile(rf"(\t{{0,{kwargs['level']}}})[\-\*] ([\S\s]*)")
        if type_ == "heading":
            return re.compile(rf"(#{{1,6}}) ([\S\s]*)")
        if type_ == "link":
            return re.compile(
                rf"([\S\s]*)\[([^\n\f\v\r\]]+)\]\(([^\n\f\v\r\t \)]+)\)([\S\s]*)"
            )
        if type_ == "bi":
            return re.compile(
                rf"([\S\s]*)((\*{{{kwargs['level']}}})(\S.*?[^\s\*])(\*{{{kwargs['level']}}})|(\_{{{kwargs['level']}}})(\S.*?[^\s\_])(\_{{{kwargs['level']}}}))([\S\s]*)"
            )

    def isList(self, md, params={}):
        """Checks if current line is list and parses it further

        Args:
            md (str): the partial markdown file
            params (dict, optional): to pass the style params. Defaults to {}.
        """
        regex = self.getRe("list", level=self.prev_level + 1)
        match = regex.match(md)
        if match:
            val, self.prev_level = match.group(2), len(match.group(1))
            self.result.append(
                IDS(
                    val="   " * self.prev_level + "\u2022 ",
                    viewer=self.viewer,
                    type_="list",
                    params=params,
                )
            )
            self.isHeading(val, params)
        else:
            self.prev_level = -1
            self.isHeading(md, params)

    def isHeading(self, md, params):

        """Checks if current line is heading and parses it further

        Args:
            md (str): the partial markdown file
            params (dict): to pass the style params.
        """
        regex = self.getRe("heading")
        match = regex.match(md)
        if match:
            val, depth = match.group(2), len(match.group(1))
            if depth == 1:
                params["underline"] = 1
            self.isLink(val, {**params, "heading": f"h{depth}"})

        else:
            self.isLink(md, params)

    def isLink(self, md, params):
        """Checks if current line is link and parses it further

        Args:
            md (str): the partial markdown file
            params (dict): to pass the style params.
        """
        regex = self.getRe("link")
        match = regex.match(md)
        if match:
            pre, text, link, post = (
                match.group(1),
                match.group(2),
                match.group(3),
                match.group(4),
            )
            self.isStyle(pre, params)
            self.isStyle(text, {**params, "link_to": link})
            self.isLink(post, params)
        else:
            self.isStyle(md, params)

    def isStyle(self, md, params):
        """Checks if current line is bold or italics and parses it further

        Args:
            md (str): the partial markdown file
            params (dict): to pass the style params.
        """
        for level, style in [[3, "bi"], [2, "b"], [1, "i"]]:
            regex = self.getRe("bi", level=level)
            match = regex.match(md)
            if match:
                if match.group(4):
                    val = match.group(4)
                elif match.group(7):
                    val = match.group(7)
                pre, post = match.group(1), match.group(9)
                self.isText(pre, params)
                style_config = {}
                style_config["slant"] = "italic" if "i" in style else "roman"
                style_config["weight"] = "bold" if "b" in style else "normal"

                self.isText(val, {**params, **style_config})
                self.isStyle(post, params)
                break
        else:
            self.isText(md, params)

    def isText(self, md, params):
        """Checks if current line is text and parses it further

        Args:
            md (str): the partial markdown file
            params (dict): to pass the style params.
        """
        self.result.append(IDS(md, viewer=self.viewer, **params))
