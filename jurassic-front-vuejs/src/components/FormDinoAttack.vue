<template>



    <section class="formulario">
    
        <form action="mailto:peinchaust@ucema.edu.ar" class="center" method="post" enctype="text/plain">
            <fieldset>
                <legend>Datos de Contacto: [1/3]</legend>
            
                <div>
                    <label for="nombre">Nombre y Apellido</label>
                    <input type="text" name="nombre" id="" size="30" placeholder="Ingrese el Nombre y Apellido"> 
                </div>

                <div>
                    <label for="mail">Mail</label> 
                    <input type="email" name="mail" id="" value="@">
                </div>            
            </fieldset>

            <br>
            <fieldset>
                <legend>Descripción del Dinosaurio: [2/3]</legend>
                <div>
                    <label for="dino">Tipo</label>
                    <select name="dino" id="">
                        <option value="trex">Trex</option>
                        <option value="raptor">raptor</option>
                        <option value="mosasaurio">mosasaurio</option>
                        <option value="Argentinosaurio">Argentinosaurio</option>
                        <option value="triceratops">triceratops</option>
                    </select>
                </div>
            </fieldset>

            <br>
            <fieldset>
                <legend>Descripción del Ataque: [3/3]</legend>
                <div>
                    <br>
                    <label for="ataque">Indique si las razones del ataque, es alguna de las siguientes:</label>
                    <fieldset>
                        <input type="checkbox" name="ataque" id="alimentar">Acerqué la mano para darle de comer <br>
                        <input type="checkbox" name="ataque" id="tierno">Se veía muy tierno, y quise acariciarlo <br>
                        <input type="checkbox" name="ataque" id="selfie">Me quise sacar una selfie, y me puse al lado...<br>
                        <input type="checkbox" name="ataque" id="herviboro">En Jurassic Park los herviboro era innofensivos..<br>                    
                        <br>
                        
                        <input type="button" onclick="ayuda('error')" value="Que hice mal?" />
                    </fieldset>
                </div>

                <span id="error">
                    Recuerde respetar a los animales
                </span>
            </fieldset>

            <input class="btn" type="submit" value="Reportar Ataque" />

        </form>


    </section>    
    

    <br>
    <img src="../assets/img/icono-06-huevo-dino.png" class="center" alt="">


</template>

<script>
export default {
  name: 'FormDinoAttack',
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
