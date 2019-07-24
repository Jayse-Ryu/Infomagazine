<template>
  <main>
    <div v-html="html"></div>
  </main>
</template>

<script>
  export default {
    name: "preview",
    mounted() {
      this.page_id = this.$route.params.landing_id

      axios.get(this.$store.state.endpoints.baseUrl + 'landing_pages/' + this.page_id + '/preview/')
        .then((response) => {
          console.log(response.data.data)
          this.html = response.data.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
    data: () => ({
      page_id: '',
      html: {}
    }),
    methods: {
      temp() {
      }
    }
  }
</script>

<style scoped>

</style>
