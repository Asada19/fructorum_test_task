from datetime import datetime

import opengraph

from .models import LinkTypes


class BookmarkService:
    def __init__(self, link):
        self.link = link
        self.title = ""
        self.description = ""
        self.preview_image = ""
        self.type = "website"
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.fetch_open_graph_data()

    def fetch_open_graph_data(self):
        try:
            og = opengraph.OpenGraph(url=self.link)
            self.title = og.title if og.title else ""
            self.description = og.description if og.description else ""
            self.preview_image = og.image if og.image else ""
            for link_type in LinkTypes.choices:
                self.type = (
                    og.type if og.type.startswith(link_type) else LinkTypes.WEBSITE
                )
        except Exception as e:
            print(f"Failed to fetch Open Graph data: {e}")
