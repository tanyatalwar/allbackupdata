<template>
<div>
   <h1>Users Overviews</h1>
   <p>Team Id is {{ $route.params.teamId }}</p>
</hr>
<button @click="goHome">Home</button>
</div>
</template>

<script>
export default{
    watch:{
      '$route' (to, from){
         alert(to.params.teamId);
      }
    },
	created(){
    		alert(this.$route.params.teamId);
    	},
    methods:{
       goHome(){
          this.$router.push('/');
       }
    }
} 
</script>