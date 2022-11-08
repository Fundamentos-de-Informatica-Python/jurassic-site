<template>



    <section>
        <h1> Tiranosaurio Rex</h1>
        <small> Keep out!</small>
        <img src="../assets/img/dino_02_trex.png" 
            id="dino" 
            alt="trex">
    </section>
    
    <section  class="center">
        <button onclick="show('dino')">On Trex</button> 
        <button onclick="hide('dino')">Off Trex</button>   
        <button onclick="hide('dino')">Edad Trex?</button> 
    </section>

</template>

<script>


export default {
  name: "DinoTrexView",
  components: {

  }
}
</script>

<style scoped>
@import "../assets/css/estilos.css";

</style>