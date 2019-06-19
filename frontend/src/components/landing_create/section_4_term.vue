<template>
  <div>

    <div class="form-group row mb-0">

      <label class="col-sm-3 col-form-label-sm mt-3" for="term_status">약관</label>

      <div class="col-sm-9 mt-sm-3">
        <label class="switch" for="term_status">
          <input type="checkbox" id="term_status" :value="term_switch"
                 @change="$emit('update:term_switch', !term_switch)">
          <span class="slider round"></span>
        </label>
      </div>

      <label v-if="term_switch" class="col-sm-3 col-form-label-sm mt-3"
             for="term_switch">
        약관 이미지
      </label>

      <div v-if="term_switch" class="col-sm-9 mt-sm-3">
        <label class="switch" for="term_switch">
          <input type="checkbox" id="term_switch" :value="image_switch"
                 @change="term_file_delete()">
          <span class="slider round"></span>
        </label>
      </div>

    </div>

    <div class="form-group row"
         v-if="term_switch && image_switch">
      <label class="col-sm-3 col-form-label-sm mt-3" for="term_img">약관 이미지 파일</label>
      <div class="col-sm-9 mt-sm-3 row ml-0">
        <input type="file" class="input_one_btn form-control col-md-11 pt-1" id="term_img" placeholder="이미지"
               ref="term_file_input" @change="term_file_add()" accept="image/*">
        <button type="button" class="btn btn-danger col-md-1 p-0" @click.prevent="term_file_delete()">삭제</button>
      </div>
    </div>

    <div class="form-group row"
         v-if="term_switch && !image_switch">
      <label class="col-sm-3 col-form-label-sm mt-3" for="term_title">약관 제목</label>
      <div class="col-sm-9 mt-sm-3">
        <input type="text" class="form-control" id="term_title" placeholder="title"
               v-model="term.title">
      </div>
      <label class="col-sm-3 col-form-label-sm mt-3" for="term_cont">약관 내용</label>
      <div class="col-sm-9 mt-sm-3">
                    <textarea type="text" class="form-control" id="term_cont" rows="4" placeholder="content"
                              v-model="term.content"></textarea>
      </div>


    </div>


  </div>
</template>

<script>
  export default {
    name: "section_3_term",
    props: [
      'term_switch',
      'image_switch',
      'term',
    ],
    mounted() {

    },
    methods: {
      term_file_add() {
        /* When file data changed */
        // let file_data = $event.target.files[0]
        // this.dynamo_obj.landing_info.term.image = file_data
      },
      term_file_delete() {
        this.$emit('update:image_switch', !this.image_switch)
        /* Remove file data */
        // if (this.$refs.term_file_input) {
        //   this.$refs.term_file_input.value = null
        // }
        // this.dynamo_obj.landing_info.term.image = null
      },
    }
  }
</script>

<style scoped>

</style>
