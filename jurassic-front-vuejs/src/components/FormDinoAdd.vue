<template>


    <section class="formulario">

        <fieldset>
            <legend>Agregar Dinosaurio:</legend>
        
            <div>
                <label for="nombre">Nombre</label>
                <input type="text" v-model="nombre" size="30" placeholder="Ingrese el Nombre"> 
            </div>

            <div>
                <label for="peso">Peso (Tn)</label> 
                <input type="text" v-model="peso"  placeholder="Peso en Toneladas">
            </div>

            <br>

            <button id="addDinoButton" @click="addDino">
                Agregar Dino
            </button>

            <button id="listDinoButton" @click="listDinos">
                Ver Dinos
            </button>

        </fieldset>


        <br>


        <div id="dino-container">
            <div id="div-table">
                <div id="data-loader" class="loader"></div>
                <table id="dino-table" hidden>
                    <thead>
                        <tr>
                            <th>Nombre</th>
                            <th>Peso</th>
                            <th>Imagen</th>
                        </tr>
                    </thead>
                    <tbody>
                    </tbody>
                </table>
            </div>
        </div>

    </section>    
    

</template>

<script>
import axios from 'axios';

export default {
  name: 'FormDinoAdd',
  data() {
    return {
      nombre: "",
      peso: ""
    }
  },
  methods: {
    addDino() {
    
     
        axios.post('http://localhost:5000/api/jurassic/dinos', {
                'height': '13m',
                'img':  this.nombre + '.jpg',
                'long': '2m',
                'name': this.nombre,
                'type': 'carnivoro',
                'weight': this.peso
            })
            .then(resp => console.log(resp))
            .catch(e => console.log('Error!!!', e))
    },
    listDinos() {

        axios.get('http://127.0.0.1:5000/api/jurassic/dinos')
            .then(function (response) {

                let dinoTableBody = document.getElementById('dino-table').getElementsByTagName('tbody')[0];

                dinoTableBody.innerHTML = "";

                for (let i=0 ; i<response.data.length ; i++) {
                    
                    let dinoItem = response.data[i];

                    let dinoTableBody = document.getElementById('dino-table').getElementsByTagName('tbody')[0];
                    let row = dinoTableBody.insertRow(-1);

                    let cell0 = row.insertCell(0);
                    cell0.innerHTML = dinoItem.name;

                    let cell1 = row.insertCell(1);
                    cell1.innerHTML = dinoItem.weight;

                    let cell2 = row.insertCell(2);
                    cell2.innerHTML = dinoItem.img;
                }
                document.getElementById("data-loader").hidden = true;
                document.getElementById("dino-table").hidden = false;

            })
            .catch(function (error) {
                console.log(error);
                alert("No se puedo recuperar la lista de Dinos!");
        });
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

    form {
        width: 80%;
        text-align: left;
    }
    label {
        display: block;
        margin: .5em 0 0 0;
    }
    .btn {
        display: block;
        margin: 1em 0;
    }

    div {
        margin: .4em 0;
    }
    
    div label {
        width: 25%;
        float: left;
        
    }
    div#container {
        width: 70%;
        display: flex;
        flex-flow: column;
        float: left;

    }

</style>
