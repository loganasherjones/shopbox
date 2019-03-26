from shopbox.shopbox import app
from shopbox.util import sanic_config_manager


sanic_config_manager(app, prefix="SHOPBOX_")


if __name__ == "__main__":

    app.run()
