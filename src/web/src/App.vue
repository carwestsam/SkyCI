<template>
  <div id="app">
    <!-- <img src="./assets/logo.png"> -->
    <a href="/">Home</a>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #2c3e50;
  margin-top: 60px;
  margin-left: 10px;
}
* {
  margin:0;
  border:0;
  padding:0;
}
</style>
