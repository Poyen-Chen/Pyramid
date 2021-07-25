<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/arrownext.png">
    <HelloWorld msg="Welcome to my Homepage"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld
  }
}
</script>
