import streamlit as st
import math
import matplotlib.pyplot as plt
import bcrypt
import json
import os
from typing import Optional, Tuple, List, Dict, Any

# ==============================================
# CONSTANTES
# ==============================================
K = 9e9  # Constante de Coulomb (N m²/C²)
G = 6.674e-11  # Constante gravitacional (N m²/kg²)
π = 3.14  # Pi
MAX_CURRENT = 10  # Limite de corrente segura (Amperes)

# ==============================================
# FUNÇÕES DE CÁLCULO FÍSICO/MATEMÁTICO
# ==============================================
def calculate_current(charge: float, time: float) -> Tuple[Optional[float], str]:
    """Calcula a intensidade da corrente elétrica."""
    if time <= 0:
        st.error("O tempo deve ser maior que zero.")
        return None, ""
    
    current = charge / time
    
    if current > MAX_CURRENT:
        st.warning("Aviso: A corrente está muito alta! Risco de sobrecarga ou curto-circuito.")
    
    steps = (
        f"\n## Cálculo da Intensidade da Corrente (A)\n"
        f"\n### Fórmula\n"
        f"\n$$I = \\frac{{Q}}{{t}}$$\n"
        f"\n### Substituindo os valores\n"
        f"\n$$I = \\frac{{{charge}}}{{{time}}}$$\n"
        f"\n### Resultado\n"
        f"\n$$I = {current:.2f} \\text{{ A}}$$\n"
    )
    
    _plot_graph(
        x=[0, time], y=[0, current],
        x_label='Tempo (s)', y_label='Corrente (A)',
        title='Gráfico da Intensidade da Corrente',
        filename='current_plot.png'
    )
    
    return current, steps

def calculate_charge(current: float, time: float) -> Tuple[float, str]:
    """Calcula a quantidade de carga elétrica."""
    charge = current * time
    steps = (
        f"\n## Cálculo da Quantidade de Carga (C)\n"
        f"\n### Fórmula\n"
        f"\n$$Q = I \\cdot t$$\n"
        f"\n### Substituindo os valores\n"
        f"\n$$Q = {current} \\cdot {time}$$\n"
        f"\n### Resultado\n"
        f"\n$$Q = {charge:.2f} \\text{{ C}}$$\n"
    )
    
    _plot_graph(
        x=[0, time], y=[0, charge],
        x_label='Tempo (s)', y_label='Carga (C)',
        title='Gráfico da Quantidade de Carga',
        filename='charge_plot.png'
    )
    
    return charge, steps

def calculate_time(current: float, charge: float) -> Tuple[Optional[float], str]:
    """Calcula o tempo a partir da corrente e carga."""
    if current <= 0:
        st.error("A corrente deve ser maior que zero.")
        return None, ""
    
    time = charge / current
    steps = (
        f"\n## Cálculo do Tempo (s)\n"
        f"\n### Fórmula\n"
        f"\n$$t = \\frac{{Q}}{{I}}$$\n"
        f"\n### Substituindo os valores\n"
        f"\n$$t = \\frac{{{charge}}}{{{current}}}$$\n"
        f"\n### Resultado\n"
        f"\n$$t = {time:.2f} \\text{{ s}}$$\n"
    )
    
    _plot_graph(
        x=[0, current], y=[0, time],
        x_label='Corrente (A)', y_label='Tempo (s)',
        title='Gráfico do Tempo',
        filename='time_plot.png'
    )
    
    return time, steps

def calculate_gravitational_force(mass1: float, mass2: float, distance: float) -> Tuple[Optional[float], str]:
    """Calcula a força gravitacional entre duas massas."""
    if distance <= 0:
        st.error("A distância deve ser maior que zero.")
        return None, ""
    
    force = G * mass1 * mass2 / distance**2
    steps = (
        f"\n## Cálculo da Força da Gravitação Universal (N)\n"
        f"\n### Fórmula\n"
        f"\n$$F = \\frac{{G \\cdot m1 \\cdot m2}}{{d^2}}$$\n"
        f"\n### Substituindo os valores\n"
        f"\n$$F = \\frac{{{G} \\cdot {mass1} \\cdot {mass2}}}{{{distance}^2}}$$\n"
        f"\n### Resultado\n"
        f"\n$$F = {force:.2e} \\text{{ N}}$$\n"
    )
    
    distance_vals = list(range(1, 11))
    force_vals = [G * mass1 * mass2 / (d**2) for d in distance_vals]
    
    _plot_graph(
        x=distance_vals, y=force_vals,
        x_label='Distância (m)', y_label='Força (N)',
        title='Gráfico da Força da Gravitação Universal',
        filename='gravitational_force_plot.png'
    )
    
    return force, steps

# ==============================================
# FUNÇÕES AUXILIARES
# ==============================================
def _plot_graph(x: List[float], y: List[float], x_label: str, y_label: str, 
               title: str, filename: str) -> None:
    """Função auxiliar para plotar gráficos."""
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, marker='o')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(True)
    plt.savefig(filename)
    plt.close()

# ==============================================
# FUNÇÕES DE AUTENTICAÇÃO E USUÁRIO
# ==============================================
def load_users() -> Dict[str, Any]:
    """Carrega os usuários do arquivo JSON."""
    if not os.path.exists('users.json') or os.stat('users.json').st_size == 0:
        return {}
    with open('users.json', 'r') as f:
        return json.load(f)

def save_users(users: Dict[str, Any]) -> None:
    """Salva os usuários no arquivo JSON."""
    with open('users.json', 'w') as f:
        json.dump(users, f, indent=4)

def verify_login(username: str, password: str) -> bool:
    """Verifica as credenciais de login."""    
    users = load_users()
    if username in users:
        hashed_password = users[username]['password']
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
    return False

def register_user(username: str, password: str) -> bool:
    """Registra um novo usuário."""    
    users = load_users()
    if username in users:
        return False
    
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    users[username] = {
        'password': hashed_password.decode('utf-8'),
        'friends': []
    }
    save_users(users)
    return True

# ==============================================
# FUNÇÕES DE INTERFACE
# ==============================================
def auth_page() -> None:
    """Página de autenticação (login/registro)."""
    st.title("Login ou Registro")
    option = st.radio("Escolha uma opção:", ("Login", "Registrar"))

    if option == "Login":
        _login_section()
    elif option == "Registrar":
        _register_section()

def _login_section() -> None:
    """Seção de login."""
    st.subheader("Login")
    username = st.text_input("Nome de Usuário (Login)", key='login_user')
    password = st.text_input("Senha (Login)", type='password', key='login_pass')
    
    if st.button("Entrar"):
        if verify_login(username, password):
            st.session_state.update({
                'logged_in': True,
                'username': username,
                'page': 'main'
            })
        else:
            st.error("Nome de usuário ou senha incorretos.")

def _register_section() -> None:
    """Seção de registro."""    
    st.subheader("Registro")
    username = st.text_input("Nome de Usuário (Registro)", key='register_user')
    password = st.text_input("Senha (Registro)", type='password', key='register_pass')
    confirm_password = st.text_input("Confirmar Senha", type='password', key='register_pass_confirm')
    
    if st.button("Registrar"):
        if password != confirm_password:
            st.error("As senhas não coincidem.")
        elif register_user(username, password):
            st.success("Registro bem-sucedido! Agora você pode fazer login.")
            st.session_state['page'] = 'main'
        else:
            st.error("Nome de usuário já existe.")

# ==============================================
# FUNÇÃO PRINCIPAL
# ==============================================
def main_page() -> None:
    """Página principal após o login."""
    if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
        st.error("Você precisa fazer login primeiro.")
        return
    
    st.title(f"Bem-vindo, {st.session_state['username']}!")
    st.write("Escolha uma operação física ou matemática para calcular.")
    
    option = st.selectbox("Selecione um cálculo", ("Calcular Corrente", "Calcular Carga", "Calcular Tempo", "Calcular Força Gravitacional"))

    if option == "Calcular Corrente":
        charge = st.number_input("Carga (C)", min_value=0.0)
        time = st.number_input("Tempo (s)", min_value=0.01)
        if st.button("Calcular"):
            current, steps = calculate_current(charge, time)
            if current is not None:
                st.markdown(steps)
                st.image("current_plot.png")
    
    elif option == "Calcular Carga":
        current = st.number_input("Corrente (A)", min_value=0.0)
        time = st.number_input("Tempo (s)", min_value=0.01)
        if st.button("Calcular"):
            charge, steps = calculate_charge(current, time)
            st.markdown(steps)
            st.image("charge_plot.png")

    elif option == "Calcular Tempo":
        current = st.number_input("Corrente (A)", min_value=0.0)
        charge = st.number_input("Carga (C)", min_value=0.0)
        if st.button("Calcular"):
            time, steps = calculate_time(current, charge)
            st.markdown(steps)
            st.image("time_plot.png")
    
    elif option == "Calcular Força Gravitacional":
        mass1 = st.number_input("Massa 1 (kg)", min_value=0.0)
        mass2 = st.number_input("Massa 2 (kg)", min_value=0.0)
        distance = st.number_input("Distância (m)", min_value=0.01)
        if st.button("Calcular"):
            force, steps = calculate_gravitational_force(mass1, mass2, distance)
            st.markdown(steps)
            st.image("gravitational_force_plot.png")

# Função principal
def main() -> None:
    """Função principal da aplicação."""
    if 'page' not in st.session_state:
        st.session_state['page'] = 'auth'
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if st.session_state['page'] == 'auth':
        auth_page()
    elif st.session_state['logged_in']:
        main_page()

if __name__ == "__main__":
    main()
