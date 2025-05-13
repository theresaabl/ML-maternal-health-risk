import streamlit as st

class MultiPage: 
    """
    Create an instance of MultiPage
    Class to generate multiple streamlit pages
    """
    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title=self.app_name,
            page_icon=":hospital:")
    
    def add_page(self, title, func) -> None:
        """
        Add a page to the multipage app
        """
        self.pages.append({"title": title, "function": func })

    def run(self):
        """
        Run the multipage app
        Display the sidebar menu with the app pages
        """
        st.title(self.app_name)
        page = st.sidebar.radio(
            'Menu',
            self.pages,
            format_func=lambda page: page['title']
            )
        page['function']() 