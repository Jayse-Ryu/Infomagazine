<template>
  <main class="preview_html_wrap" v-if="execute">

    <header class="preview_head row" id="preview_head">
      <h3 class="head_title col-6 m-0">랜딩 미리보기</h3>
      <button class="head_button btn btn-danger col-6 m-0" type="button" @click="$emit('update:flag', false)">미리보기 닫기</button>
    </header>

    <iframe id="preview_frame" class="resize_frame" width="80%" height="80%"></iframe>

  </main>
</template>

<script>
  export default {
    name: "preview",
    props: [
      'flag',
      'html'
    ],
    mounted() {
      if(this.execute) {
        this.make_preview()
      }
    },
    data: () => ({
      page_id: ''
    }),
    methods: {
      make_preview() {
        let frame = document.getElementById('preview_frame')

        let head_from = (this.html.indexOf('<head') + 6)
        let head_to = this.html.lastIndexOf('</head>')
        let head_string = this.html.substring(head_from, head_to)

        let body_from = (this.html.indexOf('<body') + 6)
        let body_to = this.html.lastIndexOf('</body>')
        let body_string = this.html.substring(body_from, body_to)

        frame.contentDocument.head.innerHTML = head_string
        frame.contentDocument.body.innerHTML = body_string
      }
    },
    computed: {
      execute() {
        let execute = this.flag
        return execute
      }
    }
  }
</script>

<style lang="scss" scoped>
  .preview_html_wrap {
    position: fixed;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    background: rgba(0,0,0,0.6);
    z-index: 1000;
  }

  .preview_head {
    width: 100%;
    padding: 4% 2%;
    .head_title {
      color: #efefef;
    }
  }

  .resize_frame {
    display: block;
    max-width: 100%;
    min-width: 300px;
    max-height: 100%;
    resize: both !important;
    overflow: auto;
    margin: 0 auto;
    background-color: #ffffff;
  }
</style>
