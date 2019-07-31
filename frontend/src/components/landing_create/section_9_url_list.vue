<template>
  <div class="form-group mb-0">
    <h5>파일 리스트</h5>

    <div class="list_area">
      <div class="list_header">
        <div class="list-group-item text-center d-inline-flex justify-content-between p-1 pt-2 pb-2 text-center"
             style="border-radius: 0; width:100%;">
          <div class="col-4 p-0">URL</div>
          <div class="col-4 p-0">조회수</div>
          <div class="col-4 p-0">DB 수</div>
        </div>
      </div>
      <ul class="text-center list-group list-group-flush text-center">
        <li class="list-group-item list-group-item-action d-inline-flex justify-content-around p-1">
          <div class="col-4 p-0">main_url</div>
          <div class="col-4 p-0">123</div>
          <div class="col-4 p-0">28</div>
        </li>
        <li class="list-group-item list-group-item-action d-inline-flex justify-content-around p-1">
          <div class="col-4 p-0">main_url</div>
          <div class="col-4 p-0">123</div>
          <div class="col-4 p-0">28</div>
        </li>
        <li class="list-group-item list-group-item-action d-inline-flex justify-content-around p-1">
          <div class="col-4 p-0">main_url</div>
          <div class="col-4 p-0">123</div>
          <div class="col-4 p-0">28</div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  export default {
    name: "section_9_url_list",
    props: [
      'page_id'
    ],
    mounted() {

    },
    methods: {}
  }
</script>

<style scoped>

</style>
