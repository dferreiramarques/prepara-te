import json
import random

random.seed(42)

cards = []
_id = [0]

def add(domain, topic, question, answer, explanation, difficulty="medio"):
    _id[0] += 1
    cards.append({
        "id": f"c{_id[0]:03d}",
        "domain": domain,
        "topic": topic,
        "question": question,
        "answer": answer,
        "explanation": explanation,
        "difficulty": difficulty,
    })

NUM = "Números"
GM = "Geometria e Medida"
ALG = "Álgebra"
DP = "Dados e Probabilidade"

# =====================================================================
# NÚMEROS — conceitos
# =====================================================================
add(NUM, "Valor posicional", "No número 47 832, qual é o valor posicional do algarismo 8?",
    "800 (oito centenas)",
    "O algarismo 8 ocupa a 3ª casa a contar da direita, a casa das centenas, por isso vale 8 × 100 = 800.")

add(NUM, "Ordens e classes", "Quantas classes tem o número 5 214 397?",
    "Duas classes: a classe dos milhões e a classe das unidades",
    "5 214 397 = 5 milhões, 214 mil e 397 unidades. A classe dos milhões (5) e a classe das unidades (214 397, com as ordens de milhar e simples).")

add(NUM, "Múltiplos", "Quais são os primeiros 5 múltiplos de 7 (maiores que zero)?",
    "7, 14, 21, 28, 35",
    "Os múltiplos de um número obtêm-se multiplicando-o sucessivamente por 1, 2, 3, 4, 5…: 7×1=7, 7×2=14, 7×3=21, 7×4=28, 7×5=35.")

add(NUM, "Divisores", "Quais são todos os divisores de 24?",
    "1, 2, 3, 4, 6, 8, 12, 24",
    "Um divisor de 24 é um número que divide 24 sem deixar resto. Testando: 24÷1=24, 24÷2=12, 24÷3=8, 24÷4=6, 24÷6=4, 24÷8=3, 24÷12=2, 24÷24=1.")

add(NUM, "Critérios de divisibilidade", "Como se sabe, sem dividir, se um número é divisível por 3?",
    "Se a soma dos seus algarismos for múltiplo de 3",
    "Exemplo: 234 → 2+3+4 = 9, que é múltiplo de 3, logo 234 é divisível por 3 (234÷3=78).")

add(NUM, "Critérios de divisibilidade", "Como se sabe, sem dividir, se um número é divisível por 9?",
    "Se a soma dos seus algarismos for múltiplo de 9",
    "Exemplo: 5 481 → 5+4+8+1 = 18, que é múltiplo de 9, logo 5 481 é divisível por 9.")

add(NUM, "Critérios de divisibilidade", "Como se sabe, sem dividir, se um número é divisível por 4?",
    "Se o número formado pelos dois últimos algarismos for múltiplo de 4 (ou 00)",
    "Exemplo: 3 716 → os dois últimos algarismos formam 16, que é múltiplo de 4 (16÷4=4), logo 3 716 é divisível por 4.")

add(NUM, "Números primos", "O que é um número primo?",
    "Um número natural maior que 1 que tem exatamente dois divisores: 1 e ele próprio",
    "Por exemplo, 7 só é divisível por 1 e por 7, por isso é primo. Já o 8 tem mais divisores (1, 2, 4, 8), logo não é primo — é composto.")

add(NUM, "Números primos", "Indica os números primos entre 10 e 20.",
    "11, 13, 17, 19",
    "Testando cada número de 10 a 20: 11, 13, 17 e 19 só são divisíveis por 1 e por si próprios. Os restantes (12, 14, 15, 16, 18, 20) têm mais divisores.")

add(NUM, "Números primos e compostos", "1 é um número primo? Porquê?",
    "Não",
    "Por definição, um número primo tem exatamente dois divisores diferentes. O número 1 tem apenas um divisor (ele próprio), por isso não é considerado primo nem composto.")

add(NUM, "Frações", "O que representa o denominador de uma fração?",
    "O número de partes iguais em que o todo foi dividido",
    "Numa fração a/b, o denominador (b) indica em quantas partes iguais se dividiu a unidade, e o numerador (a) indica quantas dessas partes se consideram.")

add(NUM, "Frações equivalentes", "As frações 2/3 e 8/12 são equivalentes? Justifica.",
    "Sim",
    "Multiplicando o numerador e o denominador de 2/3 por 4, obtém-se 8/12 (2×4=8 e 3×4=12). Como representam a mesma parte do todo, são frações equivalentes.")

add(NUM, "Simplificação de frações", "Simplifica a fração 18/24 para a sua forma irredutível.",
    "3/4",
    "18 e 24 têm o divisor comum 6: 18÷6=3 e 24÷6=4. Como 3 e 4 já não têm divisores comuns além de 1, a fração 3/4 é irredutível.")

add(NUM, "Comparação de frações", "Qual é maior: 3/5 ou 3/8?",
    "3/5",
    "Quando o numerador é igual, é maior a fração com menor denominador, porque o todo foi dividido em partes maiores. Como 5 < 8, cada quinto é maior do que cada oitavo, logo 3/5 > 3/8.")

add(NUM, "Comparação de frações", "Qual é maior: 5/6 ou 7/9?",
    "5/6",
    "Reduzindo ao mesmo denominador (18): 5/6 = 15/18 e 7/9 = 14/18. Como 15/18 > 14/18, conclui-se que 5/6 > 7/9.")

add(NUM, "Numeral misto", "Escreve a fração 17/5 na forma de numeral misto.",
    "3 e 2/5 (três inteiros e dois quintos)",
    "Divide-se 17 por 5: 17÷5 dá quociente 3 e resto 2. O quociente é a parte inteira e o resto forma a nova fração: 3 + 2/5.")

add(NUM, "Números decimais", "No número 6,205, qual é o algarismo das centésimas?",
    "0",
    "Após a vírgula, a 1ª casa é das décimas, a 2ª das centésimas e a 3ª das milésimas: 6,205 → 2 (décimas), 0 (centésimas), 5 (milésimas).")

add(NUM, "Comparação de decimais", "Qual é maior: 3,4 ou 3,25?",
    "3,4",
    "Comparam-se casa a casa a partir da vírgula: as partes inteiras são iguais (3). Nas décimas, 4 > 2, por isso 3,4 é maior, independentemente do número de casas decimais.")

add(NUM, "Operações com decimais", "Calcula: 4,7 + 2,35",
    "7,05",
    "Alinham-se as vírgulas: 4,70 + 2,35 = 7,05.")

add(NUM, "Arredondamentos", "Arredonda 6,378 às décimas.",
    "6,4",
    "Olha-se para o algarismo das centésimas (7). Como 7 ≥ 5, arredonda-se por excesso: o algarismo das décimas sobe de 3 para 4, ficando 6,4.")

add(NUM, "Propriedades das operações", "Como se chama a propriedade da adição que diz que 5 + 8 = 8 + 5?",
    "Propriedade comutativa",
    "A propriedade comutativa da adição garante que trocar a ordem das parcelas não altera o resultado da soma.")

add(NUM, "Propriedades das operações", "Como se chama a propriedade que permite calcular 4 × (2 + 3) = 4×2 + 4×3?",
    "Propriedade distributiva da multiplicação em relação à adição",
    "Esta propriedade permite 'distribuir' a multiplicação por cada parcela da soma dentro dos parênteses: 4×(2+3) = 8+12 = 20, tal como 4×5 = 20.")

add(NUM, "Divisão inteira", "Numa divisão inteira, o dividendo é 47, o divisor é 6. Qual é o quociente e qual é o resto?",
    "Quociente 7, resto 5",
    "6 × 7 = 42, e 47 − 42 = 5. Como 5 é menor que o divisor 6, a divisão está certa: 47 = 6×7 + 5.")

add(NUM, "Máximo divisor comum (ideia)", "Quais são os divisores comuns a 12 e 18?",
    "1, 2, 3 e 6",
    "Divisores de 12: 1, 2, 3, 4, 6, 12. Divisores de 18: 1, 2, 3, 6, 9, 18. Os que aparecem em ambas as listas são 1, 2, 3 e 6.")

add(NUM, "Mínimo múltiplo comum (ideia)", "Qual é o menor múltiplo comum a 4 e a 6, maior que zero?",
    "12",
    "Múltiplos de 4: 4, 8, 12, 16… Múltiplos de 6: 6, 12, 18… O menor número que aparece nas duas listas é 12.")

add(NUM, "Expressões numéricas", "Calcula, respeitando a prioridade das operações: 5 + 3 × 2",
    "11",
    "A multiplicação tem prioridade sobre a adição: primeiro calcula-se 3×2=6, depois 5+6=11.")

add(NUM, "Expressões numéricas", "Calcula: (5 + 3) × 2",
    "16",
    "Os parênteses indicam o que se calcula primeiro: 5+3=8, depois 8×2=16.")

add(NUM, "Adição de frações", "Calcula 2/7 + 3/7.",
    "5/7",
    "Com o mesmo denominador, somam-se apenas os numeradores e mantém-se o denominador: 2+3=5, ficando 5/7.")

add(NUM, "Subtração de frações", "Calcula 5/8 − 1/8.",
    "4/8, que simplifica para 1/2",
    "Com o mesmo denominador, subtraem-se os numeradores: 5−1=4, ficando 4/8. Simplificando (dividindo por 4), obtém-se 1/2.")

add(NUM, "Sistema de numeração decimal", "Quantas unidades tem uma dezena de milhar?",
    "10 000",
    "Cada ordem do sistema decimal vale 10 vezes a anterior: 1 dezena de milhar = 10 × 1000 unidades = 10 000 unidades.")

add(NUM, "Números pares e ímpares", "A soma de dois números ímpares é sempre par ou ímpar?",
    "Par",
    "Por exemplo, 3+5=8 e 7+9=16. Dois números ímpares deixam sempre resto 1 na divisão por 2; somados, esses restos completam mais uma unidade, tornando o total divisível por 2.")

# =====================================================================
# NÚMEROS — cartões calculados (garantia de correção matemática)
# =====================================================================
random.seed(7)
for _ in range(10):
    a = random.randint(20, 80)
    if a % 3 == 0:
        a += 1
    add(NUM, "Divisores", f"Quantos divisores tem o número {a}?",
        str(len([d for d in range(1, a+1) if a % d == 0])),
        "Divisores de " + str(a) + ": " + ", ".join(str(d) for d in range(1, a+1) if a % d == 0) + ".",
        "dificil")

for n in [23, 34, 41, 56, 63, 77]:
    is_prime = n > 1 and all(n % d != 0 for d in range(2, int(n**0.5)+1))
    add(NUM, "Números primos", f"O número {n} é primo ou composto?",
        "Primo" if is_prime else "Composto",
        (f"{n} só é divisível por 1 e por {n}, logo é primo." if is_prime
         else f"{n} tem outros divisores além de 1 e {n} — por exemplo " +
              str(next(d for d in range(2, n) if n % d == 0)) + " — logo é composto."))

for _ in range(6):
    num1, den = random.randint(2, 9), random.choice([4, 6, 8, 10, 12])
    num2 = random.randint(2, 9)
    while num2 == num1:
        num2 = random.randint(2, 9)
    maior = num1 if num1 > num2 else num2
    add(NUM, "Comparação de frações", f"Qual é maior: {num1}/{den} ou {num2}/{den}?",
        f"{maior}/{den}",
        f"Como as frações têm o mesmo denominador ({den}), compara-se diretamente o numerador: {maior} é o maior numerador.")

# =====================================================================
# GEOMETRIA E MEDIDA
# =====================================================================
add(GM, "Retas", "O que são retas paralelas?",
    "Retas que nunca se intersectam, mantendo sempre a mesma distância entre si",
    "Duas retas no mesmo plano são paralelas se, por mais que se prolonguem, nunca se cruzam — como os carris de uma linha de comboio.")

add(GM, "Retas", "O que são retas perpendiculares?",
    "Retas que se intersectam formando um ângulo reto (90°)",
    "Quando duas retas se cruzam e o ângulo formado é exatamente 90°, dizem-se perpendiculares — como os lados de uma folha de papel.")

add(GM, "Ângulos", "Como se classifica um ângulo com amplitude de 90°?",
    "Ângulo reto",
    "Um ângulo de exatamente 90° chama-se ângulo reto. É o ângulo que se forma, por exemplo, entre os dois lados de um esquadro.")

add(GM, "Ângulos", "Como se classifica um ângulo com amplitude entre 90° e 180°?",
    "Ângulo obtuso",
    "Ângulos com amplitude superior a 90° e inferior a 180° chamam-se obtusos. Abaixo de 90° são agudos; exatamente 180° é um ângulo raso.")

add(GM, "Ângulos", "Como se classifica um ângulo com amplitude menor que 90°?",
    "Ângulo agudo",
    "Qualquer ângulo com amplitude entre 0° e 90° (sem incluir estes valores) é classificado como agudo.")

add(GM, "Ângulos", "Qual é a amplitude de um ângulo raso?",
    "180°",
    "O ângulo raso corresponde a meia volta e mede exatamente 180° — os seus lados formam uma linha reta.")

add(GM, "Triângulos", "Como se classifica um triângulo com os três lados de comprimentos diferentes?",
    "Triângulo escaleno",
    "Quando nenhum dos três lados tem o mesmo comprimento, o triângulo chama-se escaleno. Se dois lados forem iguais, é isósceles; se os três forem iguais, é equilátero.")

add(GM, "Triângulos", "Como se classifica um triângulo com os três lados iguais?",
    "Triângulo equilátero",
    "Num triângulo equilátero, os três lados (e também os três ângulos, todos de 60°) são iguais entre si.")

add(GM, "Triângulos", "Como se classifica um triângulo que tem um ângulo reto?",
    "Triângulo retângulo",
    "Um triângulo com um ângulo de 90° chama-se retângulo. Os lados que formam esse ângulo chamam-se catetos, e o lado oposto chama-se hipotenusa.")

add(GM, "Soma dos ângulos internos", "Qual é a soma das amplitudes dos ângulos internos de qualquer triângulo?",
    "180°",
    "Em qualquer triângulo, por maior ou mais estranho que seja, a soma dos três ângulos internos é sempre 180°.")

add(GM, "Soma dos ângulos internos", "Num triângulo, dois dos ângulos medem 50° e 70°. Quanto mede o terceiro ângulo?",
    "60°",
    "A soma dos ângulos internos de um triângulo é 180°. Então: 180° − 50° − 70° = 60°.")

add(GM, "Quadriláteros", "Quantos lados e quantos ângulos internos tem um quadrilátero?",
    "4 lados e 4 ângulos internos",
    "'Quadri' remete para quatro: um quadrilátero é sempre um polígono de 4 lados e 4 ângulos, como o quadrado, o retângulo, o losango ou o trapézio.")

add(GM, "Polígonos", "Como se chama um polígono com 5 lados?",
    "Pentágono",
    "Os polígonos recebem nomes conforme o número de lados: triângulo (3), quadrilátero (4), pentágono (5), hexágono (6), heptágono (7), octógono (8).")

add(GM, "Polígonos", "Como se chama um polígono com 6 lados?",
    "Hexágono",
    "Um hexágono tem exatamente 6 lados e 6 ângulos internos — é a forma clássica de um favo de mel.")

add(GM, "Circunferência e círculo", "Qual é a diferença entre circunferência e círculo?",
    "A circunferência é a linha (o contorno); o círculo é a região plana delimitada por essa linha",
    "Podemos pensar na circunferência como a 'moldura' e no círculo como a 'moldura mais o interior preenchido'.")

add(GM, "Circunferência", "O que é o raio de uma circunferência?",
    "O segmento de reta que une o centro a qualquer ponto da circunferência",
    "Todos os raios de uma mesma circunferência têm o mesmo comprimento. O diâmetro é o dobro do raio.")

add(GM, "Perímetro", "Como se calcula o perímetro de um retângulo com 8 cm de comprimento e 5 cm de largura?",
    "26 cm",
    "O perímetro é a soma de todos os lados: P = 2×(comprimento + largura) = 2×(8+5) = 2×13 = 26 cm.")

add(GM, "Perímetro", "Um quadrado tem 6 cm de lado. Qual é o seu perímetro?",
    "24 cm",
    "Num quadrado, os 4 lados são iguais: P = 4 × lado = 4 × 6 = 24 cm.")

add(GM, "Área", "Como se calcula a área de um retângulo com 7 cm de comprimento e 4 cm de largura?",
    "28 cm²",
    "A área do retângulo é dada por comprimento × largura: A = 7 × 4 = 28 cm².")

add(GM, "Área", "Um quadrado tem 5 cm de lado. Qual é a sua área?",
    "25 cm²",
    "A área do quadrado é lado × lado: A = 5 × 5 = 25 cm².")

add(GM, "Área do triângulo", "Um triângulo tem 10 cm de base e 6 cm de altura. Qual é a sua área?",
    "30 cm²",
    "A área do triângulo é (base × altura) ÷ 2: A = (10 × 6) ÷ 2 = 60 ÷ 2 = 30 cm².")

add(GM, "Sólidos geométricos", "Quantas faces, vértices e arestas tem um cubo?",
    "6 faces, 8 vértices e 12 arestas",
    "O cubo é um prisma quadrangular regular: tem 6 faces quadradas, 8 vértices (pontas) e 12 arestas (linhas onde as faces se encontram).")

add(GM, "Sólidos geométricos", "O que distingue um prisma de uma pirâmide?",
    "O prisma tem duas bases iguais e paralelas; a pirâmide tem apenas uma base e um vértice comum a todas as faces laterais",
    "Nas faces laterais, o prisma tem retângulos (ou paralelogramos) e a pirâmide tem triângulos que se encontram todos num único ponto, o vértice da pirâmide.")

add(GM, "Sólidos geométricos", "Quantas faces tem uma pirâmide de base quadrangular?",
    "5 faces (1 base quadrada + 4 faces triangulares)",
    "A pirâmide quadrangular tem uma base em forma de quadrado e quatro faces laterais triangulares que se encontram no vértice.")

add(GM, "Planificações", "O que é a planificação de um sólido geométrico?",
    "A representação de todas as faces do sólido, desenhadas no plano e ligadas entre si, que ao serem dobradas reconstroem o sólido",
    "É como 'desmontar' o sólido e espalmá-lo numa folha — útil, por exemplo, para construir um cubo em cartolina.")

add(GM, "Unidades de comprimento", "Quantos centímetros há num metro?",
    "100 cm",
    "1 metro = 100 centímetros, porque cada unidade do sistema métrico vale 10 vezes a unidade imediatamente inferior (m → dm → cm → mm).")

add(GM, "Unidades de comprimento", "Converte 3,5 metros em centímetros.",
    "350 cm",
    "Para converter metros em centímetros, multiplica-se por 100: 3,5 × 100 = 350 cm.")

add(GM, "Unidades de massa", "Quantos gramas há num quilograma?",
    "1000 g",
    "1 kg = 1000 g, seguindo o mesmo princípio do sistema métrico decimal.")

add(GM, "Unidades de capacidade", "Quantos mililitros há num litro?",
    "1000 ml",
    "1 litro = 1000 mililitros. Uma garrafa de 1,5 l, por exemplo, tem 1500 ml.")

add(GM, "Unidades de área", "Quantos cm² há num m²?",
    "10 000 cm²",
    "Um quadrado de 1 m de lado equivale a um quadrado de 100 cm de lado; a área é 100 × 100 = 10 000 cm².")

add(GM, "Unidades de tempo", "Quantos minutos há em 2 horas e meia?",
    "150 minutos",
    "1 hora = 60 minutos. 2 horas = 120 minutos; meia hora = 30 minutos; 120 + 30 = 150 minutos.")

add(GM, "Posição relativa de retas", "Duas retas que se cruzam num único ponto, mas sem formar ângulo de 90°, dizem-se…",
    "Concorrentes (oblíquas)",
    "Retas concorrentes intersectam-se num só ponto. Se esse ângulo for de 90°, são também perpendiculares; caso contrário, dizem-se apenas concorrentes ou oblíquas.")

add(GM, "Simetria", "O que é um eixo de simetria de uma figura?",
    "Uma linha que divide a figura em duas partes exatamente iguais, uma espelho da outra",
    "Se dobrarmos a figura ao longo do eixo de simetria, as duas metades encaixam perfeitamente uma na outra.")

random.seed(11)
for _ in range(6):
    c, l = random.randint(4, 15), random.randint(2, 10)
    while c == l:
        l = random.randint(2, 10)
    add(GM, "Perímetro e área", f"Um retângulo tem {c} cm de comprimento e {l} cm de largura. Calcula o seu perímetro e a sua área.",
        f"Perímetro = {2*(c+l)} cm; Área = {c*l} cm²",
        f"Perímetro: 2×({c}+{l}) = {2*(c+l)} cm. Área: {c}×{l} = {c*l} cm².")

# =====================================================================
# ÁLGEBRA
# =====================================================================
add(ALG, "Sequências", "Numa sequência, os termos são 3, 7, 11, 15… Qual é a regra de formação e qual é o próximo termo?",
    "Soma-se sempre 4 ao termo anterior; o próximo termo é 19",
    "A diferença entre termos consecutivos é constante: 7−3=4, 11−7=4, 15−11=4. Logo, o termo seguinte é 15+4=19.")

add(ALG, "Sequências", "Numa sequência, os termos são 2, 4, 8, 16… Qual é a regra e qual é o próximo termo?",
    "Cada termo é o dobro do anterior; o próximo termo é 32",
    "2×2=4, 4×2=8, 8×2=16, logo o próximo é 16×2=32.")

add(ALG, "Regularidades", "Numa sequência de figuras feitas com palitos, a 1ª figura tem 4 palitos, a 2ª tem 7 e a 3ª tem 10. Quantos palitos terá a 4ª figura?",
    "13 palitos",
    "A sequência aumenta sempre 3 palitos de figura para figura (4, 7, 10, 13…), porque se acrescenta o mesmo padrão a cada passo.")

add(ALG, "Termo geral (ideia)", "Numa sequência em que o termo de ordem n é dado por 3×n + 1, qual é o valor do 5º termo?",
    "16",
    "Substitui-se n por 5 na expressão: 3×5+1 = 15+1 = 16.")

add(ALG, "Expressões com incógnita", "Se x + 8 = 15, qual é o valor de x?",
    "x = 7",
    "Para isolar x, subtrai-se 8 a ambos os membros: x = 15 − 8 = 7.")

add(ALG, "Expressões com incógnita", "Se 4 × x = 28, qual é o valor de x?",
    "x = 7",
    "Para isolar x, divide-se ambos os membros por 4: x = 28 ÷ 4 = 7.")

add(ALG, "Expressões numéricas", "Calcula o valor de 2 × (3 + 5) − 4.",
    "12",
    "Primeiro os parênteses: 3+5=8. Depois a multiplicação: 2×8=16. Por fim a subtração: 16−4=12.")

add(ALG, "Proporcionalidade direta (ideia)", "Se 3 canetas custam 6 €, quanto custam 5 canetas ao mesmo preço?",
    "10 €",
    "Cada caneta custa 6€÷3=2€. Para 5 canetas: 5×2€=10€. As grandezas são diretamente proporcionais.")

add(ALG, "Regularidades numéricas", "Completa a sequência: 100, 90, 80, 70, __",
    "60",
    "A sequência diminui sempre 10 unidades em cada passo, logo o termo seguinte é 70−10=60.")

add(ALG, "Padrões geométricos", "Numa sequência de quadrados feitos com azulejos, o número de azulejos é sempre o quadrado da ordem da figura (1º=1, 2º=4, 3º=9…). Quantos azulejos tem a 5ª figura?",
    "25 azulejos",
    "A regra é: número de azulejos = ordem × ordem. Para a 5ª figura: 5×5=25.")

add(ALG, "Sinal de igualdade", "A expressão 12 − 5 = 4 + 3 é verdadeira ou falsa?",
    "Verdadeira",
    "12−5=7 e 4+3=7. Como os dois membros são iguais (ambos valem 7), a igualdade é verdadeira.")

add(ALG, "Sequências decrescentes", "Numa sequência, os termos são 50, 44, 38, 32… Qual é o próximo termo?",
    "26",
    "A diferença entre termos consecutivos é sempre −6 (50−6=44, 44−6=38, 38−6=32). O próximo termo é 32−6=26.")

add(ALG, "Pensamento computacional (ideia)", "Se um algoritmo repete a instrução 'soma 3' quatro vezes a partir de 0, que número final se obtém?",
    "12",
    "Repetir 'soma 3' quatro vezes a partir de 0 corresponde a 0+3+3+3+3, ou seja, 4×3=12.")

add(ALG, "Relações entre grandezas", "Um carro percorre 60 km em cada hora, a uma velocidade constante. Quantos km percorre em 3 horas?",
    "180 km",
    "Como a velocidade é constante, a distância é diretamente proporcional ao tempo: 60 km/h × 3 h = 180 km.")

add(ALG, "Números em falta", "Descobre o número em falta: __ + 15 = 42",
    "27",
    "Para descobrir o número em falta, subtrai-se: 42 − 15 = 27. Verificação: 27+15=42.")

# =====================================================================
# DADOS E PROBABILIDADE
# =====================================================================
add(DP, "Tipos de variáveis", "Numa recolha de dados sobre a cor dos olhos dos colegas de turma, a variável em estudo é qualitativa ou quantitativa?",
    "Qualitativa",
    "Uma variável é qualitativa quando as suas respostas são categorias ou qualidades (como cores), e não números. Se fosse a 'idade em anos', seria quantitativa.")

add(DP, "Tipos de variáveis", "A 'altura dos alunos em centímetros' é uma variável qualitativa ou quantitativa?",
    "Quantitativa",
    "É quantitativa porque as respostas são valores numéricos (medidas), que podem ser ordenados e usados em cálculos.")

add(DP, "Frequência absoluta", "Numa turma de 20 alunos, 8 preferem futebol. Qual é a frequência absoluta da resposta 'futebol'?",
    "8",
    "A frequência absoluta é simplesmente o número de vezes que uma resposta ocorre — neste caso, 8 alunos responderam 'futebol'.")

add(DP, "Frequência relativa", "Numa turma de 20 alunos, 8 preferem futebol. Qual é a frequência relativa dessa resposta?",
    "8/20, que simplifica para 2/5 (ou 0,4, ou seja 40%)",
    "A frequência relativa é a frequência absoluta a dividir pelo total de dados: 8÷20 = 0,4 = 40%.")

add(DP, "Moda", "Numa turma, as notas de um teste (0 a 5) foram: 3, 4, 3, 5, 3, 4, 2. Qual é a moda?",
    "3",
    "A moda é o valor que aparece mais vezes no conjunto de dados. O valor 3 aparece 3 vezes, mais do que qualquer outro.")

add(DP, "Tabelas de frequências", "Para que serve uma tabela de frequências?",
    "Para organizar os dados recolhidos, mostrando quantas vezes (frequência) cada valor ou categoria ocorre",
    "É uma forma de resumir um conjunto grande de respostas, tornando mais fácil ver padrões, comparar categorias e construir gráficos.")

add(DP, "Gráficos de barras", "Num gráfico de barras sobre desportos preferidos, qual é a informação dada pela altura de cada barra?",
    "A frequência (o número de respostas) de cada categoria",
    "Quanto mais alta a barra, maior é a frequência dessa categoria — o eixo vertical costuma representar o número de respostas ou a percentagem.")

add(DP, "Pictogramas", "Num pictograma sobre livros lidos, cada símbolo representa 2 livros. Se uma turma tem 5 símbolos, quantos livros leu?",
    "10 livros",
    "Cada símbolo vale 2 livros, então multiplica-se: 5 símbolos × 2 livros = 10 livros.")

add(DP, "Diagrama de caule-e-folhas", "Num diagrama de caule-e-folhas, o que representa o 'caule'?",
    "A(s) ordem(s) de maior valor dos dados (por exemplo, as dezenas), enquanto a 'folha' representa a ordem das unidades",
    "Por exemplo, para o valor 47, o caule é '4' (dezenas) e a folha é '7' (unidades). Vários valores com o mesmo caule partilham a mesma linha.")

add(DP, "Acontecimentos", "Ao lançar um dado equilibrado de 6 faces, sair o número 7 é um acontecimento certo, possível ou impossível?",
    "Impossível",
    "Um dado de 6 faces só tem os números de 1 a 6, por isso nunca pode sair o número 7 — é um acontecimento impossível.")

add(DP, "Acontecimentos", "Ao lançar um dado equilibrado de 6 faces, sair um número entre 1 e 6 é um acontecimento certo, possível ou impossível?",
    "Certo",
    "Como o dado só tem as faces de 1 a 6, é garantido que o resultado estará sempre entre 1 e 6 — é um acontecimento certo.")

add(DP, "Probabilidade (ideia intuitiva)", "Numa saca com 3 bolas vermelhas e 2 bolas azuis, é mais provável tirar uma bola vermelha ou uma bola azul?",
    "Vermelha",
    "Há mais bolas vermelhas (3) do que azuis (2) na saca, por isso é mais provável, ao acaso, sair uma bola vermelha.")

add(DP, "Probabilidade (ideia intuitiva)", "Ao lançar uma moeda equilibrada, qual é a probabilidade de sair 'coroa'?",
    "1 em 2 (ou seja, metade das vezes, 1/2)",
    "Uma moeda tem apenas dois resultados possíveis, igualmente prováveis: cara ou coroa. Logo, cada um tem probabilidade 1/2.")

add(DP, "Média (ideia)", "As idades de 4 colegas são 10, 11, 10 e 9 anos. Qual é a idade média?",
    "10 anos",
    "Soma-se todos os valores e divide-se pelo número de valores: (10+11+10+9)÷4 = 40÷4 = 10.")

add(DP, "Recolha de dados", "Qual é a primeira etapa de um estudo estatístico?",
    "Definir claramente a questão ou o objetivo do estudo, e depois planear como recolher os dados",
    "Antes de recolher dados, é preciso saber exatamente o que se quer descobrir — só assim se escolhe bem a amostra e o método de recolha (inquérito, observação, etc.).")

add(DP, "Amostra e população", "Numa sondagem sobre o desporto favorito, feita a 30 alunos de uma escola com 500 alunos, o que representam os 30 alunos?",
    "Uma amostra da população (os 500 alunos da escola)",
    "A população é o conjunto total que se quer estudar; a amostra é um subconjunto representativo, usado quando não é possível (ou prático) inquirir toda a população.")

add(DP, "Gráficos", "Além do gráfico de barras e do pictograma, indica outro tipo de gráfico usado para organizar dados.",
    "Diagrama de caule-e-folhas (ou gráfico circular / de linhas, consoante o tipo de dados)",
    "A escolha do gráfico depende do tipo de dados e do que se quer destacar: comparações (barras), evolução no tempo (linhas), partes de um todo (circular).")

add(DP, "Interpretação de dados", "Num gráfico de barras, a categoria 'natação' tem a barra mais alta de todas. O que isso significa?",
    "Que 'natação' foi a resposta com maior frequência (a mais escolhida)",
    "A barra mais alta corresponde sempre à categoria com mais respostas — é a moda do conjunto de dados nesse contexto.")

add(DP, "Frequência relativa em percentagem", "Numa turma de 25 alunos, 5 têm animal de estimação um gato. Qual é a percentagem correspondente?",
    "20%",
    "Frequência relativa: 5÷25 = 0,2. Em percentagem, 0,2 corresponde a 20%.")

add(DP, "Contagem e organização", "Antes de construir uma tabela de frequências, o que se costuma fazer aos dados recolhidos em bruto?",
    "Organizá-los, por exemplo através de uma contagem (traços) de cada valor ou categoria",
    "Uma tabela de contagem ajuda a passar de uma lista desordenada de respostas para um resumo organizado, que depois se transforma na tabela de frequências.")

random.seed(3)
for _ in range(4):
    total = random.choice([20, 25, 30, 40])
    fav = random.randint(4, total // 2)
    from math import gcd
    g = gcd(fav, total)
    add(DP, "Frequência relativa", f"Numa turma de {total} alunos, {fav} preferem Ciências. Qual é a frequência relativa, em fração irredutível?",
        f"{fav//g}/{total//g}",
        f"Frequência relativa = {fav}/{total}. Dividindo ambos por {g} (o maior divisor comum), obtém-se a fração irredutível {fav//g}/{total//g}.")

print(f"Total de cartões gerados: {len(cards)}")
random.shuffle(cards)
for i, c in enumerate(cards, 1):
    c["id"] = f"c{i:03d}"

with open("data/5/matematica.json", "w", encoding="utf-8") as f:
    json.dump({"generatedFor": "Matemática 5º ano — Aprendizagens Essenciais", "cards": cards}, f, ensure_ascii=False, indent=2)

by_domain = {}
for c in cards:
    by_domain[c["domain"]] = by_domain.get(c["domain"], 0) + 1
print(by_domain)
