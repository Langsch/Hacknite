from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

# ficam aqui (e nao no app.py) para os models e as rotas poderem importar sem import circular
db = SQLAlchemy()
csrf = CSRFProtect()
