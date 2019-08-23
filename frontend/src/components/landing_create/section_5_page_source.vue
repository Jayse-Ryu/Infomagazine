<template>
  <div class="form-group row">

    <label class="col-sm-12 col-form-label-sm mt-3" for="page_title">
      <span>페이지 타이틀</span>
      <span class="question badge btn-secondary p-1 align-middle" v-if="window_width > 768"
            v-tooltip="{
                  content: msg.title,
                  placement: 'right',
                  offset: 5,
                  trigger: 'hover',
                  }">?</span>
      <span class="question badge btn-secondary p-1" v-else
            v-tooltip="{
                  content: msg.title,
                  placement: 'right',
                  offset: 5,
                  trigger: 'click',
                  }">?</span>
    </label>
    <div class="col-sm-12">
      <input type="text" class="form-control" id="page_title" maxlength="50"
             :value="title" @keyup="$emit('update:title', $event.target.value)"
             @change="push_landing()">
    </div>

    <label class="col-sm-3 col-form-label-sm mt-3" for="header_script">
      <span>헤더 스크립트</span>
    </label>
    <div class="col-sm-12">
            <textarea type="text" class="form-control" id="header_script" rows="4"
                      :value="header_script"
                      @keyup="$emit('update:header_script', $event.target.value)"
                      @change="push_landing()"></textarea>
    </div>

    <label class="col-sm-3 col-form-label-sm mt-3" for="body_script">
      <span>바디 스크립트</span>
    </label>
    <div class="col-sm-12">
            <textarea type="text" class="form-control" id="body_script" rows="4"
                      :value="body_script"
                      @keyup="$emit('update:body_script', $event.target.value)"
                      @change="push_landing()"></textarea>
    </div>


    <label class="col-sm-3 col-form-label-sm mt-3" for="body_script">
      <span>페이스북 픽셀</span>
    </label>
    <div class="col-sm-9">
      <input type="text" class="form-control" id="facebook" maxlength="50"
             v-model="tracking_info.fb"
             placeholder="아이디 코드"
             @change="push_landing()">
    </div>

    <label class="col-sm-3 col-form-label-sm mt-3" for="body_script">
      <span>카카오 픽셀</span>
    </label>
    <div class="col-sm-9">
      <input type="text" class="form-control" id="kakao" maxlength="50"
             v-model="tracking_info.ka"
             placeholder="아이디 코드"
             @change="push_landing()">
    </div>

    <label class="col-sm-3 col-form-label-sm mt-3" for="body_script">
      <span>구글 애널리틱스</span>
    </label>
    <div class="col-sm-9">
      <input type="text" class="form-control" id="google_a" maxlength="50"
             v-model="tracking_info.ga"
             placeholder="아이디 코드"
             @change="push_landing()">
    </div>

    <label class="col-sm-3 col-form-label-sm mt-3" for="body_script">
      <span>구글 태그매니저</span>
    </label>
    <div class="col-sm-9">
      <input type="text" class="form-control" id="google_tm" maxlength="50"
             v-model="tracking_info.gtm"
             placeholder="아이디 코드"
             @change="push_landing()">
    </div>

    <label class="col-sm-3 col-form-label-sm mt-3" for="body_script">
      <span>구글 디스플레이 네트워크</span>
    </label>
    <div class="col-sm-9">
      <input type="text" class="form-control" id="google_dn" maxlength="50"
             v-model="tracking_info.gdn"
             placeholder="아이디 코드"
             @change="push_landing()">
    </div>


  </div>
</template>

<script>
  export default {
    name: "section_5_page_source",
    props: [
      'window_width',
      'title',
      'header_script',
      'body_script',
      'tracking_info',
      'push_landing'
    ],
    data: () => ({
      msg: {
        title: '사이트 내부 제목입니다.',
      }
    }),
  }
</script>

<style scoped>

</style>
