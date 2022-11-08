<template>

  <HeaderSite/>
  <MenuTop/>
  <FormDinoAdd/>

<br>
Help Add Dino

</template>

<script>
import HeaderSite from "@/components/HeaderSite";
import MenuTop from "@/components/MenuTop";
import FormDinoAdd from "@/components/FormDinoAdd";

export default {
  name: "HelpAddDinoView",
  components: {
    HeaderSite,
    MenuTop,
    FormDinoAdd
  }
}
</script>

<style scoped>
@import "../assets/css/estilos.css";

</style>