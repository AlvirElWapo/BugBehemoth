from main import create_app
from config.config import DevConfig

app = create_app(DevConfig)

if __name__ == '__main__':
    app.run()