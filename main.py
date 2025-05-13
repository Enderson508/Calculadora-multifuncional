import streamlit as st
import math
import matplotlib.pyplot as plt
import bcrypt
import json
import os
from typing import Optional, Tuple, List, Dict, Any

# ==============================================
# CONSTANTES E CONFIGURAÇÕES
# ==============================================

# Constantes físicas
K = 9e9  # Constante de Coulomb (N m²/C²)
G = 6.674e-11  # Constante gravitacional (N m²/kg²)
π = 3.14
MAX_CURRENT = 10  # Limite de corrente segura (Amperes)

# Configurações de arquivos
DATA_FILES = {
    'users': 'users.json',
    'messages': 'messages.json',
    'notifications': 'notifications.json'
}

# ==============================================
# FUNÇÕES AUXILIARES
# ==============================================

def load_data(file_key: str) -> Any:
    """Carrega dados de um arquivo JSON."""
    file_path = DATA_FILES[file_key]
    if not os.path.exists(file_path) or os.stat(file_path).st_size == 0:
        return {} if file_key in ['users', 'messages'] else []
    
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            # Converter chaves de string para tupla quando necessário
            if file_key == 'messages':
                return {tuple(eval(key)): value for key, value in data.items()}
            return data
    except (json.JSONDecodeError, SyntaxError):
        return {} if file_key in ['users', 'messages'] else []

def save_data(file_key: str, data: Any) -> None:
    """Salva dados em um arquivo JSON."""
    file_path = DATA_FILES[file_key]
    try:
        # Converter chaves de tupla para string quando necessário
        if file_key == 'messages':
            data = {str(key): value for key, value in data.items()}
        
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
    except TypeError as e:
        st.error(f"Erro ao salvar dados: {str(e)}")

def plot_graph(x: List[float], y: List[float], x_label: str, y_label: str, 
               title: str, filename: str, scatter: bool = False) -> None:
    """Gera e salva um gráfico."""
    plt.figure(figsize=(10, 5))
    if scatter:
        plt.scatter(x, y)
    else:
        plt.plot(x, y, marker='o')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(True)
    plt.savefig(filename)
    plt.close()

# ==============================================
# FUNÇÕES DE CÁLCULO CIENTÍFICO
# ==============================================

def calculate_current(charge: float, time: float) -> Tuple[Optional[float], str]:
    """Calcula a intensidade da corrente elétrica."""
    if time <= 0:
        st.error("O tempo deve ser maior que zero.")
        return None, ""
    
    current = charge / time
    
    if current > MAX_CURRENT:
        st.warning("Aviso: Corrente acima do limite seguro!")
    
    steps = (
        f"## Cálculo da Intensidade da Corrente (A)\n"
        f"### Fórmula\n$$I = \\frac{{Q}}{{t}}$$\n"
        f"### Substituição\n$$I = \\frac{{{charge}}}{{{time}}}$$\n"
        f"### Resultado\n$$I = {current:.2f} \\text{{ A}}$$\n"
    )
    
    plot_graph([0, time], [0, current], 'Tempo (s)', 'Corrente (A)', 
              'Variação da Corrente', 'current_plot.png')
    
    return current, steps

def calculate_gravitational_force(mass1: float, mass2: float, distance: float) -> Tuple[Optional[float], str]:
    """Calcula a força gravitacional entre duas massas."""
    if distance <= 0:
        st.error("A distância deve ser maior que zero.")
        return None, ""
    
    force = G * mass1 * mass2 / distance**2
    steps = (
        f"## Cálculo da Força Gravitacional (N)\n"
        f"### Fórmula\n$$F = \\frac{{G \\cdot m1 \\cdot m2}}{{d^2}}$$\n"
        f"### Substituição\n$$F = \\frac{{{G:.3e} \\cdot {mass1} \\cdot {mass2}}}{{{distance}^2}}$$\n"
        f"### Resultado\n$$F = {force:.3e} \\text{{ N}}$$\n"
    )
    
    distances = list(range(1, 11))
    forces = [G * mass1 * mass2 / (d**2) for d in distances]
    
    plot_graph(distances, forces, 'Distância (m)', 'Força (N)',
              'Força Gravitacional vs Distância', 'gravitational_force_plot.png')
    
    return force, steps

def bhaskara(a: float, b: float, c: float) -> Tuple[Tuple[Optional[float], Optional[float]], str]:
    """Calcula raízes de equação quadrática."""
    delta = b**2 - 4*a*c
    steps = (
        f"## Cálculo das Raízes (Bhaskara)\n"
        f"### Delta\n$$\\Delta = {b}^2 - 4 \\cdot {a} \\cdot {c} = {delta:.2f}$$\n"
    )
    
    if delta < 0:
        steps += "### Não existem raízes reais (Δ < 0)"
        return (None, None), steps
    
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    
    steps += (
        f"### Raízes\n"
        f"$$x_1 = \\frac{{-({b}) + \\sqrt{{{delta:.2f}}}}{{2 \\cdot {a}}} = {x1:.2f}$$\n"
        f"$$x_2 = \\frac{{-({b}) - \\sqrt{{{delta:.2f}}}}{{2 \\cdot {a}}} = {x2:.2f}$$\n"
    )
    
    plot_graph([x1, x2], [0, 0], 'x', 'f(x)', 'Raízes da Equação', 
              'bhaskara_plot.png', scatter=True)
    
    return (x1, x2), steps

# (Outras funções de cálculo seguindo o mesmo padrão...)

# ==============================================
# FUNÇÕES DE GERENCIAMENTO DE USUÁRIOS
# ==============================================

def verify_login(username: str, password: str) -> bool:
    """Verifica credenciais de login."""
    users = load_data('users')
    if username in users:
        hashed = users[username]['password']
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
    return False

def register_user(username: str, password: str) -> bool:
    """Registra um novo usuário."""
    users = load_data('users')
    if username in users:
        return False
    
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    users[username] = {
        'password': hashed.decode('utf-8'),
        'friends': []
    }
    save_data('users', users)
    return True

# ==============================================
# FUNÇÕES DE INTERAÇÃO SOCIAL
# ==============================================

def send_friend_request(sender: str, receiver: str) -> None:
    """Envia solicitação de amizade."""
    notifications = load_data('notifications')
    notifications.append({
        'to': receiver,
        'message': {
            'type': 'friend_request',
            'from': sender,
            'timestamp': str(datetime.now())
        }
    })
    save_data('notifications', notifications)

def accept_friend_request(requester: str, accepter: str) -> None:
    """Aceita uma solicitação de amizade."""
    users = load_data('users')
    
    # Adiciona amigo mutuamente
    users[accepter].setdefault('friends', []).append(requester)
    users[requester].setdefault('friends', []).append(accepter)
    
    save_data('users', users)
    remove_notification(accepter, requester)

def remove_notification(username: str, from_user: str) -> None:
    """Remove uma notificação específica."""
    notifications = load_data('notifications')
    notifications = [n for n in notifications if not (
        n['to'] == username and 
        n['message']['from'] == from_user
    )]
    save_data('notifications', notifications)

# ==============================================
# INTERFACES DE USUÁRIO
# ==============================================

def auth_page() -> None:
    """Página de autenticação."""
    st.title("🔐 Login / Registro")
    tab1, tab2 = st.tabs(["Login", "Registro"])

    with tab1:
        with st.form("login_form"):
            username = st.text_input("Usuário")
            password = st.text_input("Senha", type="password")
            
            if st.form_submit_button("Entrar"):
                if verify_login(username, password):
                    st.session_state.update({
                        'logged_in': True,
                        'username': username,
                        'page': 'main'
                    })
                    st.rerun()
                else:
                    st.error("Credenciais inválidas")

    with tab2:
        with st.form("register_form"):
            new_user = st.text_input("Novo usuário")
            new_pass = st.text_input("Senha", type="password")
            confirm_pass = st.text_input("Confirmar senha", type="password")
            
            if st.form_submit_button("Registrar"):
                if new_pass != confirm_pass:
                    st.error("Senhas não coincidem")
                elif register_user(new_user, new_pass):
                    st.success("Registro realizado! Faça login.")
                else:
                    st.error("Usuário já existe")

def main_page() -> None:
    """Página principal da aplicação."""
    st.title("🧪 Calculadora Científica Plus")
    current_user = st.session_state.get('username', '')
    
    # Sidebar com funcionalidades sociais
    with st.sidebar:
        st.header(f"👤 {current_user}")
        
        # Abas para funcionalidades sociais
        tab1, tab2, tab3 = st.tabs(["Amigos", "Chat", "Notificações"])
        
        with tab1:
            # Implementar lista de amigos e busca
            pass
            
        with tab2:
            # Implementar interface de chat
            pass
            
        with tab3:
            # Mostrar notificações
            notifications = [n for n in load_data('notifications') 
                            if n['to'] == current_user]
            
            if not notifications:
                st.write("Sem notificações")
            else:
                for note in notifications:
                    if note['message']['type'] == 'friend_request':
                        st.write(f"Amizade: {note['message']['from']}")
                        col1, col2 = st.columns(2)
                        with col1:
                            if st.button("Aceitar", key=f"accept_{note['message']['from']}"):
                                accept_friend_request(note['message']['from'], current_user)
                                st.rerun()
                        with col2:
                            if st.button("Recusar", key=f"reject_{note['message']['from']}"):
                                remove_notification(current_user, note['message']['from'])
                                st.rerun()
    
    # Seção principal de cálculos
    st.header("📊 Cálculos Científicos")
    
    calc_type = st.selectbox("Selecione o tipo de cálculo:", [
        "Lei de Coulomb", "Gravitação Universal", 
        "Movimento Uniforme", "Equação de Bhaskara",
        "Geometria Plana"
    ])
    
    if calc_type == "Gravitação Universal":
        with st.form("gravitation_form"):
            col1, col2 = st.columns(2)
            with col1:
                m1 = st.number_input("Massa 1 (kg)", value=1.0)
                m2 = st.number_input("Massa 2 (kg)", value=1.0)
            with col2:
                dist = st.number_input("Distância (m)", value=1.0)
            
            if st.form_submit_button("Calcular Força"):
                force, steps = calculate_gravitational_force(m1, m2, dist)
                if force is not None:
                    st.success(f"Força gravitacional: {force:.3e} N")
                    st.markdown(steps)
                    st.image('gravitational_force_plot.png')
    
    elif calc_type == "Equação de Bhaskara":
        with st.form("bhaskara_form"):
            col1, col2, col3 = st.columns(3)
            with col1:
                a = st.number_input("Coeficiente a", value=1.0)
            with col2:
                b = st.number_input("Coeficiente b", value=0.0)
            with col3:
                c = st.number_input("Coeficiente c", value=0.0)
            
            if st.form_submit_button("Calcular Raízes"):
                roots, steps = bhaskara(a, b, c)
                if roots[0] is not None:
                    st.success(f"Raízes: x₁ = {roots[0]:.2f}, x₂ = {roots[1]:.2f}")
                    st.markdown(steps)
                    st.image('bhaskara_plot.png')
                else:
                    st.warning("Não há raízes reais")

# ==============================================
# FUNÇÃO PRINCIPAL
# ==============================================

def main() -> None:
    """Controla o fluxo principal da aplicação."""
    # Inicializa estado da sessão
    if 'page' not in st.session_state:
        st.session_state.page = 'auth'
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    
    # Roteamento de páginas
    if st.session_state.page == 'auth':
        auth_page()
    elif st.session_state.logged_in:
        main_page()

if __name__ == "__main__":
    main()
