<template>
    <transition name="fade" mode="out-in">
      <div class="select_company_wrap" v-show="company_flag">
        <div class="container company_list_box">

          <h4>고객업체를 먼저 선택해주세요.</h4>

          <div class="form-group row">
            <label class="col-sm-3 col-form-label-sm mt-3" for="company_id">
              <span>고객업체*</span>
            </label>

            <div class="col-sm-9 mt-sm-3">
              <select class="form-control" name="company" id="company_id"
                      v-model="dynamo_obj.landing_info.landing.company">
                <option value="-1">선택하세요</option>
                <option v-for="content in landing_company" :value="content.id">
                  {{content.name }} - {{ content.sub_name }}
                </option>
              </select>
            </div>
          </div>

          <button type="button" class="col btn btn-info mt-3" @click="first_check">선택</button>
          <router-link to="/landing">
            <button type="button" class="btn btn-dark col-12 mt-2">취소</button>
          </router-link>
        </div>
      </div>
    </transition>
</template>

<script>
    export default {
        name: "popup_2_company"
    }
</script>

<style scoped>

</style>
