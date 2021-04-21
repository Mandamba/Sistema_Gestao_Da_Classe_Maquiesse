const disableds = async () => {
    let inputbatizar = document.getElementById("batizado")
    let inputdatabatismo = document.getElementById("dataquefoibatizado")
    let inputTemDeficiencia = document.getElementById('temdeficiencia')
    let seleccaoDeficiencia = document.getElementById('seleccaoDeficiencia')
    let orfao = document.getElementById("orfao")
    let partedequeeorfao = document.getElementById('partedequeeorfao')
    let SelecionaMembro = document.getElementById('SlecionaMembro')
    let PaiTocoista = document.getElementById('PaiTocoista')
    let inputsenha = document.getElementById('inputsenha')
    let inputemail = document.getElementById('inputemail')
    let botaosubmit = document.getElementById('botaosubmit')

    if (inputemail == '' || inputsenha == '') {
        botaosubmit.disabled = true
    }
    if (inputsenha != '' || inputemail != '') {
        botaosubmit.disabled = false
    }
    if (inputbatizar.value == "Sim") {
        inputdatabatismo.disabled = false;
    }
    if (inputbatizar.value == "Não") {
        //inputdatabatismo.outerHTML=null
        inputdatabatismo.disabled = true;
    }

    if (inputTemDeficiencia.value == 'Sim') {
        seleccaoDeficiencia.disabled = false
    }
    if (inputTemDeficiencia.value == 'Não') {
        seleccaoDeficiencia.disabled = true
        //seleccaoDeficiencia.outerHTML = null
    }
    if (orfao.value == 'Sim') {
        partedequeeorfao.disabled = false
    }
    if (orfao.value == 'Não') {
        partedequeeorfao.disabled = true
    }

    if (SelecionaMembro.value != 'Sleciona o Membro') {
        PaiTocoista.disabled = false
    }

}
