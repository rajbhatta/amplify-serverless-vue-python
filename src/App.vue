<template>
  <div id="nav" class="container mx-auto"> <!-- start of upper nav container -->
    <div class="box-border  border-4"> <!--start of box-border -->
      <router-link to="/">Dashboard</router-link> |
      <router-link to="/add">Add Sensor</router-link>
    </div> <!-- end of box-border -->
  </div> <!-- end of upper nav container -->
  <router-view />
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
<style src="./assets/tailwind.css"></style>
