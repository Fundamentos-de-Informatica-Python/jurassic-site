<template>

  <HeaderSite/>
  <MenuTop/>
  <FormDinoAttack/>

</template>

<script>
import HeaderSite from "@/components/HeaderSite";
import MenuTop from "@/components/MenuTop";
import FormDinoAttack from "@/components/FormDinoAttack";

export default {
  name: "HelpAttackDinoView",
  components: {
    HeaderSite,
    MenuTop,
    FormDinoAttack
  }
}
</script>

<style scoped>
@import "../assets/css/estilos.css";

</style>