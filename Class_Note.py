# -*- coding: utf-8 -*-
from datetime import datetime

class Note:
    def __init__(self, title, content, created_at=None, updated_at=None):
        self.title = title
        self.content = content
        self.created_at = created_at if created_at else datetime.now().isoformat()
        self.updated_at = updated_at if updated_at else self.created_at
    
    def update(self, title=None, content=None):
        if title is not None:
            self.title = title
        if content is not None:
            self.content = content
        self.updated_at = datetime.now().isoformat()
    
    def to_dict(self):
        return {
            'title': self.title,
            'content': self.content,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    @staticmethod
    def from_dict(data):
        return Note(
            data['title'],
            data['content'],
            data.get('created_at'),
            data.get('updated_at')
        )   