const app = (function() {
    const widget_altura = document.getElementsByTagName("input")[0];
    const widget_peso = document.getElementsByTagName("input")[1];
    const widget_imc = document.getElementById("imc");
    const widget_classificacao = document.getElementById("classificacao");

    function calcule_imc() {
        const peso = Number(widget_peso.value);
        const altura = Number(widget_altura.value);
        let imc = imclib.calcula(peso, altura);

        widget_imc.innerText = "";
        widget_classificacao.innerText = "";

        if (imc > 0) {  
            widget_imc.innerText = imc.toPrecision(3);
            widget_classificacao.innerText = imclib.classifica(imc); 
        }
    }

    var obj = {
        render: calcule_imc
    };

    return obj;
})();
