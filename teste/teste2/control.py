import sys

#change path so that other packeges of the aplication can be imported
sys.path.append("../../../api-flask/")

from teste.teste1.user import testando


def chamar():
    testando()