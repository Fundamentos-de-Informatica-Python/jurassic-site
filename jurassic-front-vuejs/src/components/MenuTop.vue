<template>

  <nav>
      Welcome to the Jurasic Park!
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
