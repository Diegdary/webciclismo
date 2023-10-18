const idusuario = document.getElementById("consejo").value;

const getmessages = ()=>{
    let listmessage = []
    let jsonusers = {}

    //conseguir lista de usuarios
    axios.get('api/usuarios?ID=12345')
  .then(function (response) {
    listuser=response.data
    listuser.map((item)=>{
        jsonusers[item.id]=item.nombre
    })
  })
  .catch(function (error) {
    console.log(error);
  })


    axios.get('api/comunidades?ID=12345')
  .then(function (response) {

    listmessage = response.data
    console.log(listmessage)
    console.log(jsonusers)
    finalmesagge = ""
    //generar html a partir de la lista de mensajes del db

    listmessage.map((item,index)=>{

        finalmesagge += `
        <article class="comentario">
                <h3 class="nombre">${jsonusers[item.id_usuario]}</h3>
                <p>
                    ${item.mensaje}
                </p>
            </article>
        `

    })

    document.getElementById("coments").innerHTML=finalmesagge;

  })
  .catch(function (error) {
    console.log(error);
  })
}

const sendmessage = ()=>{
    data = {
        "id_usuario": idusuario,
        "mensaje": document.getElementById("consejo").value
    }

    var config = {
        headers: {
            'Content-Type': 'application/json'
        }
    };

    axios.post("api/savecomunidad", JSON.stringify(data), config)
    .then(
        response => {
            console.log('respuesta del backend:', response.data);
            window.location.reload()
        }
    )
    .catch(function (error) {
        console.error('Error al enviar datos:', error);
    });



}

getmessages()

