import streamlit as st
import json
import bcrypt
import uuid
import os

# ===============================
# Configuração Inicial
# ===============================
st.set_page_config(page_title="Sistema de Login", layout="centered")

# ===============================
# Funções Utilitárias
# ===============================
def carregar_usuarios():
    if os.path.exists("users.json"):
        with open("users.json", "r") as f:
            return json.load(f)
    return {}

def salvar_usuarios(usuarios):
    with open("users.json", "w") as f:
        json.dump(usuarios, f, indent=4)

def criar_hash_senha(senha):
    return bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()

def verificar_senha(senha, hash_senha):
    return bcrypt.checkpw(senha.encode(), hash_senha.encode())

# ===============================
# Interface de Registro
# ===============================
def registrar():
    st.title("Criar Conta")
    novo_usuario = st.text_input("Nome de usuário")
    nova_senha = st.text_input("Senha", type="password")
    confirmar_senha = st.text_input("Confirmar senha", type="password")

    if st.button("Registrar"):
        if nova_senha != confirmar_senha:
            st.error("As senhas não coincidem.")
            return

        usuarios = carregar_usuarios()

        if novo_usuario in usuarios:
            st.error("Usuário já existe.")
        else:
            usuarios[novo_usuario] = {
                "id": str(uuid.uuid4()),
                "senha": criar_hash_senha(nova_senha),
                "amigos": [],
                "notificacoes": [],
                "anotacao": ""
            }
            salvar_usuarios(usuarios)
            st.success("Conta criada com sucesso! Faça login.")

# ===============================
# Interface de Login
# ===============================
def login():
    st.title("Login")
    usuario = st.text_input("Nome de usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        usuarios = carregar_usuarios()

        if usuario in usuarios and verificar_senha(senha, usuarios[usuario]["senha"]):
            st.session_state["usuario_logado"] = usuario
            st.success("Login realizado com sucesso!")
            st.rerun()
        else:
            st.error("Usuário ou senha incorretos.")

# ===============================
# Página do Perfil
# ===============================
def mostrar_perfil(usuario):
    usuarios = carregar_usuarios()
    dados = usuarios[usuario]

    st.title("Perfil")
    st.subheader(f"Bem-vindo, {usuario}!")

    st.write("🔑 ID:", dados["id"])

    st.text_area("📝 Anotação pessoal", value=dados.get("anotacao", ""), key="anotacao_input")
    if st.button("Salvar Anotação"):
        dados["anotacao"] = st.session_state.anotacao_input
        usuarios[usuario] = dados
        salvar_usuarios(usuarios)
        st.success("Anotação salva!")

# ===============================
# Página de Notificações
# ===============================
def mostrar_notificacoes(usuario):
    usuarios = carregar_usuarios()
    notificacoes = usuarios[usuario].get("notificacoes", [])

    st.title("Notificações")
    if notificacoes:
        for i, noti in enumerate(notificacoes):
            col1, col2 = st.columns([4, 1])
            col1.write(noti["mensagem"])

            if noti["tipo"] == "convite":
                if col2.button("Aceitar", key=f"aceitar_{i}"):
                    usuarios[usuario]["amigos"].append(noti["de"])
                    usuarios[usuario]["notificacoes"].pop(i)
                    salvar_usuarios(usuarios)
                    st.success(f"Agora você é amigo de {noti['de']}!")
                    st.rerun()
    else:
        st.info("Nenhuma notificação no momento.")

# ===============================
# Página de Amigos
# ===============================
def mostrar_amigos(usuario):
    usuarios = carregar_usuarios()
    amigos = usuarios[usuario].get("amigos", [])

    st.title("Meus Amigos")
    if amigos:
        for amigo in amigos:
            st.write(f"👤 {amigo}")
    else:
        st.info("Você ainda não tem amigos adicionados.")

    st.subheader("🔍 Adicionar amigo por ID")
    id_input = st.text_input("Digite o ID do usuário")
    if st.button("Adicionar amigo"):
        for user, dados in usuarios.items():
            if dados["id"] == id_input:
                if user == usuario:
                    st.warning("Você não pode se adicionar.")
                    return
                if user in usuarios[usuario]["amigos"]:
                    st.info("Este usuário já é seu amigo.")
                    return

                usuarios[user]["notificacoes"].append({
                    "tipo": "convite",
                    "mensagem": f"{usuario} quer ser seu amigo!",
                    "de": usuario
                })
                salvar_usuarios(usuarios)
                st.success("Convite enviado!")
                return

        st.error("Usuário não encontrado.")

# ===============================
# Logout
# ===============================
def logout():
    st.session_state.pop("usuario_logado", None)
    st.success("Logout realizado com sucesso!")
    st.rerun()

# ===============================
# Menu Principal
# ===============================
def menu_principal():
    usuario = st.session_state["usuario_logado"]

    st.sidebar.title("Menu")
    pagina = st.sidebar.selectbox("Ir para:", ["Perfil", "Amigos", "Notificações", "Sair"])

    if pagina == "Perfil":
        mostrar_perfil(usuario)
    elif pagina == "Amigos":
        mostrar_amigos(usuario)
    elif pagina == "Notificações":
        mostrar_notificacoes(usuario)
    elif pagina == "Sair":
        logout()

# ===============================
# Execução Principal
# ===============================
def main():
    if "usuario_logado" not in st.session_state:
        opcoes = ["Login", "Criar Conta"]
        escolha = st.sidebar.selectbox("Menu", opcoes)

        if escolha == "Login":
            login()
        elif escolha == "Criar Conta":
            registrar()
    else:
        menu_principal()

if __name__ == "__main__":
    main()
