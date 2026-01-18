from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ItemLista(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text)
    valor = db.Column(db.Float)
    imagem_url = db.Column(db.String(200))
    reservado = db.Column(db.Boolean, default=False)
    reservado_por = db.Column(db.String(100))
    
    def __repr__(self):
        return f'<Item {self.nome}>'