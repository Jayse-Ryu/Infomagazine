<template>
  <div class="form-group mb-0">
    <h5>파일 리스트</h5>

    <div class="list_area">
      <div class="list_header">
        <div class="list-group-item text-center d-inline-flex justify-content-between p-1 pt-2 pb-2 text-center"
             style="border-radius: 0; width:100%;">
          <div class="col-12 p-0">파일 URL</div>
        </div>
      </div>
      <ul class="text-center list-group list-group-flush text-center">
        <li v-if="!url_list.length"
            class="list-group-item list-group-item-action d-inline-flex justify-content-around p-1">
          <span>파일 없음</span>
        </li>
        <li v-else class="list-group-item list-group-item-action d-inline-flex justify-content-around p-1"
            v-for="item in url_list">
          <a :href="item" target="_blank" class="col-11" style="word-break: break-all;">{{ item }}</a>
          <button type="button" class="btn btn-sm btn-danger p-0 col-1" @click="delete_url">삭제</button>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  export default {
    name: "section_9_url_list",
    props: [
      'page_id',
      'url_list',
      'del_url'
    ],
    mounted() {

    },
    methods: {
      delete_url() {
        this.del_url()
      }
    },
    computed: {

    }
  }
</script>

<style scoped>

</style>
