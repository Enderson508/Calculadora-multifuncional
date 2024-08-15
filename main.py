import streamlit as st
import math
import matplotlib.pyplot as plt

# Constante de Coulomb
K = 9e9  # N m²/C²
# constante de newthon
G = 6.674 * 10e-11

# pi
π = 3.14

# Definindo o valor limite de corrente para verificação de segurança
max_current = 10  # Amperes

# Função para calcular a intensidade da corrente
def calculate_current(charge, time):
    if time <= 0:
        st.error("O tempo deve ser maior que zero.")
        return None, ""
    current = charge / time
    if current > max_current:
        st.warning("Aviso: A corrente está muito alta! Risco de sobrecarga ou curto-circuito.")
    steps = f"\n## Cálculo da Intensidade da Corrente (A)\n" \
            f"\n### Fórmula\n" \
            f"\n$$I = \\frac{{Q}}{{t}}$$\n" \
            f"\n### Substituindo os valores\n" \
            f"\n$$I = \\frac{{{charge}}}{{{time}}}$$\n" \
            f"\n### Resultado\n" \
            f"\n$$I = {current:.2f} \\text{{ A}}$$\n"
    # Plotar gráfico
    plt.figure(figsize=(10, 5))
    plt.plot([0, time], [0, current], marker='o')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Corrente (A)')
    plt.title('Gráfico da Intensidade da Corrente')
    plt.grid(True)
    plt.savefig('current_plot.png')
    plt.close()
    return current, steps




#Geometria Plana(começo)

def calculate_area_replace(π, raio):
    are = π * raio ** 2
    steps = f"\n## Calculando área do Círculo\n"\
            f"\n### Fórmula\n" \
            f"\n$$A = π \\cdot r^2$$\n"\
            f"\n## substituindo valores\n" \
            f"\n$$A = {π} \\cdot {raio}^2$$\n" \
            f"\n##Resultado\n"\
            f"\n$$A = {are:.2f} \\text A$$\n"\


    # Plotar gráfico
    distance_val = list(range(1, 11))  # Distância de 1 a 10 metros
    velocity_val = [(π * raio * d_val) for d_val in distance_val]
    plt.figure(figsize=(10, 5))
    plt.plot(distance_val, velocity_val, marker='o')
    plt.xlabel('Distância (m)')
    plt.ylabel('Velocidade (m/s)')
    plt.title('Gráfico da Velocidade de acordo com a Área do Círculo')
    plt.grid(True)
    plt.savefig('area_plot.png')
    plt.close()
    return are, steps

def calculate_triangle_ll(h, ary):
    hrr = ary * h / 2
    steps = f"\n### Calculando a Área\n" \
            f"\n## Fórmula\n" \
            f"\n$$A = \\frac{{B \\cdot H}}{{2}}$$\n" \
            f"\n## Substituindo valores\n" \
            f"\n$$A = \\frac{{ {ary} \\cdot {h}}}{{{2}}}$$\n" \
            f"\n## Resultado\n" \
            f"\n$$A = {hrr:.2f}$$\n"


    distance_vllil = list(range(1, 11))  # Distância de 1 a 10 metros
    velocity_vllil = [hrr * d_val for d_val in distance_vllil]  # Usar a área calculada no gráfico
    plt.figure(figsize=(10, 5))
    plt.plot(distance_vllil, velocity_vllil, marker='o')
    plt.xlabel('Distância (m)')
    plt.ylabel('Velocidade (m/s)')
    plt.title('Gráfico da Velocidade de acordo com a Área do Triângulo')
    plt.grid(True)
    plt.savefig('area_triangle.png')
    plt.close()
    return hrr, steps


def calculate_area_trapez(trap, trapl, hll):
    result = (trap + trapl) * hll / 2
    steps = f"\n### Calculando Área do Trapézio\n" \
            f"\n## Fórmula\n" \
            f"\n$$A = \\frac{{ (b1 + b2) \\cdot h}}{{2}}$$\n" \
            f"\n## Substituindo Valores\n" \
            f"\n$$A = \\frac{{ ({trap} + {trapl}) \\cdot {hll}}}{{{2}}}$$\n" \
            f"\n## Resultado\n" \
            f"\n$$A = {result:.2f}$$\n"

    distance_trap = list(range(1, 11))  # Distância de 1 a 10 metros
    velocity_trap = [result * d_val for d_val in distance_trap]  # Usar a área calculada no gráfico
    plt.figure(figsize=(10, 5))
    plt.plot(distance_trap, velocity_trap, marker='o')
    plt.xlabel('Distância (m)')
    plt.ylabel('Velocidade (m/s)')
    plt.title('Gráfico da Velocidade de acordo com a Área do Triângulo')
    plt.grid(True)
    plt.savefig('area_trapezio.png')
    plt.close()
    return result, steps

# Função para calcular a força da gravitação universal
def calculate_gravitational_force(mass1, mass2, distance):
    if distance <= 0:
        st.error("A distância deve ser maior que zero.")
        return None, ""
    force = G * mass1 * mass2 / distance ** 2
    steps = f"\n## Cálculo da Força da Gravitação Universal (N)\n" \
            f"\n### Fórmula\n" \
            f"\n$$F = \\frac{{G \\cdot m1 \\cdot m2}}{{d^2}}$$\n" \
            f"\n### Substituindo os valores\n" \
            f"\n$$F = \\frac{{{G} \\cdot {mass1} \\cdot {mass2}}}{{{distance}^2}}$$\n" \
            f"\n### Resultado\n" \
            f"\n$$F = {force:.2e} \\text{{ m/s²}}$$\n"
    # Plotar gráfico
    distance_vals = list(range(1, 11))  # Distância de 1 a 10 metros
    force_vals = [G * mass1 * mass2 / (d_val ** 2) for d_val in distance_vals]
    plt.figure(figsize=(10, 5))
    plt.plot(distance_vals, force_vals, marker='o')
    plt.xlabel('Distância (m)')
    plt.ylabel('Força (N)')
    plt.title('Gráfico da Força da Gravitação Universal')
    plt.grid(True)
    plt.savefig('gravitational_force_plot.png')
    plt.close()
    return force, steps

def calculate_distance_replace(Mas1, Mas2, F):
    distance = G * Mas1 * Mas2 / F
    d = math.sqrt(distance)
    steps = f"\n## Cálculo de Distância\n"\
            f"\n### Formula\n"\
            f"\n$$d^2 = \\frac{{G \\cdot M1 \\cdot M2}}{{F}}$$\n"\
            f"\n### Substituindo Valores\n"\
            f"\n$$d^2 = \\frac{{{G} \\cdot{Mas1} \\cdot {Mas2}}}{{{F}}}$$\n"\
            f"\n### Resultado\n"\
            f"\n$$d = {d:.2e} \\text{{ m}}$$\n"

    distance_vals = list(range(1, 11))  # Distância de 1 a 10 metros
    force_vals = [G * Mas1 * Mas2 / (d_val ** 2) for d_val in distance_vals]

    plt.figure(figsize=(10, 5))
    plt.plot(distance_vals, force_vals, marker='o', linestyle='-')
    plt.xlabel('Distância (m)')
    plt.ylabel('Força (N)')
    plt.title('Gráfico da Força da Gravitação Universal')
    plt.grid(True)
    plt.savefig('gravitational_distance_replaceplot.png')
    plt.close()

    return d, steps      


#Função para calcular torriceli
def calculate_torricelli_force(vi, a, s):
    velocit = vi**2 + 2*a*s
    vf = math.sqrt(velocit)
    steps = f"## Cálculo de Torricelli\n"\
        f"### Fórmula\n"\
        f"\n$$Vf^2 = vi^2 + 2a\\cdot s$$\n"\
        f"\n### Substituindo os valores\n"\
        f"\n$$Vf^2 = {vi}^2 + 2 \\cdot {a}\\cdot {s}$$\n"\
        f"\n### Resultado\n"\
        f"\n$$Vf = {vf:.2f} \\text{{ m/s}}$$\n"

    # Plotar gráfico
    distance_vals = list(range(1, 11))  # Distância de 1 a 10 metros
    velocity_vals = [math.sqrt(vi**2 + 2*a*d_val) for d_val in distance_vals]
    plt.figure(figsize=(10, 5))
    plt.plot(distance_vals, velocity_vals, marker='o')
    plt.xlabel('Distância (m)')
    plt.ylabel('Velocidade (m/s)')
    plt.title('Gráfico da Velocidade de acordo com a Lei de Torricelli')
    plt.grid(True)
    plt.savefig('torricelli_plot.png')
    plt.close()
    return velocit, steps



# Função para calcular a quantidade de carga
def calculate_charge(current, time):
    charge = current * time
    steps = f"\n## Cálculo da Quantidade de Carga (C)\n" \
            f"\n### Fórmula\n" \
            f"\n$$Q = I \\cdot t$$\n" \
            f"\n### Substituindo os valores\n" \
            f"\n$$Q = {current} \\cdot {time}$$\n" \
            f"\n### Resultado\n" \
            f"\n$$Q = {charge:.2f} \\text{{ C}}$$\n"
    # Plotar gráfico
    plt.figure(figsize=(10, 5))
    plt.plot([0, time], [0, charge], marker='o')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Carga (C)')
    plt.title('Gráfico da Quantidade de Carga')
    plt.grid(True)
    plt.savefig('charge_plot.png')
    plt.close()
    return charge, steps

# Função para calcular o tempo
def calculate_time(current, charge):
    if current <= 0:
        st.error("A corrente deve ser maior que zero.")
        return None, ""
    time = charge / current
    steps = f"\n## Cálculo do Tempo (s)\n" \
            f"\n### Fórmula\n" \
            f"\n$$t = \\frac{{Q}}{{I}}$$\n" \
            f"\n### Substituindo os valores\n" \
            f"\n$$t = \\frac{{{charge}}}{{{current}}}$$\n" \
            f"\n### Resultado\n" \
            f"\n$$t = {time:.2f} \\text{{ s}}$$\n"
    # Plotar gráfico
    plt.figure(figsize=(10, 5))
    plt.plot([0, current], [0, time], marker='o')
    plt.xlabel('Corrente (A)')
    plt.ylabel('Tempo (s)')
    plt.title('Gráfico do Tempo')
    plt.grid(True)
    plt.savefig('time_plot.png')
    plt.close()
    return time, steps

# Função para calcular as raízes da equação de Bhaskara
def bhaskara(a, b, c):
    delta = b ** 2 - 4 * a * c
    steps = f"\n## Cálculo das Raízes pela Fórmula de Bhaskara\n" \
            f"\n### Cálculo do Delta\n" \
            f"\n$$\\Delta = b^2 - 4ac$$\n" \
            f"\n$$\\Delta = ({b})^2 - 4 \\cdot {a} \\cdot {c}$$\n" \
            f"\n$$\\Delta = {b * b} - {4 * a * c}$$\n" \
            f"\n$$\\Delta = {delta}$$\n"
    if delta < 0:
        steps += "\n### Não existem raízes reais porque \\(\\Delta < 0\\)."
        return (None, None), steps
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    steps += f"\n### Cálculo das Raízes\n" \
             f"\n$$x = \\frac{{-b \\pm \\sqrt{{\\Delta}}}}{{2a}}$$\n" \
             f"\n$$x_1 = \\frac{{-{b} + \\sqrt{{{delta}}}}}{{2 \\cdot {a}}}$$\n" \
             f"\n$$x_1 = {x1:.2f}$$\n" \
             f"\n$$x_2 = \\frac{{-{b} - \\sqrt{{{delta}}}}}{{2 \\cdot {a}}}$$\n" \
             f"\n$$x_2 = {x2:.2f}$$\n"
    # Plotar gráfico
    x_vals = [x1, x2]
    y_vals = [0, 0]
    plt.figure(figsize=(10, 5))
    plt.scatter(x_vals, y_vals)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gráfico das Raízes da Equação de Bhaskara')
    plt.grid(True)
    plt.savefig('bhaskara_plot.png')
    plt.close()
    return (x1, x2), steps

# Função para calcular o campo elétrico
def calculate_electric_field(q, d):
    if d == 0:
        st.error("A distância não pode ser zero.")
        return None, ""
    field = K * abs(q) / d**2
    steps = f"\n## Cálculo do Campo Elétrico (N/C)\n" \
            f"\n### Fórmula\n" \
            f"\n$$E = \\frac{{K \\cdot |q|}}{{d^2}}$$\n" \
            f"\n### Substituindo os valores\n" \
            f"\n$$E = \\frac{{{K} \\cdot |{q}|}}{{{d}^2}}$$\n" \
            f"\n### Resultado\n" \
            f"\n$$E = {field:.2f} \\text{{ N/C}}$$\n"
    # Plotar gráfico
    d_vals = list(range(1, 11))  # Distância de 1 a 10 metros
    e_vals = [K * abs(q) / (d_val**2) for d_val in d_vals]
    plt.figure(figsize=(10, 5))
    plt.plot(d_vals, e_vals, marker='o')
    plt.xlabel('Distância (m)')
    plt.ylabel('Campo Elétrico (N/C)')
    plt.title('Gráfico do Campo Elétrico')
    plt.grid(True)
    plt.savefig('electric_field_plot.png')
    plt.close()
    return field, steps

# Função para calcular a força elétrica
def calculate_electric_force(q1, q2, d):
    if d == 0:
        st.error("A distância não pode ser zero.")
        return None, ""
    force = K * abs(q1) * abs(q2) / d**2
    steps = f"\n## Cálculo da Força Elétrica (N)\n" \
            f"\n### Fórmula\n" \
            f"\n$$F = \\frac{{K \\cdot |q_1| \\cdot |q_2|}}{{d^2}}$$\n" \
            f"\n### Substituindo os valores\n" \
            f"\n$$F = \\frac{{{K} \\cdot |{q1}| \\cdot |{q2}|}}{{{d}^2}}$$\n" \
            f"\n### Resultado\n" \
            f"\n$$F = {force:.2f} \\text{{ N}}$$\n"
    # Plotar gráfico
    d_vals = list(range(1, 11))  # Distância de 1 a 10 metros
    f_vals = [K * abs(q1) * abs(q2) / (d_val**2) for d_val in d_vals]
    plt.figure(figsize=(10, 5))
    plt.plot(d_vals, f_vals, marker='o')
    plt.xlabel('Distância (m)')
    plt.ylabel('Força Elétrica (N)')
    plt.title('Gráfico da Força Elétrica')
    plt.grid(True)
    plt.savefig('electric_force_plot.png')
    plt.close()
    return force, steps

# Função para calcular a velocidade média
def calculate_average_velocity(distance, time):
    if time <= 0:
        st.error("O tempo deve ser maior que zero.")
        return None, ""
    velocity = distance / time
    steps = f"\n## Cálculo da Velocidade Média (m/s)\n" \
            f"\n### Fórmula\n" \
            f"\n$$v = \\frac{{d}}{{t}}$$\n" \
            f"\n### Substituindo os valores\n" \
            f"\n$$v = \\frac{{{distance}}}{{{time}}}$$\n" \
            f"\n### Resultado\n" \
            f"\n$$v = {velocity:.2f} \\text{{ m/s}}$$\n"
    # Plotar gráfico
    x_values = [0, time]
    y_values = [0, velocity]
    plt.figure(figsize=(10, 5))
    plt.plot(x_values, y_values, marker='o')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Velocidade (m/s)')
    plt.title('Gráfico da Velocidade Média')
    plt.grid(True)
    plt.savefig('average_velocity_plot.png')
    plt.close()
    return velocity, steps

# Função para calcular a posição no movimento uniforme
def calculate_position_uniform_motion(velocity, time):
    position = velocity * time
    steps = f"\n## Cálculo da Posição (m)\n" \
            f"\n### Fórmula\n" \
            f"\n$$x = v \\cdot t$$\n" \
            f"\n### Substituindo os valores\n" \
            f"\n$$x = {velocity} \\cdot {time}$$\n" \
            f"\n### Resultado\n" \
            f"\n$$x = {position:.2f} \\text{{ m}}$$\n"
    # Plotar gráfico
    x_values = [0, time]
    y_values = [0, position]
    plt.figure(figsize=(10, 5))
    plt.plot(x_values, y_values, marker='o')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Posição (m)')
    plt.title('Gráfico da Posição no Movimento Uniforme')
    plt.grid(True)
    plt.savefig('uniform_motion_position_plot.png')
    plt.close()
    return position, steps

# Função para calcular a aceleração no movimento uniformemente acelerado
def calculate_acceleration_uniformly_accelerated_motion(initial_velocity, final_velocity, time):
    if time <= 0:
        st.error("O tempo deve ser maior que zero.")
        return None, ""
    acceleration = (final_velocity - initial_velocity) / time
    steps = f"\n## Cálculo da Aceleração (m/s²)\n" \
            f"\n### Fórmula\n" \
            f"\n$$a = \\frac{{v_f - v_i}}{{t}}$$\n" \
            f"\n### Substituindo os valores\n" \
            f"\n$$a = \\frac{{{final_velocity} - {initial_velocity}}}{{{time}}}$$\n" \
            f"\n### Resultado\n" \
            f"\n$$a = {acceleration:.2f} \\text{{ m/s²}}$$\n"
    # Plotar gráfico
    x_values = [0, time]
    y_values = [initial_velocity, final_velocity]
    plt.figure(figsize=(10, 5))
    plt.plot(x_values, y_values, marker='o')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Velocidade (m/s)')
    plt.title('Gráfico da Velocidade no Movimento Uniformemente Acelerado')
    plt.grid(True)
    plt.savefig('uniformly_accelerated_motion_plot.png')
    plt.close()
    return acceleration, steps

# Função para calcular o deslocamento no movimento uniformemente acelerado
def calculate_displacement_uniformly_accelerated_motion(initial_velocity, acceleration, time):
    displacement = initial_velocity * time + 0.5 * acceleration * time**2
    steps = f"\n## Cálculo do Deslocamento (m)\n" \
            f"\n### Fórmula\n" \
            f"\n$$x = v_i \\cdot t + \\frac{1}{2} a \\cdot t^2$$\n" \
            f"\n### Substituindo os valores\n" \
            f"\n$$x = {initial_velocity} \\cdot {time} + \\frac{1}{2} \\cdot {acceleration} \\cdot {time}^2$$\n" \
            f"\n### Resultado\n" \
            f"\n$$x = {displacement:.2f} \\text{{ m}}$$\n"
    # Plotar gráfico
    x_values = [0, time]
    y_values = [0, displacement]
    plt.figure(figsize=(10, 5))
    plt.plot(x_values, y_values, marker='o')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Deslocamento (m)')
    plt.title('Gráfico do Deslocamento no Movimento Uniformemente Acelerado')
    plt.grid(True)
    plt.savefig('displacement_plot.png')
    plt.close()
    return displacement, steps

# Função principal
def main():
    st.title("Calculadora de Física e Matemática")
      calculation_type = st.selectbox(
        "Física:",
        ["Intensidade da Corrente", "Quantidade de Carga", "Tempo", "Raízes da Equação de Bhaskara",
         "Campo Elétrico", "Força Elétrica", "Geometria Plana", "Velocidade Média", "Movimento Uniforme",
         "Movimento Uniformemente Acelerado","Gravitação universal", "Equação de Torricelli"]


    ) 




    if calculation_type == "Intensidade da Corrente":
        charge = st.number_input("Digite a carga (C)", value=0.0)
        time = st.number_input("Digite o tempo (s)", value=0.0)
        if st.button("Calcular Corrente"):
            current, steps = calculate_current(charge, time)
            if current is not None:
                st.write(f"Intensidade da Corrente: {current:.2f} A")
                st.markdown(steps)
                st.image('current_plot.png')


    elif calculation_type == "Equação de Torricelli":
        st.header('Cálculo da Velocidade Final com Torricelli')
        vi = st.number_input('Velocidade Inicial (m/s)')
        a = st.number_input('Aceleração (m/s²)')
        s = st.number_input('Distância (m)')
        if st.button('Calcular Velocidade Final'):
            vf, steps = calculate_torricelli_force(vi, a, s)
            if vf is not None:
                st.write(steps)
                st.image('torricelli_plot.png')       

    elif calculation_type == "Quantidade de Carga":
        current = st.number_input("Digite a corrente (A)", value=0.0)
        time = st.number_input("Digite o tempo (s)", value=0.0)
        if st.button("Calcular Carga"):
            charge, steps = calculate_charge(current, time)
            if charge is not None:
                st.write(f"Quantidade de Carga: {charge:.2f} C")
                st.markdown(steps)
                st.image('charge_plot.png')

    elif calculation_type == "Tempo":
        current = st.number_input("Digite a corrente (A)", value=0.0)
        charge = st.number_input("Digite a carga (C)", value=0.0)
        if st.button("Calcular Tempo"):
            time, steps = calculate_time(current, charge)
            if time is not None:
                st.write(f"Tempo: {time:.2f} s")
                st.markdown(steps)
                st.image('time_plot.png')



    elif calculation_type == "Gravitação universal":
        Massa1 = st.number_input("Digite a massa 1 (kg)", value=0.0)
        Massa2 = st.number_input("Digite a massa 2 (kg)", value=0.0)
        Distância = st.number_input("Digite a distância/Força (m)", value=0.0)
        if st.button("Calcular Força"):
            force, steps = calculate_gravitational_force(Massa1, Massa2, Distância)
            if force is not None:
                st.write(f"Força: {force:.2f} m/s")
                st.markdown(steps)
                st.image('gravitational_force_plot.png')


        if st.button("Calcular Distância"):
            force, steps = calculate_gravitational_force(Massa1, Massa2, Distância)
            distance, steps = calculate_distance_replace(Massa1, Massa2, Distância)
            if distance is not None:
                st.write(f"Distância: {distance:.2f} m/s")
                st.markdown(steps)
                st.image('gravitational_distance_replaceplot.png')


    elif calculation_type == "Campo Elétrico":
        charge = st.number_input("Digite a carga (C)", value=0.0)
        distance = st.number_input("Digite a distância (m)", value=0.0)
        if st.button("Calcular Campo Elétrico"):
            field, steps = calculate_electric_field(charge, distance)
            if field is not None:
                st.write(f"Campo Elétrico: {field:.2f} N/C")
                st.markdown(steps)
                st.image('electric_field_plot.png')

    elif calculation_type == "Força Elétrica":
        charge1 = st.number_input("Digite a carga 1 (C)", value=0.0)
        charge2 = st.number_input("Digite a carga 2 (C)", value=0.0)
        distance = st.number_input("Digite a distância (m)", value=0.0)
        if st.button("Calcular Força Elétrica"):
            force, steps = calculate_electric_force(charge1, charge2, distance)
            if force is not None:
                st.write(f"Força Elétrica: {force:.2f} N")
                st.markdown(steps)
                st.image('electric_force_plot.png')

    elif calculation_type == "Velocidade Média":
        distance = st.number_input("Digite a distância (m)", value=0.0)
        time = st.number_input("Digite o tempo (s)", value=0.0)
        if st.button("Calcular Velocidade Média"):
            velocity, steps = calculate_average_velocity(distance, time)
            if velocity is not None:
                st.write(f"Velocidade Média: {velocity:.2f} m/s")
                st.markdown(steps)
                st.image('average_velocity_plot.png')

    elif calculation_type == "Movimento Uniforme":
        velocity = st.number_input("Digite a velocidade (m/s)", value=0.0)
        time = st.number_input("Digite o tempo (s)", value=0.0)
        if st.button("Calcular Posição"):
            position, steps = calculate_position_uniform_motion(velocity, time)
            if position is not None:
                st.write(f"Posição: {position:.2f} m")
                st.markdown(steps)
                st.image('uniform_motion_position_plot.png')

    elif calculation_type == "Movimento Uniformemente Acelerado":
        initial_velocity = st.number_input("Digite a velocidade inicial (m/s)", value=0.0)
        final_velocity = st.number_input("Digite a velocidade final (m/s)", value=0.0)
        time = st.number_input("Digite o tempo (s)", value=0.0)
        if st.button("Calcular Aceleração"):
            acceleration, steps = calculate_acceleration_uniformly_accelerated_motion(initial_velocity, final_velocity, time)
            if acceleration is not None:
                st.write(f"Aceleração: {acceleration:.2f} m/s²")
                st.markdown(steps)
                st.image('uniformly_accelerated_motion_plot.png')

        if st.button("Calcular Deslocamento"):
            acceleration, steps = calculate_acceleration_uniformly_accelerated_motion(initial_velocity, final_velocity, time)
            displacement, steps = calculate_displacement_uniformly_accelerated_motion(initial_velocity, acceleration, time)
            if displacement is not None:
                st.write(f"Deslocamento: {displacement:.2f} m")
                st.markdown(steps)
                st.image('displacement_plot.png')



                
                
    calculate_ss = st.selectbox(
      "Matemática:",
      ["Geometria Plana", "Raízes da Equação de Bhaskara"]
      )            

    #GEOMETRIA PLANA            
   elif calculate_ss == "Geometria Plana":
        raio = st.number_input("Digite o  raio (r)", value=0.0)
        if st.button("Calcular Círculo"):
            are, steps = calculate_area_replace(π , raio)
            if are is not None:
                st.write(f"Área: {are:.2f}")
                st.markdown(steps)
                st.image('area_plot.png')

        ary = st.number_input("Base", value=0.0)
        h = st.number_input("Altura(h)", value=0.0)
        if  st.button("Calcular Área do triângulo"):
            hrr, steps = calculate_triangle_ll(ary, h)
            if hrr is not None:
                st.write(f"Área: {hrr:.2f}") 
                st.markdown(steps)
                st.image('area_triangle.png')
        trap = st.number_input("Base (1)", value = 0.0)
        trapl = st.number_input("Base (2)", value = 0.0)  
        hll = st.number_input("Alturas(h)", value = 0.0)
        if st.button('Calcular Área do trapézio'):
            result, steps = calculate_area_trapez(trap, trapl, hll)
            if result is not None:
                st.write(f"Área: {result:.2f}") 
                st.markdown(steps)
                st.image('area_trapezio.png')

    elif calculate_ss == "Raízes da Equação de Bhaskara":
        a = st.number_input("Digite o valor de a", value=1.0)
        b = st.number_input("Digite o valor de b", value=0.0)
        c = st.number_input("Digite o valor de c", value=0.0)
        if st.button("Calcular Raízes"):
            roots, steps = bhaskara(a, b, c)
            if roots[0] is not None:
                st.write(f"Raízes: x1 = {roots[0]:.2f}, x2 = {roots[1]:.2f}")
                st.markdown(steps)
                st.image('bhaskara_plot.png')







if __name__ == "__main__":
    main()
