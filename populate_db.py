from flask import Flask
from models import db, ItemLista

# Cria uma app Flask temporária
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:SUA_SENHA_AQUI@localhost:5432/lista_casamento'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Conecta o banco a esta app
db.init_app(app)

# Mesma lista de itens que você tinha...
itens_exemplo = [
    {
        'nome': 'Jogo de Panelas Tramontina',
        'descricao': 'Jogo 10 peças em inox, antiaderente',
        'valor': 349.90,
        'imagem_url': 'https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80'
    },
    {
        'nome': 'Máquina de Café Nespresso',
        'descricao': 'Máquina de café espresso com cápsulas',
        'valor': 449.90,
        'imagem_url': 'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80'
    },
    {
        'nome': 'Jogo de Toalhas de Banho',
        'descricao': 'Conjunto 6 peças 100% algodão egípcio',
        'valor': 189.90,
        'imagem_url': 'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80'
    },
    {
        'nome': 'Air Fryer Mondial',
        'descricao': 'Fritadeira elétrica 4L, preta',
        'valor': 399.90,
        'imagem_url': 'https://images.unsplash.com/photo-1630382732125-0f8c8e2d7d30?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80'
    },
    {
        'nome': 'Conjunto de Facas Cutco',
        'descricao': 'Conjunto 8 peças com suporte de madeira',
        'valor': 299.90,
        'imagem_url': 'https://images.unsplash.com/photo-1583773724168-20af40b6a7e9?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80'
    },
    {
        'nome': 'Jogo de Cama Queen Size',
        'descricao': 'Conjunto 4 peças 300 fios, almofadas inclusas',
        'valor': 279.90,
        'imagem_url': 'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80'
    }
]

reservados_exemplo = [
    {
        'nome': 'Liquidificador Oster',
        'descricao': 'Liquidificador 600W, jarra de vidro',
        'valor': 159.90,
        'imagem_url': 'https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80',
        'reservado': True,
        'reservado_por': 'Tia Maria'
    },
    {
        'nome': 'Conjunto de Taças de Vinho',
        'descricao': '6 taças de vinho tinto, cristal',
        'valor': 129.90,
        'imagem_url': 'https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80',
        'reservado': True,
        'reservado_por': 'Primo Carlos'
    }
]

# Executa dentro do contexto da aplicação
with app.app_context():
    # Cria tabelas (se não existirem)
    db.create_all()
    
    # Limpa dados existentes
    ItemLista.query.delete()
    
    # Adiciona todos os itens
    for dados_item in itens_exemplo:
        item = ItemLista(**dados_item)
        db.session.add(item)
    
    for dados_item in reservados_exemplo:
        item = ItemLista(**dados_item)
        db.session.add(item)
    
    db.session.commit()
    print(f'✅ {len(itens_exemplo) + len(reservados_exemplo)} itens adicionados ao banco!')