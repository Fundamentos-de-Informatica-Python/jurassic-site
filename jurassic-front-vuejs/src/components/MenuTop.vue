<template>

  <nav>
      <a href="jurasssic-site-01-trex.html">TRex</a>
      <a href="jurasssic-site-02-raptor.html">Rapotors</a>
      <a href="jurasssic-site-03-mosa.html">Mosasaurio</a>
      <a href="jurasssic-site-04-argsaurio.html">ArgSaurios</a>
      <a href="jurasssic-site-05-0800Dino.html">0-800-Dinos Attack</a>
      <a href="jurasssic-site-06-AddDino.html">0-800-Dino Sugest</a>
  </nav>

  <nav>
      <router-link :to="{name: 'DinoTrexRoute'}">TRex</router-link>
      <router-link :to="{name: 'DinoRaptorRoute'}">Raptors</router-link>
      <router-link :to="{name: 'DinoMosasaurioRoute'}">Mosasaurio</router-link>
      <router-link :to="{name: 'DinoArgSaurioRoute'}">ArgSaurios</router-link>

      <router-link :to="{name: 'HelpAttackDinoRoute'}">0-800-Help</router-link>
      <router-link :to="{name: 'HelpAddDinoRoute'}">0-800-Add</router-link>
  </nav>  


</template>

<script>
export default {
  name: 'MenuTop',
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
