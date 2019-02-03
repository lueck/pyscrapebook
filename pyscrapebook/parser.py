from html.parser import HTMLParser

# Inherit from object because HTMLParser in Python 2.7 is not a new
# style class. See
# https://stackoverflow.com/questions/1713038/super-fails-with-error-typeerror-argument-1-must-be-type-not-classobj-when

class HTML2TextParser(HTMLParser, object):

    def __init__(self, handle,
                 content_el = "div",
                 content_id = "content",
                 next_url_tag = "a",
                 next_url_label = "next",
                 next_url_attr = "href"):
        self.out = handle
        self.content_el = content_el
        self.content_id = content_id
        self.next_url_tag = next_url_tag
        self.next_url_label = next_url_label
        self.next_url_attr = next_url_attr
        # init state
        self.open_tags = list()
        self.content = False
        self.content_done = False
        self.content_string = ""
        self.next_url = None
        self.inner = ""
        super(HTML2TextParser, self).__init__()
        
    def is_content_container(self, tag, attrs):
        if tag.lower() == self.content_el:
            for (k, v) in attrs:
                if str.lower(k) == "id":
                    if v.lower() == self.content_id:
                        return True
        return False

    def has_next_url(self, tag, attrs):
        if tag == self.next_url_tag:
            if self.next_url_label in self.inner:
                for (k, v) in attrs:
                    if k.lower() == self.next_url_attr:
                        return True
        return False
    
    def get_next_url(self, tag, attrs, default = None):
        if tag == self.next_url_tag:
            for (k, v) in attrs:
                if k.lower() == self.next_url_attr:
                    return v
        return default
    
    def handle_starttag(self, tag, attrs):
        self.open_tags.append((tag, attrs))
        self.inner = ""
        if self.content:
            if any(tag == s for s in ["p", "div"]):
                self.out.write("\n")
        if self.is_content_container(tag, attrs):
            self.content = True

    def handle_endtag(self, tag):
        # if self.content:
        #     if any(tag == s for s in ["p", "div"]):
        #         self.out.write("\n")
        while True:
            (top_tag, top_attrs) = self.open_tags.pop()
            if self.is_content_container(top_tag, top_attrs):
                self.content = False
                self.content_done = True
                self.content_string = self.content_string.strip()
            if self.has_next_url(top_tag, top_attrs):
                self.next_url = self.get_next_url(top_tag, top_attrs)
            if top_tag == tag:
                break

    def handle_startendtag(self, tag, attrs):
        if self.content:
            if any(tag == s for s in ["br", "p", "div"]):
                self.out.write("\n")
            
    def handle_data(self, data):
        self.inner = self.inner + data
        if self.content:
            u = data.replace('\\n', '\n') #.strip()
            self.content_string = self.content_string + u.strip()
            self.out.write(u)

    def handle_entityref(self, name):
        c = unichr(name2codepoint[name])
        self.inner = self.inner + c
        if self.content:
            self.out.write(c)
            self.content_string = self.content_string + c

    def handle_charref(self, name):
        if name.startswith('x'):
            c = unichr(int(name[1:], 16))
        else:
            c = unichr(int(name))
        self.inner = self.inner + c
        if self.content:
            self.out.write(c)
            self.content_string  = self.content_string + c
        
