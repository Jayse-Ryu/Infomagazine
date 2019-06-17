<template>

  <div class="form-group row mb-0">
    <label class="col-sm-3 col-form-label-sm mt-3" for="form_group">DB 폼 그룹</label>
    <form class="col-sm-9 mt-sm-3 row ml-0" v-on:submit.prevent="form_group_add">
      <input type="text" class="input_one_btn form-control col-md-11" id="form_group" name="form_group"
             placeholder="폼 그룹 이름" maxlength="50" v-model="form_temp">
      <button type="submit" class="btn btn-primary col-md-1 p-0" name="form_group">추가</button>
    </form>
    <label class="col-sm-3 col-form-label-sm mt-3" for="form_group_list"></label>
    <div class="col-sm-9 mt-sm-3 row ml-0">
      <select class="input_one_btn form-control col-md-11" name="form_group_list" id="form_group_list"
              v-model="form_arrow" @change="form_changed(form_arrow)">
        <option value="-1">그룹을 선택하세요</option>
        <option v-for="item in dynamo_obj.landing_info.form" :value="item.sign">{{ item.name }}</option>
      </select>
      <button type="button" class="btn btn-danger col-md-1 p-0"
              @click.prevent="form_group_delete(form_selected.sign)">
        삭제
      </button>
    </div>

    <!-- Somehow !== is not responsible -->
    <label v-if="form_selected.sign != -1" class="col-sm-3 col-form-label-sm mt-3" for="form_group_bg">
      폼 배경색
    </label>
    <div v-if="form_selected.sign != -1" class="col-sm-9 mt-sm-3 row ml-0">
      <div class="color_wrap form-control col-sm-2" id="form_group_bg">
        <input type="color" v-model="form_selected.bg_color" class="color_picker">
      </div>
      <div class="margin_div"></div>
      <input type="text" v-model="form_selected.bg_color" class="form-control col-sm-5" maxlength="10">
    </div>

    <label v-if="form_selected.sign != -1" class="col-sm-3 col-form-label-sm mt-3" for="opacity_slider">
      배경 불투명도
    </label>
    <div v-if="form_selected.sign != -1" class="col-sm-9 mt-sm-3 row ml-0">
      <div class="form-control col-sm-2">{{ form_selected.opacity * 10 }}%</div>
      <div class="margin_div"></div>
      <div class="slide_container col-sm-5 form-control border-0 p-0">
        <input class="opacity_slider w-100 h-100" id="opacity_slider" type="range" min="0" max="10" value="10"
               v-model="form_selected.opacity">
      </div>
    </div>

    <label v-if="form_selected.sign != -1" class="col-sm-3 col-form-label-sm mt-3" for="form_group_col">
      폼 폰트색
    </label>
    <div v-if="form_selected.sign != -1" class="col-sm-9 mt-sm-3 row ml-0">
      <div class="color_wrap form-control col-sm-2" id="form_group_col">
        <input type="color" v-model="form_selected.tx_color" class="color_picker">
      </div>
      <div class="margin_div"></div>
      <input type="text" v-model="form_selected.tx_color" class="form-control col-sm-5" maxlength="10">
    </div>
  </div>

</template>

<script>
  export default {
    name: "section_2_db_form"
  }
</script>

<style scoped>

</style>
