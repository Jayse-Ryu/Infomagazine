<template>
  <div class="form-group row">

    <!--<label class="col-sm-3 col-form-label-sm mt-3" for="status">활성상태</label>
    <div class="col-sm-9 mt-sm-3">
      <label class="switch" for="status">
        <input type="checkbox" id="status" v-model="landing.is_active">
        <span class="slider round"></span>
      </label>
    </div>-->

<!--    <label class="col-sm-3 col-form-label-sm mt-3" for="mobile">모바일 전용</label>-->
<!--    <div class="col-sm-9 mt-sm-3">-->
<!--      <label class="switch" for="mobile">-->
<!--        <input type="checkbox" id="mobile" v-model="landing.is_mobile">-->
<!--        <span class="slider round"></span>-->
<!--      </label>-->
<!--    </div>-->

  </div>
</template>

<script>
  export default {
    name: "section_8_page_opt",
    props: [
      'landing',
      'push_landing'
    ],
    data: () => ({

    }),
    mounted() {

    },
    methods: {

    }
  }
</script>

<style scoped>

</style>
