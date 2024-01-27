from HealthTools.__init__ import verifica_pressão_arterial
from HealthTools.__init__ import verifica_imc
from HealthTools.__init__ import calcular_tfg
from HealthTools.__init__ import contar_hemacias
from HealthTools.__init__ import contar_leucocitos
from HealthTools.__init__ import contar_plaquetas
from HealthTools.__init__ import calcular_fcm
from HealthTools.__init__ import calcular_frequencia_respiratoria
from HealthTools.__init__ import calcular_debito_cardiaco
from HealthTools.__init__ import calcular_tp
from HealthTools.__init__ import calcular_ttpa
from HealthTools.__init__ import calcular_indice_apgar
from HealthTools.__init__ import classificar_pvc
from HealthTools.__init__ import classificar_glicemia
from HealthTools.__init__ import classificar_spo2
from HealthTools.__init__ import calcular_debito_urinario
from HealthTools.__init__ import classificar_espirometria
from HealthTools.__init__ import teste_capacidade_anaerobica
from HealthTools.__init__ import teste_funcao_renal
from HealthTools.__init__ import teste_funcao_hepatica
from HealthTools.__init__ import teste_funcao_tireoidiana


'''
# Função 1 - Pressão arterial
resultado_simple = verifica_pressão_arterial(130, 60, 'masculino', 40, 'simple')
print(resultado_simple)

resultado_advanced = verifica_pressão_arterial(140, 80, 'masculino', 40, 'advanced')
print(resultado_advanced)

teste = verifica_pressão_arterial(90, 60, 'feminino', 40, 'simple')
print(teste)
'''
"""
#Função 2 - Verifica Indice de massa corporal
resultado_simple = verifica_imc(70, 1.80, "masculino", "simple")
print(resultado_simple)
"""
"""
#Função 3- Calcula
tfg = calcular_tfg(1.2, 30, sexo='masculino', raca='negra', output='ml/min/1.73m^2')
print("TFG:", tfg)
"""
"""
# Função4- contagem de hemacias
resultado_hemacias = contar_hemacias(8.2, "masculino","simple")
print("Métrica de hemácias:", resultado_hemacias)
"""
"""
# Função5- Contagem de leucócitos
resultado_hemacias = contar_leucocitos(7.0,"simple")
print(resultado_hemacias)
"""

"""#Função6- contar_plaquetas
resltado = contar_plaquetas(1000000,"simple")
print(resltado)"""

"""#Função7- Calcular frequencia cardiaca maxima
resultado = calcular_fcm(8,"masculino")
print(resultado)"""

#Função8- Frequencia respiratoria
"""idade = 25
fr = 22  # Frequência respiratória de exemplo
categoria_fr = calcular_frequencia_respiratoria(fr, idade)
print("Categoria da Frequência Respiratória:", categoria_fr)"""

"""#Função9 - calcular_debito_cardiaco
frequencia_cardiaca = 75  # Exemplo de frequência cardíaca (bpm)
volume_sistolico = 70  # Exemplo de volume sistólico (ml/bat)
resultado = calcular_debito_cardiaco(frequencia_cardiaca, volume_sistolico, saida='simple')
print(resultado)"""

#Função10 - calcular_tp

"""resultado_simple = calcular_tp(12.5, saida='simple')
print(resultado_simple)  # Saída: "Normal"

resultado_advanced = calcular_tp(11.8)
print(resultado_advanced)  # Saída: (11.8, 'Normal')"""

"""#Função11 - Tempo de Tromboplastina Parcial Ativada (TTPA)


resultado_simple = calcular_ttpa(30.0, saida='simple')
print(resultado_simple)  # Saída: "Normal"

resultado_advanced = calcular_ttpa(32.5)
print(resultado_advanced)  # Saída: (32.5, 'Alto')"""

"""#Função12 - Indice Apgar
cor = 4
frequencia_cardiaca = 5
respiracao = 3
tonus_muscular = 5
reflexos = 4

indice_apgar_total = calcular_indice_apgar(cor, frequencia_cardiaca, respiracao, tonus_muscular, reflexos,saida = "advanced")

print("Classificação do Índice de Apgar:", indice_apgar_total)"""

"""#Função13 - Concentração de Glicose no Sangue (Glicemia)
resultado = classificar_glicemia(139)
print(resultado)"""

"""#Função14 - Saturação de Oxigênio (SpO2)

resultado = classificar_spo2(92)
print(resultado)
"""

"""#Função15 - Calcula debito urinario
resultado = calcular_debito_urinario(2,2,"simple")
print(resultado)
"""

"""#Função16 -Teste de Função Pulmonar (espirometria)
resultado_analise = classificar_espirometria(3.0, 4.0, 'masculino', 35)
print(resultado_analise)"""

"""#Função17 - analisa capacidade anaerobica
# Exemplo de uso:
tempo_teste = 15
resultado = teste_capacidade_anaerobica(tempo_teste)
print("Resultado do teste de capacidade anaeróbica:", resultado)"""

"""#Função18 - teste_funcao_renal
resultado = teste_funcao_renal(0.2,1.2,'advanced')
print(resultado)"""

"""#Função19 - Teste Função Hepatica
resultado = teste_funcao_hepatica(ast=30, alt=40, alp=100, bilirrubina_total=1.0, bilirrubina_direta=0.2, bilirrubina_indireta=0.8, saida='simple')
print(resultado)"""

"""#Função20- classifica_função tireoide
resultado = teste_funcao_tireoidiana(tsh=2.5, t4_total=110, t4_livre=15, t3_total=2.2, t3_livre=4.5, saida='simple')
print(resultado)"""




