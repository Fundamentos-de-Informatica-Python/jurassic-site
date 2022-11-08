<template>

  <HeaderSite/>
  <MenuTop/>

  <section>
      <h1>Velociraptor</h1>
      <small>Temibles!!</small>
      <br>
      <img src="../assets/img/dino_03_raptor1.png" class="raptors" >
      <img src="../assets/img/dino_03_raptor2.png" class="raptors" >
  </section>

</template>

<script>
import HeaderSite from "@/components/HeaderSite";
import MenuTop from "@/components/MenuTop";

export default {
  name: "DinoRaptorView",
  components: {
    HeaderSite,
    MenuTop
  }
}
</script>

<style scoped>
@import "../assets/css/estilos.css";

img.raptors {
    border: 10px solid white
}
img.raptors:hover {
    border: 10px solid peru   
}
</style>