from src.my_module import CPFValidator

def test_cpf_validator_valid():
    validator = CPFValidator("123.456.789-09")
    assert validator.validate() == False

def test_cpf_validator_invalid():
    validator = CPFValidator("111.111.111-11")
    assert validator.validate() == False
