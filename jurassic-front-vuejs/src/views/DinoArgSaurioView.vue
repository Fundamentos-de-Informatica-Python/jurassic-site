<template>

  <HeaderSite/>
  <MenuTop/>

    <section>
        <h1>Argentinosaurio</h1>
        <small> Bien Argento!</small>
        <img src="../assets/img/dino_01_argentinosaurus.jpg" class="dino big">
    </section>

</template>

<script>
import HeaderSite from "@/components/HeaderSite";
import MenuTop from "@/components/MenuTop";

export default {
  name: "DinoArgSaurioView",
  components: {
    HeaderSite,
    MenuTop
  }
}
</script>

<style scoped>
@import "../assets/css/estilos.css";

</style>