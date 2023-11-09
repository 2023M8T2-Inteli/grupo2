import re

def screw_path():
   return "A caminho do parafuso"

def screwdriver_path():
    return "A caminho da chave de fenda"

def nail_path():
    return "A caminho do prego"

intent_dict = {
    r'(?i)^Eu gostaria de um parafuso$': "screw",
    r'(?i)^Eu gostaria de uma chave de fenda$': "screwdriver",
    r'(?i)^Eu gostaria de um prego$': "nail",
}

tools_dict = {
    "screw": screw_path,
    "screwdriver": screwdriver_path,
    "nail": nail_path,
}

action_dict = {
    "screw": screw_path,
    "screwdriver": screwdriver_path,
    "nail": nail_path,
}

command = input("Olá, temos estas peças disponíveis:\n - Parafuso \n - Prego \n - Chave de fenda \n\n Digite a peça que você gostaria: ")
for key, value in intent_dict.items():
    pattern = re.compile(key)
    groups = pattern.findall(command)
    if groups:
        print(f"{action_dict[value]()}", end=" ")
print()
