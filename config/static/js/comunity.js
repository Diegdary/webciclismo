const getmessages = ()=>{
    let list = []

    axios.get('api/comunidades?ID=12345')
  .then(function (response) {
    // handle success
    console.log(response.data);
    list = response.data
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .finally(function () {
    // always executed
  });

  

}

getmessages()