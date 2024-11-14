class CPFValidator:
    def __init__(self, cpf: str):
        self.cpf = cpf

    def validate(self) -> bool:
        # Remove caracteres não numéricos
        cpf = ''.join(filter(str.isdigit, self.cpf))

        # Verifica se o CPF tem 11 dígitos
        if len(cpf) != 11:
            return False

        # Verifica se todos os dígitos são iguais (ex: 111.111.111-11)
        if cpf == cpf[0] * len(cpf):
            return False

        # Validação do primeiro dígito verificador
        sum_first_digit = sum(int(cpf[i]) * (10 - i) for i in range(9))
        first_digit = (sum_first_digit * 10 % 11) % 10
        if first_digit != int(cpf[9]):
            return False

        # Validação do segundo dígito verificador
        sum_second_digit = sum(int(cpf[i]) * (11 - i) for i in range(10))
        second_digit = (sum_second_digit * 10 % 11) % 10
        if second_digit != int(cpf[10]):
            return False

        return True

def main():
    cpf_input = input("Digite o CPF para validação (formato: 123.456.789-09): ")
    validator = CPFValidator(cpf_input)
    if validator.validate():
        print("CPF válido.")
    else:
        print("CPF inválido.")

if __name__ == "__main__":
    main()
