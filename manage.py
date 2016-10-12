from flask_script import Manager, Server
from app import app
import os


manager = Manager(app)

# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host=os.environ.get('IP', '0.0.0.0'),
    port=os.environ.get('PORT', 5000))
)

if __name__ == "__main__":
    manager.run()
