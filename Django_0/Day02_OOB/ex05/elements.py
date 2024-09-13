#!/usr/bin/python3

from elem import Elem, Text

class Html(Elem):
    def __init__(self, content=None, attr=None, tag_type='double'):
        super().__init__(tag='html', content=content, attr=attr, tag_type=tag_type)

class Head(Elem):
    def __init__(self, content=None):
        super().__init__(tag='head', content=content, tag_type='double')
        
class Body(Elem):
    def __init__(self, content=None):
        super().__init__(tag='body', content=content, tag_type='double')
        
class Title(Elem):
    def __init__(self, content=None):
        super().__init__(tag='title', content=content, tag_type='double')

class Meta(Elem):
    def __init__(self, attr={}):
        super().__init__(tag='meta', attr=attr, tag_type='simple')
    
class Img(Elem):
    def __init__(self, attr={}):
        super().__init__(tag='img', attr=attr, tag_type='simple')
        
class Table(Elem):
    def __init__(self, content=None):
        super().__init__(tag='table', content=content, tag_type='double')
        
class Th(Elem):
    def __init__(self, content=None):
        super().__init__(tag='th', content=content, tag_type='double')
        
class Tr(Elem):
    def __init__(self, content=None):
        super().__init__(tag='tr', content=content, tag_type='double')

class Td(Elem):
    def __init__(self, content=None):
        super().__init__(tag='td', content=content, tag_type='double')
        
class Ul(Elem):
    def __init__(self, content=None):
        super().__init__(tag='ul', content=content, tag_type='double')
    
class Ol(Elem):
    def __init__(self, content=None):
        super().__init__(tag='ol', content=content, tag_type='double')
        
class Li(Elem):
    def __init__(self, content=None):
        super().__init__(tag='li', content=content, tag_type='double')
        
class H1(Elem):
    def __init__(self, content=None):
        super().__init__(tag='h1', content=content, tag_type='double')
        
class H2(Elem):
    def __init__(self, content=None):
        super().__init__(tag='h2', content=content, tag_type='double')
        
class P(Elem):
    def __init__(self, content=None):
        super().__init__(tag='p', content=content, tag_type='double')
        
class Div(Elem):
    def __init__(self, content=None):
        super().__init__(tag='div', content=content, tag_type='double')
        
class Span(Elem):
    def __init__(self, content=None):
        super().__init__(tag='span', content=content, tag_type='double')
        
class Hr(Elem):
    def __init__(self, content=None):
        super().__init__(tag='hr', content=content, tag_type='simple')
        
class Br(Elem):
    def __init__(self, content=None):
        super().__init__(tag='br', content=content, tag_type='simple')

if __name__ == '__main__':
    html = Html([
                Meta(attr={'charset' : 'utf-8'}), 
                Head([Title(content=Text('"Hello ground!"'))]), 
                Body([
                    H1(content=Text('"One Piece"')),
                    Hr(),
                    P(content=Text('"Oda is a champion !"')),
                    Div([Table([
                            Th(content=Text('"Mugiwara\'s team"')), 
                            Tr([Td(content=Text('"Luffy"'))]),
                            Tr([Td(content=Text('"Zorro"'))]), 
                            Tr([Td(content=Text('"Nami"'))]), 
                            Tr([Td(content=Text('"Sanji"'))]), 
                            Tr([Td(content=Text('"Brook"'))]), 
                            Tr([Td(content=Text('"Franky"'))]),
                            ]),
                        ]),
                    Br(),
                    Img(attr={'src' : 'https://bit.ly/3Bc9gME'}),
                    Br(),
                    H2(content=Text('"Heart\'s team"')),
                    Br(),
                    Span(content=Text('"Great team !"')),
                    Ol([
                        Li(content=Text('"Bepo"')),
                        Li(content=Text('"Jean Bart"')),
                    ]),
                    Ul([
                        Li(content=Text('"Pinguin"')),
                        Li(content=Text('"Shachi"'))
                    ])
                ])], attr={'lang' : 'en'})
    print(html)