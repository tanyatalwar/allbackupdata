<template>
  <div id="app">
    <app-message></app-message>
    <router-view></router-view>
    <hr>
     <router-link to="/users/10">Users for ID 10</router-link>
     <router-link to="/users/12">Users for ID 12</router-link>
     <router-link to="/">Home</router-link>
  </div>
</template>

<script>
export default {
  data () {
    return {
    	created(){
    		
    	}
    }
  }
}
</script>

<style>

</style>
