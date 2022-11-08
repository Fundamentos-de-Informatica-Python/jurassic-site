<template>

  <HeaderSite/>
  <MenuTop/>

<BodyHome/>

<br>
Raptor
</template>

<script>
import HeaderSite from "@/components/HeaderSite";
import MenuTop from "@/components/MenuTop";
import BodyHome from "@/components/BodyHome";
// import FormDinoAdd from "@/components/FormDinoAdd";
// import FormDinoAttack from "@/components/FormDinoAttack";




export default {
  name: "DinoRaptorView",
  components: {
    HeaderSite,
    MenuTop,
    BodyHome
  }
}
</script>

<style scoped>
@import "../assets/css/estilos.css";

</style>