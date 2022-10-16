<template>
    <div id="main">
    <NavBar></NavBar>
    <div class="container">
      <router-view />
    </div>
  </div> 
</template>
<script>
import NavBar from '../components/Parts/NavBar.vue'
export default {
  name: 'MainView',
  components: { NavBar }
}
</script>