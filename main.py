import streamlit as st
import json
import uuid
import bcrypt
import os

# Carrega ou cria arquivo de dados
if not os.path.exists("users.json"):
    with open("users.json", "w") as f:
        json.dump({}, f)

def load_users():
    with open("users.json", "r") as f:
        return json.load(f)

def save_users(users):
    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode())

# ---------------- Funções de cálculo ---------------- #

def calcular_velocidade_media(distancia, tempo):
    if tempo == 0:
        return "Tempo não pode ser zero."
    return distancia / tempo

def calcular_forca_resultante(massa, aceleracao):
    return massa * aceleracao

def calcular_bhaskara(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return "Sem raízes reais."
    elif delta == 0:
        x = -b / (2 * a)
        return f"Raiz única: x = {x}"
    else:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        return f"x₁ = {x1}, x₂ = {x2}"

# ---------------- Autenticação ---------------- #

def login():
    st.subheader("Login")
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        users = load_users()
        for user in users.values():
            if user["username"] == username and check_password(password, user["password"]):
                st.session_state.logged_user = user
                st.success("Login bem-sucedido!")
                st.rerun()
        st.error("Usuário ou senha inválidos.")

def register():
    st.subheader("Registrar")
    username = st.text_input("Novo usuário")
    password = st.text_input("Nova senha", type="password")
    if st.button("Registrar"):
        users = load_users()
        if any(user["username"] == username for user in users.values()):
            st.error("Usuário já existe.")
        else:
            user_id = str(uuid.uuid4())
            users[user_id] = {
                "id": user_id,
                "username": username,
                "password": hash_password(password),
                "amigos": [],
                "notificacoes": [],
                "anotacao": ""
            }
            save_users(users)
            st.success("Registrado com sucesso! Faça login.")

def logout():
    if st.button("Sair"):
        st.session_state.logged_user = None
        st.rerun()

# ---------------- Interface ---------------- #

def show_perfil(user):
    st.title(f"Perfil: {user['username']}")

    # Anotação
    anotacao = st.text_area("Anotação pessoal:", value=user.get("anotacao", ""))
    if st.button("Salvar anotação"):
        users = load_users()
        users[user["id"]]["anotacao"] = anotacao
        save_users(users)
        st.success("Anotação salva!")

    # Amigos
    st.subheader("Amigos:")
    if user["amigos"]:
        for amigo_id in user["amigos"]:
            users = load_users()
            amigo_nome = users.get(amigo_id, {}).get("username", "Desconhecido")
            st.text(f"- {amigo_nome}")
    else:
        st.info("Nenhum amigo adicionado.")

    # Buscar amigo
    st.subheader("Buscar usuário por ID")
    search_id = st.text_input("ID do usuário")
    if st.button("Enviar pedido de amizade"):
        users = load_users()
        if search_id in users and search_id != user["id"]:
            if user["id"] not in users[search_id]["notificacoes"]:
                users[search_id]["notificacoes"].append(user["id"])
                save_users(users)
                st.success("Pedido de amizade enviado!")
            else:
                st.warning("Você já enviou um pedido para este usuário.")
        else:
            st.error("ID de usuário inválido.")

def show_notificacoes(user):
    st.title("Notificações")
    users = load_users()
    if not user["notificacoes"]:
        st.info("Sem notificações.")
    else:
        for solicitante_id in user["notificacoes"]:
            nome = users.get(solicitante_id, {}).get("username", "Desconhecido")
            col1, col2 = st.columns(2)
            col1.write(f"{nome} quer ser seu amigo.")
            if col2.button("Aceitar", key=solicitante_id):
                users[user["id"]]["amigos"].append(solicitante_id)
                users[solicitante_id]["amigos"].append(user["id"])
                users[user["id"]]["notificacoes"].remove(solicitante_id)
                save_users(users)
                st.success(f"Você e {nome} agora são amigos!")
                st.rerun()

def show_calculos():
    st.title("Calculadora Física")

    with st.expander("Velocidade Média"):
        d = st.number_input("Distância (m)", key="d_vm")
        t = st.number_input("Tempo (s)", key="t_vm")
        if st.button("Calcular Velocidade Média"):
            resultado = calcular_velocidade_media(d, t)
            st.success(f"Velocidade Média = {resultado} m/s")

    with st.expander("Força Resultante"):
        m = st.number_input("Massa (kg)", key="m_fr")
        a = st.number_input("Aceleração (m/s²)", key="a_fr")
        if st.button("Calcular Força Resultante"):
            resultado = calcular_forca_resultante(m, a)
            st.success(f"Força Resultante = {resultado} N")

    with st.expander("Bhaskara"):
        a = st.number_input("a", key="a_bh")
        b = st.number_input("b", key="b_bh")
        c = st.number_input("c", key="c_bh")
        if st.button("Calcular Bhaskara"):
            resultado = calcular_bhaskara(a, b, c)
            st.success(f"Resultado: {resultado}")

# ---------------- Execução Principal ---------------- #

def main():
    st.sidebar.title("Menu")
    if "logged_user" not in st.session_state:
        st.session_state.logged_user = None

    if st.session_state.logged_user:
        page = st.sidebar.selectbox("Ir para:", ["Perfil", "Notificações", "Cálculos", "Sair"])
        if page == "Perfil":
            show_perfil(st.session_state.logged_user)
        elif page == "Notificações":
            show_notificacoes(st.session_state.logged_user)
        elif page == "Cálculos":
            show_calculos()
        elif page == "Sair":
            logout()
    else:
        menu = st.sidebar.radio("Menu", ["Login", "Registrar"])
        if menu == "Login":
            login()
        elif menu == "Registrar":
            register()

if __name__ == "__main__":
    main()
