import os

class AppRootBase:
    @property
    def app_root(self) -> str:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        app_root = os.path.dirname(current_dir)
        return app_root