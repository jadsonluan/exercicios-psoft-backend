const imclib = (function() {
    function valor_imc(peso, altura) {
        return peso / altura ** 2;
    }

    function classifica(imc) {
        let response = "Indefinido";

        if (imc < 18.5) {
            response = "Abaixo do peso";
        } else if (imc >= 18.5 && imc < 25) {
            response = "Peso normal";
        } else if (imc >= 25 && imc < 30) {
            response = "Sobrepeso";
        } else if (imc >= 30 && imc < 35) {
            response = "Obesidade grau I";
        } else if (imc >= 35 && imc < 40) {
            response = "Obesidade grau II";
        } else if (imc >= 25 && imc < 30) {
            response = "Obesidade grau III";
        }

        return response;
    }

    let obj = {
        calcula: valor_imc,
        classifica: classifica
    };

    return obj;
})();