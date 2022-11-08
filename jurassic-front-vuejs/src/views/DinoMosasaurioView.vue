<template>

  <HeaderSite/>
  <MenuTop/>

  <section>
      <h1>Mossasaurio</h1>
      <small> Mosa mata TRex !</small>
      <img src="../assets/img/dino_04_mosasaurio.png" id="mosasaurio" class="centrar mivuelta">
  </section>

</template>

<script>
import HeaderSite from "@/components/HeaderSite";
import MenuTop from "@/components/MenuTop";

export default {
  name: "DinoMosasaurioView",
  components: {
    HeaderSite,
    MenuTop
  }
}
</script>

<style scoped>
@import "../assets/css/estilos.css";

.centrar {
    margin: 90px auto;
    display: block;
}
img#mosasaurio {
    margin: 12% auto 10% auto;
    width: 100px;
}
.mivuelta {

    
    -webkit-transition: all 1.3s ease-in-out;
    -moz-transition:    all 1.3s ease-in-out;
    -o-transition:      all 1.3s ease-in-out;
    -ms-transition:     all 1.3s ease-in-out;
}
.mivuelta:hover {
  
    -webkit-transform: rotate(-360deg) scale(8.4);
    -moz-transform:    rotate(-360deg) scale(8.4);
    -o-transform:      rotate(-360deg) scale(8.4);
    -ms-transform:     rotate(-360deg) scale(8.4);
}
</style>