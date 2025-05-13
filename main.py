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

import streamlit as st

def aba_calculos():
    st.header("🧮 Cálculos Físico-Matemáticos")

    opcoes = [
        "Velocidade Média",
        "Força Resultante",
        "Fórmula de Bhaskara",
        "Corrente Elétrica",
        "Área de Figuras Geométricas",
        "Força Gravitacional",
        "Torricelli",
        "Carga Elétrica",
        "Tempo"
    ]

    escolha = st.selectbox("Escolha o tipo de cálculo:", opcoes)

    if escolha == "Velocidade Média":
        st.subheader("Velocidade Média: v = Δs / Δt")
        distancia = st.number_input("Digite a distância (Δs) em metros:", step=1.0)
        tempo = st.number_input("Digite o tempo (Δt) em segundos:", step=1.0)
        if st.button("Calcular Velocidade"):
            if tempo != 0:
                velocidade = distancia / tempo
                steps = f"""
                ## Cálculo da Velocidade Média (m/s)
    
                ### Fórmula
    
                $$v = \frac{{\Delta s}}{{\Delta t}}$$
    
                ### Substituindo os valores
    
                $$v = \frac{{{distancia}}}{{{tempo}}}$$
    
                ### Resultado
    
                $$v = {velocidade:.2f} \text{{ m/s}}$$
                """
                st.markdown(steps)
                st.success(f"A velocidade média é {velocidade:.2f} m/s")
            else:
                st.error("O tempo não pode ser zero!")
    
    # Força Resultante
    elif escolha == "Força Resultante":
        st.subheader("Força Resultante: F = m * a")
        massa = st.number_input("Digite a massa (m) em kg:", step=1.0)
        aceleracao = st.number_input("Digite a aceleração (a) em m/s²:", step=1.0)
        if st.button("Calcular Força"):
            forca = massa * aceleracao
            steps = f"""
            ## Cálculo da Força Resultante (N)
    
            ### Fórmula
    
            $$F = m \cdot a$$
    
            ### Substituindo os valores
    
            $$F = {massa} \cdot {aceleracao}$$
    
            ### Resultado
    
            $$F = {forca:.2f} \text{{ N}}$$
            """
            st.markdown(steps)
            st.success(f"A força resultante é {forca:.2f} N")
    
    # Bhaskara
    elif escolha == "Fórmula de Bhaskara":
        st.subheader("Bhaskara: ax² + bx + c = 0")
        a = st.number_input("Digite o valor de a:")
        b = st.number_input("Digite o valor de b:")
        c = st.number_input("Digite o valor de c:")
        if st.button("Calcular Bhaskara"):
            delta = b**2 - 4*a*c
            if delta < 0:
                st.warning("Não existem raízes reais.")
            else:
                x1 = (-b + delta**0.5) / (2*a)
                x2 = (-b - delta**0.5) / (2*a)
                steps = f"""
                ## Cálculo das raízes da equação quadrática
    
                ### Fórmula
    
                $$x = \frac{{-b \pm \sqrt{{\Delta}}}}{{2a}}$$
    
                ### Substituindo os valores
    
                $$\Delta = {b}^2 - 4 \cdot {a} \cdot {c} = {delta}$$
    
                $$x_1 = \frac{{-{b} + \sqrt{{{delta}}}}}{{2 \cdot {a}}} = {x1:.2f}$$
    
                $$x_2 = \frac{{-{b} - \sqrt{{{delta}}}}}{{2 \cdot {a}}} = {x2:.2f}$$
                """
                st.markdown(steps)
                st.success(f"x₁ = {x1:.2f}, x₂ = {x2:.2f}")
    
    # Corrente Elétrica
    elif escolha == "Corrente Elétrica":
        st.subheader("Corrente Elétrica: I = Q / Δt")
        carga = st.number_input("Digite a carga elétrica (Q) em Coulombs:", step=1.0)
        tempo = st.number_input("Digite o tempo (Δt) em segundos:", step=1.0)
        if st.button("Calcular Corrente"):
            if tempo != 0:
                corrente = carga / tempo
                steps = f"""
                ## Cálculo da Corrente Elétrica (A)
    
                ### Fórmula
    
                $$I = \frac{{Q}}{{\Delta t}}$$
    
                ### Substituindo os valores
    
                $$I = \frac{{{carga}}}{{{tempo}}}$$
    
                ### Resultado
    
                $$I = {corrente:.2f} \text{{ A}}$$
                """
                st.markdown(steps)
                st.success(f"A corrente elétrica é {corrente:.2f} A")
            else:
                st.error("O tempo não pode ser zero!")


# ---------------- Autenticação ---------------- #

def login():
    st.subheader("Login")
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        users = load_users()
        for user in users.values():
            if isinstance(user, dict) and user.get("username") == username and check_password(password, user.get("password", "")):
                st.session_state["logged_user"] = user  # Aqui guarda o dicionário inteiro do usuário logado
                st.success("Login bem-sucedido!")
                st.rerun()
                return
        st.error("Usuário ou senha incorretos.")

def register():
    st.subheader("Registrar")
    username = st.text_input("Novo usuário")
    password = st.text_input("Nova senha", type="password")
    if st.button("Registrar"):
        users = load_users()
        if any(user.get("username") == username for user in users.values() if isinstance(user, dict)):
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
        opcao = st.sidebar.selectbox("Escolha a opção", ["Perfil", "Notificações", "Cálculos", "Sair"])
        if opcao == "Perfil":
            show_perfil(st.session_state.logged_user)
        elif opcao == "Notificações":
            show_notificacoes(st.session_state.logged_user)
        elif opcao == "Cálculos":
            aba_calculos()
        elif opcao == "Sair":
            logout()
    else:
        escolha = st.sidebar.radio("Login ou Registro", ["Login", "Registrar"], key="login_registro_radio")
        if escolha == "Login":
            login()
        else:
            register()

if __name__ == "__main__":
    main()
