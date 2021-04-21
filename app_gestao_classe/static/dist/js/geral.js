const requestData = async (url) => {
    const response = await fetch(`http://127.0.0.1:8000/${url}`)
    const dados = response.json()
    return dados
}
/*const carregarProvincia = () => {

}*/

const carregarMunicipio = (id) => {
    // let idPro = document.getElementById(`${id}`).value
    const municipiosss = document.getElementById('munici11')
    municipiosss.innerHTML = ""
    requestData("get_municipio_json").then(result => {
        const municipios = result.municipios
        const dados = municipios.map(municipio => {
            if (municipio.provinciaId_id == id) {
                const option = document.createElement('option')
                option.textContent = municipio.municipio
                option.setAttribute("class", "item")
                option.setAttribute("value", municipio.id)
                municipiosss.appendChild(option)
            }

        })
    })

}
const carregarArea = (id) => {
    // let idPro = document.getElementById(`${id}`).value
    const areasss = document.getElementById('area11')
    areasss.innerHTML = ""
    requestData("get_areas").then(result => {
        const areas = result.areas
        const dados = areas.map(area => {
            if (area.triboId_id == id) {
                const option = document.createElement('option')
                option.textContent = area.area
                option.setAttribute("class", "item")
                option.setAttribute("value", area.id)
                areasss.appendChild(option)
            }

        })
    })

}

requestData("get_provincias_json").then(result => {
    const provincias = result.provincia
    const dados = provincias.map(provincia => {
        const provinciasss = document.getElementById('prov')
        const option = document.createElement('option')
        option.textContent = provincia.provincia
        option.setAttribute("class", "item")
        option.setAttribute("value", provincia.id)
        provinciasss.appendChild(option)
    })
})

requestData("get_tribo").then(result => {
    const tribos = result.tribo
    const dados = tribos.map(tribo => {
        const triboss = document.getElementById('tribo')
        const option = document.createElement('option')
        option.textContent = tribo.tribo
        option.setAttribute("class", "item")
        option.setAttribute("value", tribo.id)
        triboss.appendChild(option)
    })
})

const prev = async () => {
    const profile_pic = document.getElementById('profile_pic')
    const previewContainer = document.querySelector('.image-preview')
    const previewImage = previewContainer.querySelector('.image-preview__imagem')
    const previewDefaultText = previewContainer.querySelector('.image-preview__default-text')
    //profile_pic.addEventListener('change', function () {
    const file = profile_pic.files[0]

    if (file) {
        const reader = new FileReader();
        previewDefaultText.style.display = "none"
        previewImage.style.display = "block"
        previewImage.style.borderRadius = "20px"
        previewImage.style.height = "150px"
        previewImage.style.width = "120px"
        reader.addEventListener("load", function () {
            previewImage.setAttribute("src", this.result)
        })
        reader.readAsDataURL(file)
    }
    //    })
}
