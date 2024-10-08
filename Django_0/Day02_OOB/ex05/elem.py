#!/usr/bin/python3

class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        data = super().__str__()
        data = data.replace('<', '&lt;')
        data = data.replace('>', '&gt;')
        data = data.replace('"', '&quot;')
        data = data.replace('\n', '\n<br />\n')
        return data


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    class ValidationError(Exception):
        def __init__(self):
            self.message = 'This content is not a text or an element'
        
        def __str__(self):
            return self.message

    def __init__(self, tag='div', attr=None, content=None, tag_type='double'):
        self.tag = tag
        self.attr = attr if attr is not None else {}
        self.tag_type = tag_type
        self.content = []
        
        if content:
            self.add_content(content)
        elif content is not None:
            if not isinstance(content, Text):
                raise Elem.ValidationError()

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        attr = self.__make_attr()
        if self.tag_type == 'double':
            result = f'<{self.tag}{attr}>'
            result += f'{self.__make_content()}'
            result += f'</{self.tag}>'
        elif self.tag_type == 'simple':
            result = f'<{self.tag}{attr} />'
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """

        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            elem_string = str(elem)
            replace_string = elem_string.replace("\n", "\n  ")
            result += f'  {replace_string}\n'
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))
