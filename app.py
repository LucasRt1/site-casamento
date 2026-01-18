from flask import Flask, render_template, request, jsonify
from models import db, ItemLista
import os
from dotenv import load_dotenv

# 1. CONFIGURAÇÃO DOS CAMINHOS
base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(base_dir, 'templates')

print("=" * 50)
print(f"📂 Diretório do projeto: {base_dir}")
print(f"📂 Pasta de templates: {template_dir}")
print("=" * 50)

load_dotenv()  # Carrega variáveis do .env

# 2. CRIAÇÃO DA APLICAÇÃO FLASK
app = Flask(__name__, template_folder=template_dir)

# 3. CONFIGURAÇÃO DO BANCO DE DADOS
DB_PASSWORD = os.getenv('DB_PASSWORD', 'Lucasrt2190')  # Pega do .env ou usa padrão
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{DB_PASSWORD}@localhost:5432/lista_casamento'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'uma-chave-secreta-padrao-123456')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 4. INICIALIZAÇÃO DO BANCO
db.init_app(app)

# 5. ROTAS
@app.route('/')
def index():
    # VERIFICAÇÃO DE DIAGNÓSTICO (IMPORTANTE!)
    template_path = os.path.join(template_dir, 'index.html')
    print(f"\n🔍 ROTA '/' ACESSADA")
    print(f"   Procurando: {template_path}")
    print(f"   Arquivo existe? {os.path.exists(template_path)}")
    
    if not os.path.exists(template_path):
        # Lista o que há na pasta templates
        print(f"   Conteúdo da pasta templates: {os.listdir(template_dir) if os.path.exists(template_dir) else 'Pasta não existe!'}")
        return f"""
        <h1>ERRO: Arquivo index.html não encontrado!</h1>
        <p>Procurando em: <code>{template_path}</code></p>
        <p>Crie o arquivo ou verifique a localização.</p>
        """
    
    return render_template('index.html')

@app.route('/lista')
def ver_lista():
    print(f"\n🔍 ROTA '/lista' ACESSADA")
    itens = ItemLista.query.all()
    print(f"   Itens no banco: {len(itens)}")
    return render_template('lista.html', itens=itens)

@app.route('/reservar/<int:item_id>', methods=['POST'])
def reservar_item(item_id):
    item = ItemLista.query.get_or_404(item_id)
    if not item.reservado:
        convidado_nome = request.form.get('convidado_nome')
        item.reservado = True
        item.reservado_por = convidado_nome
        db.session.commit()
        return jsonify({'success': True, 'message': f'Item "{item.nome}" reservado!'})
    return jsonify({'success': False, 'message': 'Item já foi reservado!'})

# 6. PONTO DE EXECUÇÃO
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("✅ Tabelas do banco verificadas/criadas")
    
    print("\n🚀 Servidor Flask iniciando...")
    app.run(debug=True, port=5000)