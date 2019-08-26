<template>
  <div class="form-group mb-0">
    <div class="col-12 row p-0 m-0">
      <h5 class="col-sm-10 p-0 mb-3">
        파일 리스트
        <span class="question badge btn-secondary p-1 align-middle" v-if="window_width > 768"
              v-tooltip="{
                      content: msg.file_list,
                      placement: 'right',
                      offset: 5,
                      trigger: 'hover',
                      }">?</span>
        <span class="question badge btn-secondary p-1 align-middle" v-else
              v-tooltip="{
                      content: msg.file_list,
                      placement: 'right',
                      offset: 5,
                      trigger: 'click',
                      }">?</span>
      </h5>
      <div class="col-sm-2 p-0 mb-3">
        <button type="button" class="btn btn-outline-primary w-100 p-0" @click="server_refresh">서버 새로고침</button>
      </div>
    </div>

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
          <a :href="item" target="_blank" class="col-8" style="word-break: break-all;">{{ item }}</a>
          <button type="button" class="btn btn-sm btn-outline-success p-0 col-2 mr-1" @click="overwrite_url(item)">덮어쓰기</button>
          <button type="button" class="btn btn-sm btn-danger p-0 col-2" @click="delete_url(item)">삭제</button>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  export default {
    name: "section_9_url_list",
    props: [
      'window_width',
      'page_id',
      'url_list',
      'del_url'
    ],
    data: () => ({
      msg: {
        file_list: '서버상에 이미 등록되어있는 파일들은 수정, 삭제가 24시간 뒤에 이루어집니다. 파일대로 서버를 즉시 갱신 시키려면 새로고침 해주세요.'
      }
    }),
    mounted() {

    },
    methods: {
      delete_url(key) {
        this.del_url(key)
      },
      overwrite_url(key) {
        let set = key.replace('https://landings.infomagazine.xyz/' + this.page_id + '/', '')
        let set_2 = set.replace('.html', '')
        axios.put(this.$store.state.endpoints.baseUrl + 'landing_pages/' + this.page_id + '/landing_urls/' + set_2 + '/')
          .then((response) => {
            console.log('over write test ', response)
          })
          .catch((error) => {
            alert('덮어쓰기 중 오류가 발생하였습니다.')
            console.log(error)
          })
      },
      server_refresh() {
        this.$store.state.pageOptions.loading = true
        axios.put(this.$store.state.endpoints.baseUrl + 'landing_pages/' + this.page_id + '/landing_urls/')
          .then(() => {
            alert('서버가 갱신되었습니다.')
            this.$store.state.pageOptions.loading = false
          })
          .catch((error) => {
            alert('서버갱신 중 오류가 발생하였습니다.')
            console.log(error)
            this.$store.state.pageOptions.loading = false
          })
      }
    },
    computed: {}
  }
</script>

<style scoped>

</style>
