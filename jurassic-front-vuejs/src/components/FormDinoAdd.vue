<template>


    <section class="formulario">

        <fieldset>
            <legend>Agregar Dinosaurio:</legend>
        
            <div>
                <label for="nombre">Nombre</label>
                <input type="text" name="nombre" id="nombre" size="30" placeholder="Ingrese el Nombre"> 
            </div>

            <div>
                <label for="peso">Peso (Tn)</label> 
                <input type="text" name="peso" id="peso" placeholder="Peso en Toneladas">
            </div>

            <br>

            <button id="addDinoButton">
                Agregar Dino
            </button>

            <button id="listDinoButton">
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
export default {
  name: 'FormDinoAdd',
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

    form {
        width: 80%;
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
