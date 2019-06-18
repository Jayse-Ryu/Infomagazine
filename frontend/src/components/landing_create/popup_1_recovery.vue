<template>

  <transition name="fade" mode="out-in">

    <!-- When first access for create landing, show the company choice modal -->
    <div class="select_company_wrap" v-show="auto_flag">
      <div class="container company_list_box">

        <h4>임시저장된 랜딩페이지가 있습니다.</h4>

        <div class="form-group row">
          <label class="col-sm-3 col-form-label-sm mt-3" for="auto_id">
            <span>랜딩선택</span>
          </label>

          <div class="col-md-8 mt-sm-3">
            <select class="form-control" name="company" id="auto_id"
                    v-model="recovery">
              <option value="-1">선택하세요</option>
              <option v-for="content in auto_saved" :value="content.LandingNum">
                {{content.landing_info.landing.company_name }} / {{ content.landing_info.landing.init_date }}
              </option>
            </select>
          </div>
          <div class="col-md-1 mt-sm-3 pl-md-0">
            <button type="button" class="btn btn-danger p-md-0 w-100 h-100" @click="auto_saved_delete">삭제</button>
          </div>
        </div>

        <button type="button" class="col btn btn-info mt-3" @click="auto_saved_detail">선택</button>
        <button type="button" class="btn btn-secondary col-12 mt-2" @click="auto_saved_not">선택 안함</button>
        <router-link to="/landing">
          <button type="button" class="btn btn-dark col-12 mt-2">취소</button>
        </router-link>
      </div>
    </div>
  </transition>
</template>

<script>
  export default {
    name: "popup_1_recovery"
  }
</script>

<style scoped>

</style>
