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
                # Exibição do cálculo passo a passo
                steps = f"\n## Cálculo da Velocidade Média (m/s)\n" \
                        f"\n### Fórmula\n" \
                        f"\n$$v = \\frac{{\\Delta s}}{{\\Delta t}}$$\n" \
                        f"\n### Substituindo os valores\n" \
                        f"\n$$v = \\frac{{{distancia}}}{{{tempo}}}$$\n" \
                        f"\n### Resultado\n" \
                        f"\n$$v = {velocidade:.2f} \\text{{ m/s}}$$\n"
                st.markdown(steps)
                st.success(f"A velocidade média é {velocidade:.2f} m/s")
            else:
                st.error("O tempo não pode ser zero!")

    elif escolha == "Força Resultante":
        st.subheader("Força Resultante: F = m * a")
        massa = st.number_input("Digite a massa (m) em kg:", step=1.0)
        aceleracao = st.number_input("Digite a aceleração (a) em m/s²:", step=1.0)
        if st.button("Calcular Força"):
            forca = massa * aceleracao
            steps = f"\n## Cálculo da Força Resultante (N)\n" \
                    f"\n### Fórmula\n" \
                    f"\n$$F = m \\times a$$\n" \
                    f"\n### Substituindo os valores\n" \
                    f"\n$$F = {massa} \\times {aceleracao}$$\n" \
                    f"\n### Resultado\n" \
                    f"\n$$F = {forca:.2f} \\text{{ N}}$$\n"
            st.markdown(steps)
            st.success(f"A força resultante é {forca:.2f} N")

    elif escolha == "Fórmula de Bhaskara":
        st.subheader("Bhaskara: ax² + bx + c = 0")
        a = st.number_input("Digite o valor de a:")
        b = st.number_input("Digite o valor de b:")
        c = st.number_input("Digite o valor de c:")
        if st.button("Calcular Bhaskara"):
            delta = b**2 - 4*a*c
            steps = f"\n## Cálculo das Raízes pela Fórmula de Bhaskara\n" \
                    f"\n### Fórmula\n" \
                    f"\n$$x = \\frac{{-b \\pm \\sqrt{{b^2 - 4ac}}}}{{2a}}$$\n" \
                    f"\n### Cálculo do Discriminante (Δ)\n" \
                    f"\n$$\\Delta = b^2 - 4ac$$\n" \
                    f"\n$$\\Delta = {b}^2 - 4 \\times {a} \\times {c}$$\n" \
                    f"\n$$\\Delta = {delta:.2f}$$\n"
            
            if delta < 0:
                steps += f"\n### Resultado\n" \
                         f"\nNão existem raízes reais (Δ < 0)\n"
                st.markdown(steps)
                st.warning("Não existem raízes reais.")
            else:
                x1 = (-b + delta**0.5) / (2*a)
                x2 = (-b - delta**0.5) / (2*a)
                steps += f"\n### Cálculo das Raízes\n" \
                         f"\n$$x_1 = \\frac{{-b + \\sqrt{{\\Delta}}}}{{2a}} = \\frac{{-{b} + \\sqrt{{{delta:.2f}}}}}{{2 \\times {a}}} = {x1:.2f}$$\n" \
                         f"\n$$x_2 = \\frac{{-b - \\sqrt{{\\Delta}}}}{{2a}} = \\frac{{-{b} - \\sqrt{{{delta:.2f}}}}}{{2 \\times {a}}} = {x2:.2f}$$\n" \
                         f"\n### Resultado\n" \
                         f"\n$$x_1 = {x1:.2f}$$\n" \
                         f"\n$$x_2 = {x2:.2f}$$\n"
                st.markdown(steps)
                st.success(f"x₁ = {x1:.2f}, x₂ = {x2:.2f}")

    elif escolha == "Corrente Elétrica":
        st.subheader("Corrente Elétrica: I = Q / Δt")
        carga = st.number_input("Digite a carga elétrica (Q) em Coulombs:", step=1.0)
        tempo = st.number_input("Digite o tempo (Δt) em segundos:", step=1.0)
        if st.button("Calcular Corrente"):
            if tempo != 0:
                corrente = carga / tempo
                steps = f"\n## Cálculo da Corrente Elétrica (A)\n" \
                        f"\n### Fórmula\n" \
                        f"\n$$I = \\frac{{Q}}{{\\Delta t}}$$\n" \
                        f"\n### Substituindo os valores\n" \
                        f"\n$$I = \\frac{{{carga}}}{{{tempo}}}$$\n" \
                        f"\n### Resultado\n" \
                        f"\n$$I = {corrente:.2f} \\text{{ A}}$$\n"
                st.markdown(steps)
                st.success(f"A corrente elétrica é {corrente:.2f} A")
            else:
                st.error("O tempo não pode ser zero!")

    elif escolha == "Área de Figuras Geométricas":
        figura = st.selectbox("Escolha a figura:", ["Quadrado", "Retângulo", "Triângulo", "Círculo"])
        if figura == "Quadrado":
            lado = st.number_input("Digite o lado:", step=1.0)
            if st.button("Calcular Área do Quadrado"):
                area = lado ** 2
                steps = f"\n## Cálculo da Área do Quadrado\n" \
                        f"\n### Fórmula\n" \
                        f"\n$$A = lado^2$$\n" \
                        f"\n### Substituindo os valores\n" \
                        f"\n$$A = {lado}^2$$\n" \
                        f"\n### Resultado\n" \
                        f"\n$$A = {area:.2f}$$\n"
                st.markdown(steps)
                st.success(f"A área é {area:.2f}")
        elif figura == "Retângulo":
            base = st.number_input("Base:", step=1.0)
            altura = st.number_input("Altura:", step=1.0)
            if st.button("Calcular Área do Retângulo"):
                area = base * altura
                steps = f"\n## Cálculo da Área do Retângulo\n" \
                        f"\n### Fórmula\n" \
                        f"\n$$A = base \\times altura$$\n" \
                        f"\n### Substituindo os valores\n" \
                        f"\n$$A = {base} \\times {altura}$$\n" \
                        f"\n### Resultado\n" \
                        f"\n$$A = {area:.2f}$$\n"
                st.markdown(steps)
                st.success(f"A área é {area:.2f}")
        elif figura == "Triângulo":
            base = st.number_input("Base:", step=1.0)
            altura = st.number_input("Altura:", step=1.0)
            if st.button("Calcular Área do Triângulo"):
                area = (base * altura) / 2
                steps = f"\n## Cálculo da Área do Triângulo\n" \
                        f"\n### Fórmula\n" \
                        f"\n$$A = \\frac{{base \\times altura}}{{2}}$$\n" \
                        f"\n### Substituindo os valores\n" \
                        f"\n$$A = \\frac{{{base} \\times {altura}}}{{2}}$$\n" \
                        f"\n### Resultado\n" \
                        f"\n$$A = {area:.2f}$$\n"
                st.markdown(steps)
                st.success(f"A área é {area:.2f}")
        elif figura == "Círculo":
            raio = st.number_input("Raio:", step=1.0)
            if st.button("Calcular Área do Círculo"):
                area = 3.1416 * raio ** 2
                steps = f"\n## Cálculo da Área do Círculo\n" \
                        f"\n### Fórmula\n" \
                        f"\n$$A = \\pi \\times raio^2$$\n" \
                        f"\n### Substituindo os valores\n" \
                        f"\n$$A = 3.1416 \\times {raio}^2$$\n" \
                        f"\n### Resultado\n" \
                        f"\n$$A = {area:.2f}$$\n"
                st.markdown(steps)
                st.success(f"A área é {area:.2f}")

    elif escolha == "Força Gravitacional":
        st.subheader("Força Gravitacional: F = G * (m1 * m2) / d²")
        G = 6.67430e-11
        m1 = st.number_input("Massa 1 (kg):", step=1.0)
        m2 = st.number_input("Massa 2 (kg):", step=1.0)
        distancia = st.number_input("Distância (m):", step=1.0)
        if st.button("Calcular Força Gravitacional"):
            if distancia != 0:
                Fg = G * (m1 * m2) / distancia**2
                steps = f"\n## Cálculo da Força Gravitacional (N)\n" \
                        f"\n### Fórmula\n" \
                        f"\n$$F = G \\times \\frac{{m_1 \\times m_2}}{{d^2}}$$\n" \
                        f"\n### Constante Gravitacional\n" \
                        f"\n$$G = 6.67430 \\times 10^{{-11}} \\text{{ Nm}}^2/\\text{{kg}}^2$$\n" \
                        f"\n### Substituindo os valores\n" \
                        f"\n$$F = 6.67430 \\times 10^{{-11}} \\times \\frac{{{m1} \\times {m2}}}{{{distancia}^2}}$$\n" \
                        f"\n### Resultado\n" \
                        f"\n$$F = {Fg:.4e} \\text{{ N}}$$\n"
                st.markdown(steps)
                st.success(f"A força gravitacional é {Fg:.4e} N")
            else:
                st.error("A distância não pode ser zero!")

    elif escolha == "Torricelli":
        st.subheader("Torricelli: v² = v₀² + 2*a*Δs")
        v0 = st.number_input("Velocidade inicial (v₀):", step=1.0)
        a = st.number_input("Aceleração (a):", step=1.0)
        s = st.number_input("Deslocamento (Δs):", step=1.0)
        if st.button("Calcular Velocidade Final"):
            vf2 = v0**2 + 2*a*s
            if vf2 >= 0:
                vf = vf2 ** 0.5
                steps = f"\n## Cálculo da Velocidade Final (Torricelli)\n" \
                        f"\n### Fórmula\n" \
                        f"\n$$v^2 = v_0^2 + 2 \\times a \\times \\Delta s$$\n" \
                        f"\n### Substituindo os valores\n" \
                        f"\n$$v^2 = {v0}^2 + 2 \\times {a} \\times {s}$$\n" \
                        f"\n$$v^2 = {v0**2:.2f} + {2*a*s:.2f}$$\n" \
                        f"\n$$v^2 = {vf2:.2f}$$\n" \
                        f"\n$$v = \\sqrt{{{vf2:.2f}}}$$\n" \
                        f"\n### Resultado\n" \
                        f"\n$$v = {vf:.2f} \\text{{ m/s}}$$\n"
                st.markdown(steps)
                st.success(f"A velocidade final é {vf:.2f} m/s")
            else:
                steps = f"\n## Cálculo da Velocidade Final (Torricelli)\n" \
                        f"\n### Fórmula\n" \
                        f"\n$$v^2 = v_0^2 + 2 \\times a \\times \\Delta s$$\n" \
                        f"\n### Substituindo os valores\n" \
                        f"\n$$v^2 = {v0}^2 + 2 \\times {a} \\times {s}$$\n" \
                        f"\n$$v^2 = {v0**2:.2f} + {2*a*s:.2f}$$\n" \
                        f"\n$$v^2 = {vf2:.2f}$$\n" \
                        f"\n### Resultado\n" \
                        f"\nNão existe solução real (raiz quadrada de número negativo)\n"
                st.markdown(steps)
                st.warning("Resultado inválido (velocidade imaginária).")

    elif escolha == "Carga Elétrica":
        st.subheader("Carga Elétrica: Q = n * e")
        n = st.number_input("Número de elétrons (n):", step=1.0)
        e = 1.6e-19  # Carga elementar
        if st.button("Calcular Carga"):
            Q = n * e
            steps = f"\n## Cálculo da Carga Elétrica (C)\n" \
                    f"\n### Fórmula\n" \
                    f"\n$$Q = n \\times e$$\n" \
                    f"\n### Carga Elementar\n" \
                    f"\n$$e = 1.6 \\times 10^{{-19}} \\text{{ C}}$$\n" \
                    f"\n### Substituindo os valores\n" \
                    f"\n$$Q = {n} \\times 1.6 \\times 10^{{-19}}$$\n" \
                    f"\n### Resultado\n" \
                    f"\n$$Q = {Q:.4e} \\text{{ C}}$$\n"
            st.markdown(steps)
            st.success(f"A carga elétrica é {Q:.4e} C")

    elif escolha == "Tempo":
        st.subheader("Tempo: t = d / v")
        d = st.number_input("Distância (d):", step=1.0)
        v = st.number_input("Velocidade (v):", step=1.0)
        if st.button("Calcular Tempo"):
            if v != 0:
                t = d / v
                steps = f"\n## Cálculo do Tempo (s)\n" \
                        f"\n### Fórmula\n" \
                        f"\n$$t = \\frac{{d}}{{v}}$$\n" \
                        f"\n### Substituindo os valores\n" \
                        f"\n$$t = \\frac{{{d}}}{{{v}}}$$\n" \
                        f"\n### Resultado\n" \
                        f"\n$$t = {t:.2f} \\text{{ s}}$$\n"
                st.markdown(steps)
                st.success(f"O tempo é {t:.2f} s")
            else:
                st.error("A velocidade não pode ser zero!")


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

def show_notificacoes(logged_user):
    st.subheader("Notificações")
    
    # Carrega todos os usuários
    users = load_users()
    
    # Verifica se o usuário logado existe no sistema
    if logged_user["id"] not in users:
        st.error("Erro: seu usuário não foi encontrado no sistema!")
        return
    
    user = users[logged_user["id"]]
    
    # Garante que o usuário tem a lista de notificações
    if "notificacoes" not in user:
        user["notificacoes"] = []
    
    # Verifica se há notificações
    if not user["notificacoes"]:
        st.info("Você não tem notificações no momento.")
        return
    
    # Processa cada notificação
    for solicitante_id in user["notificacoes"].copy():  # Usamos copy() para iterar sobre uma cópia
        if solicitante_id not in users:
            # Remove IDs inválidos
            user["notificacoes"].remove(solicitante_id)
            continue
            
        solicitante = users[solicitante_id]
        st.markdown(f"**{solicitante['username']}** quer ser seu amigo.")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"Aceitar {solicitante['username']}", key=f"aceitar_{solicitante_id}"):
                # Adiciona como amigo em ambos os usuários
                if "amigos" not in user:
                    user["amigos"] = []
                if "amigos" not in solicitante:
                    solicitante["amigos"] = []
                
                if solicitante_id not in user["amigos"]:
                    user["amigos"].append(solicitante_id)
                if user["id"] not in solicitante["amigos"]:
                    solicitante["amigos"].append(user["id"])
                
                # Remove a notificação
                user["notificacoes"].remove(solicitante_id)
                save_users(users)
                st.success(f"Você e {solicitante['username']} agora são amigos!")
                st.rerun()
        
        with col2:
            if st.button(f"Recusar {solicitante['username']}", key=f"recusar_{solicitante_id}"):
                user["notificacoes"].remove(solicitante_id)
                save_users(users)
                st.info(f"Pedido de {solicitante['username']} recusado.")
                st.rerun()

def show_perfil(user):
    st.title(f"Perfil: {user['username']}")
    st.subheader(f"ID: {user['id']}")
    
    # Anotações
    anotacao = st.text_area("Anotação pessoal:", value=user.get("anotacao", ""))
    if st.button("Salvar anotação"):
        users = load_users()
        users[user["id"]]["anotacao"] = anotacao
        save_users(users)
        st.success("Anotação salva!")

    # Amigos
    st.subheader("Amigos:")
    if "amigos" in user and user["amigos"]:
        users = load_users()
        for amigo_id in user["amigos"]:
            if amigo_id in users:
                st.write(f"- {users[amigo_id]['username']}")
            else:
                st.write(f"- Usuário desconhecido (ID: {amigo_id})")
    else:
        st.info("Nenhum amigo adicionado.")

    # Buscar amigo
    st.subheader("Buscar usuário por ID")
    search_id = st.text_input("ID do usuário")
    if st.button("Enviar pedido de amizade"):
        users = load_users()
        
        if not search_id:
            st.error("Por favor, insira um ID válido")
        elif search_id == user["id"]:
            st.error("Você não pode adicionar a si mesmo como amigo")
        elif search_id not in users:
            st.error("ID de usuário não encontrado")
        else:
            target_user = users[search_id]
            
            # Inicializa notificações se não existirem
            if "notificacoes" not in target_user:
                target_user["notificacoes"] = []
            
            # Verifica se já existe um pedido pendente
            if user["id"] in target_user["notificacoes"]:
                st.warning("Você já enviou um pedido para este usuário")
            else:
                target_user["notificacoes"].append(user["id"])
                save_users(users)
                st.success("Pedido de amizade enviado com sucesso!")



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
